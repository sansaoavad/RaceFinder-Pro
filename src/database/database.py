import sqlite3
from pathlib import Path


class Database:

    def __init__(self):
        self.conn = None

    def criar_banco(self, pasta_evento):

        banco = Path(pasta_evento) / "racefinder.db"

        self.conn = sqlite3.connect(banco)

        cursor = self.conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS fotos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                arquivo TEXT UNIQUE,
                numero TEXT,
                processada INTEGER DEFAULT 0
            )
        """)

        self.conn.commit()

    def inserir_foto(self, arquivo):

        cursor = self.conn.cursor()

        cursor.execute(
            """
            INSERT OR IGNORE INTO fotos (arquivo)
            VALUES (?)
            """,
            (str(arquivo),)
        )

        self.conn.commit()

    def total_fotos(self):

        cursor = self.conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM fotos")

        return cursor.fetchone()[0]