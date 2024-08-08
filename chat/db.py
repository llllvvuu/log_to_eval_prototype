import sqlite3
from datetime import datetime

FILENAME = "chat.sqlite"

conn: sqlite3.Connection | None = None


def save(obj: dict[str, str], table: str):
    global conn
    if conn is None:
        conn = sqlite3.connect("chat.sqlite")
    cursor = conn.cursor()
    cursor = cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table}
        (timestamp TEXT, {", ".join(f"{k} TEXT" for k in obj.keys())})
    """)
    _ = cursor.execute(
        f"""
        INSERT INTO {table} VALUES
        (?, {", ".join('?' for _ in obj.values())})
    """,
        (datetime.now().isoformat(),) + tuple(obj.values()),
    )
    conn.commit()


def get(keys: list[str], table: str) -> list[dict[str, str]]:
    global conn
    if conn is None:
        conn = sqlite3.connect("chat.sqlite")
    cursor = conn.cursor()
    select_fields = ", ".join(keys)
    query = f"SELECT timestamp, {select_fields} FROM {table}"
    _ = cursor.execute(query)
    rows: list[list[str]] = cursor.fetchall()
    result: list[dict[str, str]] = []
    for row in rows:
        row_dict = {"timestamp": row[0]}
        for i, key in enumerate(keys, start=1):
            row_dict[key] = row[i]
        result.append(row_dict)
    return result
