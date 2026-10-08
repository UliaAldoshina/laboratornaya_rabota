
# Strategy: стандартный срок (14 дней)

class StandardPeriodStrategy:
    def get_days(self) -> int:
        return 14

    def get_name(self) -> str:
        return "стандартный срок (14 дней)"