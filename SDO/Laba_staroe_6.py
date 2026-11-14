import sqlite3

# Создание тестовой базы данных
conn = sqlite3.connect("library.db")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS books")
cur.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, genre TEXT, author TEXT)")
books = [
    (1, "Роман", "Толстой"),
    (2, "Роман", "Достоевский"),
    (3, "Поэзия", "Пушкин"),
    (4, "Роман", "Пушкин"),
    (5, "Поэзия", "Лермонтов"),
    (6, "Фантастика", "Беляев"),
]
cur.executemany("INSERT INTO books VALUES (?, ?, ?)", books)
conn.commit()
conn.close()


def analyze_table(table_name):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()

    # Получаем список полей таблицы
    cur.execute(f"PRAGMA table_info({table_name})")
    columns = [row[1] for row in cur.fetchall() if row[1] != "id"]

    for column in columns:
        # Количество одинаковых значений в поле
        cur.execute(f"SELECT {column}, COUNT(*) FROM {table_name} GROUP BY {column}")
        counts = cur.fetchall()
        print(f"Поле '{column}' — количество одинаковых значений:")
        for value, count in counts:
            print(f"  {value}: {count}")

        # Наиболее часто повторяющееся значение
        cur.execute(
            f"SELECT {column}, COUNT(*) FROM {table_name} "
            f"GROUP BY {column} ORDER BY COUNT(*) DESC LIMIT 1"
        )
        most_common = cur.fetchone()
        print(f"Наиболее частое значение в поле '{column}': {most_common[0]} (повторений: {most_common[1]})")
        print()

    conn.close()


analyze_table("books")