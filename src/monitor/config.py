from pydantic import BaseModel

class MonitorConfig(BaseModel):
    # Drift thresholds
    dataset_drift_share: float = 0.3   # if >30% features drift -> dataset drift
    feature_drift_pvalue: float = 0.05

    # Data quality thresholds
    max_null_share: float = 0.02       # 2% nulls allowed for critical columns
    max_negative_fare_share: float = 0.001

    # Paths
    reference_path: str = "data/reference/yellow_ref.parquet"
    current_path: str = "data/current/yellow_cur.parquet"
    report_html_path: str = "reports/html/latest_report.html"
    metrics_json_path: str = "reports/json/latest_metrics.json"
