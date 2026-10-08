from datetime import date, timedelta


class NaiveLibrary:
    def __init__(self):
        self.books = []
        self.next_id = 1

    # Наивное создание объектов
    def add_item(self, item_type, title, author):
        if item_type == "printed":
            item = {"type": "printed", "title": title, "author": author,
                    "pages": 0, "status": "доступно"}
        elif item_type == "ebook":
            item = {"type": "ebook", "title": title, "author": author,
                    "size": 0.0, "status": "доступно"}
        elif item_type == "magazine":
            item = {"type": "magazine", "title": title, "author": author,
                    "issue": 0, "status": "доступно"}
        else:
            print("Неизвестный тип")
            return
        item["id"] = self.next_id
        self.next_id += 1
        self.books.append(item)

    # Наивный выбор срока через if/elif
    def issue(self, book_id, reader, reader_type="student"):
        book = self.find(book_id)
        if book is None:
            return
        if reader_type == "student":
            days = 14
        elif reader_type == "preferential":
            days = 30
        elif reader_type == "teacher":
            days = 60
        else:
            days = 7

        book["status"] = "выдано"
        book["reader"] = reader
        book["due_date"] = date.today() + timedelta(days=days)
        print(f"Выдано: {book['title']} -> {reader}, срок: {days} дней")

    # Наивные операции через if/elif
    def do_command(self, command, book_id, reader=None):
        if command == "issue":
            self.issue(book_id, reader)
        elif command == "return":
            book = self.find(book_id)
            if book:
                book["status"] = "доступно"
                book["reader"] = None
                print(f"Возвращено: {book['title']}")
        elif command == "reserve":
            book = self.find(book_id)
            if book:
                book["status"] = "забронировано"
                book["reader"] = reader
                print(f"Забронировано: {book['title']} для {reader}")

    def find(self, book_id):
        for b in self.books:
            if b["id"] == book_id:
                return b
        return None

    def show_all(self):
        for b in self.books:
            print(f"{b['id']}. {b['title']} ({b['type']}) - {b['status']}")


if __name__ == "__main__":
    lib = NaiveLibrary()
    lib.add_item("printed", "Война и мир", "Толстой")
    lib.add_item("ebook", "Python", "Петров")
    lib.issue(1, "Иванов", "teacher")
    lib.show_all()