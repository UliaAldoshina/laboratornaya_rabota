import sqlite3
from typing import List, Optional, Dict, Any

class BookRepository:
    def __init__(self, db_path: str = "database.db"):
        self.db_path = db_path

    def _get_connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def get_all(self) -> List[Dict[str, Any]]:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT b.id, b.title, a.name as author, b.year, b.price, b.is_available 
                FROM books b
                JOIN authors a ON b.author_id = a.id
            """)
            return [dict(row) for row in cursor.fetchall()]

    def get_by_id(self, book_id: int) -> Optional[Dict[str, Any]]:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT b.id, b.title, a.name as author, b.year, b.price, b.is_available 
                FROM books b
                JOIN authors a ON b.author_id = a.id
                WHERE b.id = ?
            """, (book_id,))
            row = cursor.fetchone()
            return dict(row) if row else None

    def create(self, title: str, author_id: int, year: int, price: float) -> int:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO books (title, author_id, year, price, is_available)
                VALUES (?, ?, ?, ?, 1)
            """, (title, author_id, year, price))
            conn.commit()
            return cursor.lastrowid

    def update(self, book_id: int, title: str, year: int, price: float, is_available: bool) -> bool:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE books 
                SET title = ?, year = ?, price = ?, is_available = ?
                WHERE id = ?
            """, (title, year, price, is_available, book_id))
            conn.commit()
            return cursor.rowcount > 0

    def delete(self, book_id: int) -> bool:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
            conn.commit()
            return cursor.rowcount > 0