
# Strategy: льготный срок (30 дней)

class PreferentialPeriodStrategy:
    def get_days(self) -> int:
        return 30

    def get_name(self) -> str:
        return "льготный срок (30 дней)"