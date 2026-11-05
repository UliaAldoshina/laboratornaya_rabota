from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class Book:
    id: int
    title: str
    author: str
    year: int
    genre: str
    price: float
    is_available: bool = True

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Book":
        return cls(
            id=data.get("id", 0),
            title=data["title"],
            author=data["author"],
            year=int(data["year"]),
            genre=data["genre"],
            price=float(data["price"]),
            is_available=bool(data.get("is_available", True))
        )