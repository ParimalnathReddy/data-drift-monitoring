from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
import sqlite3

app = FastAPI()

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/latest-report")
def latest_report():
    return FileResponse("reports/html/latest_report.html")

@app.get("/metrics")
def metrics(limit: int = 30):
    con = sqlite3.connect("monitoring.db")
    cur = con.cursor()
    cur.execute("SELECT run_ts, ge_pass, ge_failed_count, report_saved FROM runs ORDER BY run_ts DESC LIMIT ?", (limit,))
    rows = cur.fetchall()
    con.close()
    return [{"run_ts": r[0], "ge_pass": r[1], "ge_failed_count": r[2], "report_saved": r[3]} for r in rows]



#http://127.0.0.1:8000/latest-report