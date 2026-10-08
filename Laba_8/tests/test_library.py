
# Автоматические тесты (минимум 5)

import pytest
from repositories.memory_repository import InMemoryRepository
from services.library_service import LibraryService
from factories.book_factory import ItemFactory
from strategies.standard_period import StandardPeriodStrategy
from strategies.teacher_period import TeacherPeriodStrategy
from models.enums import BookStatus, ItemType


# ============ 1. ТЕСТ FACTORY ============

def test_factory_creates_printed_book():
    item = ItemFactory.create("printed", "Книга", "Автор", pages=100)
    assert item.item_type == ItemType.PRINTED
    assert item.pages == 100


def test_factory_creates_ebook():
    item = ItemFactory.create("ebook", "Эл. книга", "Автор", file_size=5.5)
    assert item.item_type == ItemType.EBOOK
    assert item.file_size == 5.5


# ============ 2. ТЕСТ STRATEGY ============

def test_standard_and_teacher_strategies_differ():
    standard = StandardPeriodStrategy()
    teacher = TeacherPeriodStrategy()
    assert standard.get_days() != teacher.get_days()
    assert standard.get_days() == 14
    assert teacher.get_days() == 60


# ============ 3. ТЕСТ REPOSITORY ============

def test_repository_add_and_get():
    repo = InMemoryRepository()
    item = ItemFactory.create("printed", "Книга", "Автор")
    repo.add(item)
    assert repo.get(item.id) is item
    assert len(repo.get_all()) == 1


def test_repository_delete():
    repo = InMemoryRepository()
    item = ItemFactory.create("printed", "Книга", "Автор")
    repo.add(item)
    repo.delete(item.id)
    assert repo.get(item.id) is None


# ============ 4. ТЕСТ ОСНОВНОЙ ОПЕРАЦИИ ============

def test_issue_changes_status():
    repo = InMemoryRepository()
    service = LibraryService(repo)
    item = ItemFactory.create("printed", "Книга", "Автор")
    service.add_item(item)

    result = service.issue(item.id, "Иванов", StandardPeriodStrategy())
    assert "Выдано" in result
    assert item.status == BookStatus.ISSUED
    assert item.issued_to == "Иванов"


def test_cannot_issue_already_issued():
    repo = InMemoryRepository()
    service = LibraryService(repo)
    item = ItemFactory.create("printed", "Книга", "Автор")
    service.add_item(item)
    service.issue(item.id, "Иванов", StandardPeriodStrategy())

    result = service.issue(item.id, "Петров", StandardPeriodStrategy())
    assert "Нельзя выдать" in result


# ============ 5. ТЕСТ COMMAND ============

def test_return_command_restores_status():
    repo = InMemoryRepository()
    service = LibraryService(repo)
    item = ItemFactory.create("printed", "Книга", "Автор")
    service.add_item(item)
    service.issue(item.id, "Иванов", StandardPeriodStrategy())

    result = service.return_item(item.id)
    assert "Возвращено" in result
    assert item.status == BookStatus.AVAILABLE
    assert item.issued_to is None


def test_reserve_command_changes_status():
    repo = InMemoryRepository()
    service = LibraryService(repo)
    item = ItemFactory.create("printed", "Книга", "Автор")
    service.add_item(item)

    result = service.reserve(item.id, "Сидоров")
    assert "Забронировано" in result
    assert item.status == BookStatus.RESERVED