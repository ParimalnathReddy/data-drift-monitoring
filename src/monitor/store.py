from sqlalchemy import create_engine, text
from datetime import datetime

ENGINE = create_engine("sqlite:///monitoring.db", future=True)

def init_db():
    with ENGINE.begin() as conn:
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS runs (
            run_ts TEXT PRIMARY KEY,
            ge_pass INTEGER,
            ge_failed_count INTEGER,
            report_saved INTEGER
        )
        """))

def store_run(ge_pass: bool, ge_failed_count: int, report_saved: bool):
    init_db()
    with ENGINE.begin() as conn:
        conn.execute(
            text("INSERT INTO runs (run_ts, ge_pass, ge_failed_count, report_saved) VALUES (:ts,:gp,:gfc,:rs)"),
            {"ts": datetime.utcnow().isoformat(), "gp": int(ge_pass), "gfc": ge_failed_count, "rs": int(report_saved)}
        )
