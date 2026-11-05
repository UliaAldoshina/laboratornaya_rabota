class CalculationService:
    def __init__(self, repository):
        self.repository = repository

    def calculate(self, expression: str):
        # Безопасное вычисление математического выражения
        try:
            # Ограничиваем доступные для eval символы ради безопасности
            allowed_chars = "0123456789+-*/(). "
            if not all(char in allowed_chars for char in expression):
                raise ValueError("Недопустимые символы в выражении")

            result = float(eval(expression))
            calculation = self.repository.add(expression, result)
            return calculation
        except Exception as e:
            raise ValueError(f"Ошибка вычисления: {e}")

    def get_all(self):
        return [c.to_dict() for c in self.repository.get_all()]

    def get_by_id(self, calc_id: int):
        calc = self.repository.get(calc_id)
        if not calc:
            raise LookupError(f"Запись с id={calc_id} не найдена")
        return calc.to_dict()

    def delete(self, calc_id: int):
        calc = self.repository.delete(calc_id)
        if not calc:
            raise LookupError(f"Запись с id={calc_id} не найдена")
        return {"id": calc_id}