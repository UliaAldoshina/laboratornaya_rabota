
# Factory: создание изданий

from models.entities import PrintedBook, EBook, Magazine


class ItemFactory:  # Фабрика изданий
    @staticmethod
    def create(item_type: str, title: str, author: str, **kwargs):
        item_type = item_type.lower()
        if item_type == "printed":
            return PrintedBook(id=0, title=title, author=author,
                               pages=kwargs.get("pages", 0),
                               item_type=None)
        if item_type == "ebook":
            return EBook(id=0, title=title, author=author,
                         file_size=kwargs.get("file_size", 0.0),
                         item_type=None)
        if item_type == "magazine":
            return Magazine(id=0, title=title, author=author,
                            issue_number=kwargs.get("issue_number", 0),
                            item_type=None)
        raise ValueError(f"Неизвестный тип издания: {item_type}")