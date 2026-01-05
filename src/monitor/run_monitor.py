from src.monitor.config import MonitorConfig
from src.monitor.extract import load_data
from src.monitor.validate import run_ge_checks
from src.monitor.drift import run_evidently
from src.monitor.store import store_run

def main():
    cfg = MonitorConfig()

    ref = load_data(cfg.reference_path)
    cur = load_data(cfg.current_path)

    ge_res = run_ge_checks(cur)
    ev_res = run_evidently(ref, cur, cfg.report_html_path, cfg.metrics_json_path)

    store_run(
        ge_pass=ge_res["ge_pass"],
        ge_failed_count=ge_res["ge_failed_count"],
        report_saved=ev_res["report_saved"],
    )

    # Exit code for CI: fail if GE fails
    if not ge_res["ge_pass"]:
        raise SystemExit("Data quality checks failed (Great Expectations).")

if __name__ == "__main__":
    main()
