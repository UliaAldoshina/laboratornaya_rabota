from flask import Flask, request, jsonify
from repository.book_repository import BookRepository
from services.book_service import BookService
import redis

app = Flask(__name__)

db_path = "database.db"
repo = BookRepository(db_path)

try:
    redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)
    redis_client.ping()
except Exception:
    redis_client = None

service = BookService(repo, redis_client)


@app.route("/books", methods=["GET"])
def get_books():
    books = repo.get_all()
    return jsonify(books), 200


@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id: int):
    book, source = service.get_book_by_id(book_id)
    if not book:
        return jsonify({"code": "NOT_FOUND", "error": f"Книга с id={book_id} не найдена"}), 404
    return jsonify({"source": source, "data": book}), 200


@app.route("/books", methods=["POST"])
def create_book():
    data = request.get_json()
    if not data or "title" not in data or "author_id" not in data:
        return jsonify({"code": "BAD_REQUEST", "error": "Неверные данные запроса"}), 400

    try:
        book_id = repo.create(
            title=data["title"],
            author_id=data["author_id"],
            year=data.get("year", 2023),
            price=data.get("price", 0.0)
        )
        new_book = repo.get_by_id(book_id)
        return jsonify(new_book), 201
    except Exception as e:
        return jsonify({"code": "INTERNAL_ERROR", "error": str(e)}), 400


@app.route("/books/<int:book_id>", methods=["PATCH"])
def patch_book(book_id: int):
    data = request.get_json()
    existing = repo.get_by_id(book_id)
    if not existing:
        return jsonify({"code": "NOT_FOUND", "error": f"Книга с id={book_id} не найдена"}), 404

    success = service.update_book(book_id, {
        "title": data.get("title", existing["title"]),
        "year": data.get("year", existing["year"]),
        "price": data.get("price", existing["price"]),
        "is_available": data.get("is_available", existing["is_available"])
    })

    if success:
        updated = repo.get_by_id(book_id)
        return jsonify(updated), 200
    return jsonify({"code": "UPDATE_FAILED", "error": "Не удалось обновить запись"}), 400


@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id: int):
    success = repo.delete(book_id)
    if not success:
        return jsonify({"code": "NOT_FOUND", "error": f"Книга с id={book_id} не найдена"}), 404
    return "", 204


if __name__ == "__main__":
    app.run(debug=True, port=5000)