from repository import CalculationRepository


def test_add_and_get():
    repo = CalculationRepository()
    calc = repo.add("2 + 2", 4.0)

    assert calc.id == 1
    assert calc.expression == "2 + 2"
    assert calc.result == 4.0

    fetched = repo.get(1)
    assert fetched == calc


def test_delete_object():
    repo = CalculationRepository()
    repo.add("10 - 5", 5.0)

    deleted = repo.delete(1)
    assert deleted is not None
    assert repo.get(1) is None