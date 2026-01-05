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

![System Architecture](docs/images/architecture.png)




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

.
├── .github/                # CI/CD automation
├── data/                   # Raw and sampled datasets
├── reports/                # Generated HTML & JSON drift reports
├── src/
│   ├── api/                # FastAPI service layer
│   ├── database/           # SQLite persistence & metadata
│   ├── drift/              # Evidently drift detection logic
│   ├── extraction/         # Data sampling & ingestion
│   ├── quality/            # Great Expectations validation
│   └── main.py             # Pipeline orchestration
├── tests/                  # Unit and integration tests
├── Dockerfile
├── docker-compose.yml
└── requirements.txt



### Prerequisites
- Docker & Docker Compose
- Git

### Setup
```bash
git clone <your-repo-url>
cd data-drift-monitoring
docker compose build
