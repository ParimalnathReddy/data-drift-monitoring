import json
import os
from pathlib import Path

import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset, DataSummaryPreset


def _ensure_parent_dir(path: str) -> None:
    Path(os.path.dirname(path)).mkdir(parents=True, exist_ok=True)


def run_evidently(reference: pd.DataFrame, current: pd.DataFrame, html_path: str, json_path: str) -> dict:
    _ensure_parent_dir(html_path)
    _ensure_parent_dir(json_path)

    report = Report(metrics=[
        DataDriftPreset(),
        DataSummaryPreset(),
    ])

    snapshot = report.run(reference_data=reference, current_data=current)
    snapshot.save_html(html_path)

    # Export JSON snapshot for storage / API
    snapshot.save_json(json_path)

    return {
        "report_saved": True,
        "html_path": html_path,
        "json_path": json_path,
    }
