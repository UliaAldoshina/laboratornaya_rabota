from typing import List, Optional
from models import Book
from repository import BookRepository
from exceptions import BookNotFoundError
from schemas import validate_book_data


class BookService:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def get_books(
        self,
        author: Optional[str] = None,
        genre: Optional[str] = None,
        sort_by: Optional[str] = None,
        order: str = "asc"
    ) -> List[dict]:
        books = self.repository.get_all()

        if author:
            books = [b for b in books if author.lower() in b.author.lower()]

        if genre:
            books = [b for b in books if genre.lower() == b.genre.lower()]

        if sort_by and hasattr(Book, sort_by):
            reverse = (order.lower() == "desc")
            books = sorted(books, key=lambda b: getattr(b, sort_by), reverse=reverse)

        return [b.to_dict() for b in books]

    def get_book(self, book_id: int) -> dict:
        book = self.repository.get_by_id(book_id)
        if not book:
            raise BookNotFoundError(f"Книга с id={book_id} не найдена")
        return book.to_dict()

    def create_book(self, data: dict) -> dict:
        validate_book_data(data, is_patch=False)
        book = Book.from_dict(data)
        created_book = self.repository.create(book)
        return created_book.to_dict()

    def update_book(self, book_id: int, data: dict) -> dict:
        existing = self.repository.get_by_id(book_id)
        if not existing:
            raise BookNotFoundError(f"Книга с id={book_id} не найдена")

        validate_book_data(data, is_patch=False)
        updated_book = Book.from_dict({**data, "id": book_id})
        return self.repository.update(updated_book).to_dict()

    def patch_book(self, book_id: int, data: dict) -> dict:
        existing = self.repository.get_by_id(book_id)
        if not existing:
            raise BookNotFoundError(f"Книга с id={book_id} не найдена")

        validate_book_data(data, is_patch=True)
        current_data = existing.to_dict()
        current_data.update(data)

        updated_book = Book.from_dict(current_data)
        return self.repository.update(updated_book).to_dict()

    def delete_book(self, book_id: int) -> None:
        if not self.repository.delete(book_id):
            raise BookNotFoundError(f"Книга с id={book_id} не найдена")

    def search_by_author(self, author_name: str) -> List[dict]:
        books = self.repository.get_all()
        result = [b.to_dict() for b in books if author_name.lower() in b.author.lower()]
        return result