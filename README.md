# Data Drift & Data Quality Monitoring System

## Overview
This project implements a production-style **data drift and data quality monitoring system** for machine learning pipelines.  
It compares incoming (current) data against a trusted reference dataset to detect schema issues, data quality failures, and statistical drift before downstream models are impacted.

The system is designed to mirror real-world **enterprise ML monitoring**, emphasizing automation, auditability, and reproducibility.

---

## Features
- **Data Quality Validation**
  - Schema, type, range, and null checks using Great Expectations
- **Data Drift Detection**
  - Statistical comparison of reference vs current datasets using Evidently
  - Feature-level and dataset-level drift indicators
- **Automated Reporting**
  - Generates HTML drift reports and JSON metrics
- **REST API Access**
  - Serve reports and metrics via FastAPI
- **Automation & Auditability**
  - Daily scheduled runs via GitHub Actions
  - Versioned report artifacts for governance and review
- **Containerized Execution**
  - Fully reproducible Docker-based setup

---

## Architecture / Workflow

![System Architecture](assets/Arcitecture%20Image%20Jan%205,%202026,%2003_12_00%20PM.png)





---

## Tech Stack
- **Language:** Python 3.11
- **Data Validation:** Great Expectations
- **Drift Detection:** Evidently
- **API:** FastAPI, Uvicorn
- **Persistence:** SQLite
- **Containerization:** Docker, Docker Compose
- **Automation:** GitHub Actions
- **Dataset:** NYC Taxi (TLC) public data

---

## Project Structure

data-drift-monitoring/
├── src/
│   ├── monitor/        # Data extraction, validation, drift detection
│   ├── app/            # FastAPI application
│   └── utils/          # Shared utilities
├── great_expectations/ # Data quality expectations
├── reports/
│   ├── html/           # Drift reports
│   └── json/           # Metrics snapshots
├── data/
│   ├── reference/      # Baseline dataset
│   └── current/        # Incoming dataset
├── .github/workflows/
│   └── daily_monitor.yml
├── Dockerfile
├── docker-compose.yml
└── README.md



### Prerequisites
- Docker & Docker Compose
- Git

### Setup
```bash
git clone <your-repo-url>
cd data-drift-monitoring
docker compose build
