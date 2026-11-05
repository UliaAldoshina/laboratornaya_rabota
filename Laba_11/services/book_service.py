import json
import redis
from repository.book_repository import BookRepository


class BookService:
    def __init__(self, repository: BookRepository, redis_client=None):
        self.repo = repository
        self.redis = redis_client
        self.TTL = 60

    def get_book_by_id(self, book_id: int):
        cache_key = f"book:{book_id}"

        if self.redis:
            try:
                cached_data = self.redis.get(cache_key)
                if cached_data:
                    return json.loads(cached_data), "Redis Cache"
            except Exception:
                pass

        book = self.repo.get_by_id(book_id)
        if book and self.redis:
            try:
                self.redis.setex(cache_key, self.TTL, json.dumps(book))
            except Exception:
                pass
            return book, "Database"

        return book, "Database"

    def update_book(self, book_id: int, data: dict) -> bool:
        success = self.repo.update(
            book_id,
            data.get("title"),
            data.get("year"),
            data.get("price"),
            data.get("is_available", True)
        )
        if success and self.redis:
            try:
                self.redis.delete(f"book:{book_id}")
            except Exception:
                pass
        return success