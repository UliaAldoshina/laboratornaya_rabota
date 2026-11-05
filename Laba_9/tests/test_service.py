import pytest
from repository import CalculationRepository
from service import CalculationService


def test_calculate_success():
    repo = CalculationRepository()
    service = CalculationService(repo)

    calc = service.calculate("10 * 2 + 5")
    assert calc.result == 25.0
    assert len(service.get_all()) == 1


def test_calculate_invalid_expression():
    repo = CalculationRepository()
    service = CalculationService(repo)

    with pytest.raises(ValueError):
        service.calculate("invalid_code_or_chars()")