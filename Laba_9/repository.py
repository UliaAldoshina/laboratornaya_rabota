from models import Calculation
class CalculationRepository:
    def __init__(self):
        self._storage = {}
        self._counter = 1

    def add(self, expression: str, result: float):
        calc_id = self._counter
        calculation = Calculation(id=calc_id, expression=expression, result=result)
        self._storage[calc_id] = calculation
        self._counter += 1
        return calculation

    def get(self, calc_id: int):
        return self._storage.get(calc_id)

    def get_all(self):
        return list(self._storage.values())

    def update(self, calc_id: int, expression: str, result: float):
        if calc_id not in self._storage:
            return None
        calculation = self._storage[calc_id]
        calculation.expression = expression
        calculation.result = result
        return calculation

    def delete(self, calc_id: int):
        if calc_id in self._storage:
            return self._storage.pop(calc_id)
        return None