from __future__ import annotations

import sqlite3
from collections.abc import Iterator
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "postal.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS regions (
    code TEXT PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS offices (
    code        TEXT PRIMARY KEY,
    name        TEXT NOT NULL,
    region_code TEXT NOT NULL REFERENCES regions(code)
);

CREATE TABLE IF NOT EXISTS deliveries (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    origin_office TEXT NOT NULL REFERENCES offices(code),
    dest_office   TEXT NOT NULL REFERENCES offices(code),
    accepted_at   TEXT NOT NULL,
    delivered_at  TEXT,
    piece_count   INTEGER NOT NULL,
    weight_g      INTEGER NOT NULL,
    status        TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_deliveries_accepted ON deliveries(accepted_at);
CREATE INDEX IF NOT EXISTS idx_deliveries_origin ON deliveries(origin_office);
CREATE INDEX IF NOT EXISTS idx_deliveries_dest ON deliveries(dest_office);
"""


def connect(db_path: Path | str | None = None) -> sqlite3.Connection:
    path = Path(db_path) if db_path else DB_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(path, check_same_thread=False)
    connection.row_factory = sqlite3.Row
    return connection


def init_schema(connection: sqlite3.Connection) -> None:
    connection.executescript(SCHEMA)
    connection.commit()


def get_db() -> Iterator[sqlite3.Connection]:
    connection = connect()
    try:
        yield connection
    finally:
        connection.close()
