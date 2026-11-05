from unittest.mock import MagicMock
from services.book_service import BookService


def test_service_cache_aside_miss():
    mock_repo = MagicMock()
    mock_redis = MagicMock()

    mock_redis.get.return_value = None
    mock_repo.get_by_id.return_value = {"id": 1, "title": "Книга"}

    service = BookService(mock_repo, mock_redis)
    book, source = service.get_book_by_id(1)

    assert source == "Database"
    assert book["title"] == "Книга"
    mock_redis.setex.assert_called_once()