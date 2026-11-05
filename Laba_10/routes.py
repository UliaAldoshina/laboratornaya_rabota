from flask import Blueprint, request, jsonify
from service import BookService
from repository import BookRepository
from exceptions import BookNotFoundError, ValidationError

api_bp = Blueprint("api", __name__)
repo = BookRepository()
service = BookService(repo)


@api_bp.errorhandler(BookNotFoundError)
def handle_not_found(error):
    return jsonify({"error": str(error), "code": "NOT_FOUND"}), 404


@api_bp.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify({"error": str(error), "code": "BAD_REQUEST"}), 400


@api_bp.route("/books", methods=["GET"])
def get_books():
    author = request.args.get("author")
    genre = request.args.get("genre")
    sort_by = request.args.get("sort")
    order = request.args.get("order", "asc")

    books = service.get_books(author=author, genre=genre, sort_by=sort_by, order=order)
    return jsonify(books), 200


@api_bp.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id: int):
    book = service.get_book(book_id)
    return jsonify(book), 200


@api_bp.route("/books", methods=["POST"])
def create_book():
    data = request.get_json(silent=True)
    if data is None:
        raise ValidationError("Отсутствует JSON в теле запроса")
    created = service.create_book(data)
    return jsonify(created), 201


@api_bp.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id: int):
    data = request.get_json(silent=True)
    if data is None:
        raise ValidationError("Отсутствует JSON в теле запроса")
    updated = service.update_book(book_id, data)
    return jsonify(updated), 200


@api_bp.route("/books/<int:book_id>", methods=["PATCH"])
def patch_book(book_id: int):
    data = request.get_json(silent=True)
    if data is None:
        raise ValidationError("Отсутствует JSON в теле запроса")
    patched = service.patch_book(book_id, data)
    return jsonify(patched), 200


@api_bp.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id: int):
    service.delete_book(book_id)
    return "", 204


@api_bp.route("/books/by-author", methods=["GET"])
def search_by_author():
    author = request.args.get("name", "")
    if not author:
        raise ValidationError("Параметр 'name' обязателен для поиска")
    result = service.search_by_author(author)
    return jsonify(result), 200