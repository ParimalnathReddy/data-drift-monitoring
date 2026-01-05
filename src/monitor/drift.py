import json
import os
from pathlib import Path

import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset, DataSummaryPreset


def _ensure_parent_dir(path: str) -> None:
    '''
    Ensures the parent directory exists for a given path.
    '''
    Path(os.path.dirname(path)).mkdir(parents=True, exist_ok=True)


def run_evidently(reference: pd.DataFrame, current: pd.DataFrame, html_path: str, json_path: str) -> dict:
    '''
    Runs Evidently drift detection and saves the report and metrics.
    '''
    _ensure_parent_dir(json_path)
    # Create Evidently report
    report = Report(metrics=[
        DataDriftPreset(),
        DataSummaryPreset(),
    ])
    # Run Evidently report
    snapshot = report.run(reference_data=reference, current_data=current)
    # Save HTML report
    snapshot.save_html(html_path)
    # Save JSON snapshot for storage / API
    snapshot.save_json(json_path)

    return {
        "report_saved": True,
        "html_path": html_path,
        "json_path": json_path,
    }
