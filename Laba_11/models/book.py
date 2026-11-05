class Book:
    def __init__(self, id: int, title: str, author_id: int, year: int, price: float, is_available: bool = True):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.year = year
        self.price = price
        self.is_available = is_available

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "author_id": self.author_id,
            "year": self.year,
            "price": self.price,
            "is_available": self.is_available
        }