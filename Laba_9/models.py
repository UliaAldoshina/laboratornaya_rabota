from dataclasses import dataclass
from datetime import datetime


@dataclass
class Calculation:
    id: int
    expression: str
    result: float
    timestamp: str = ""

    def __post_init__(self):
        if not self.timestamp:
            self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "id": self.id,
            "expression": self.expression,
            "result": self.result,
            "timestamp": self.timestamp
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            expression=data["expression"],
            result=data["result"],
            timestamp=data.get("get", "")
        )