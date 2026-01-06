# Data Drift & Data Quality Monitoring System

## Overview
This project implements a production-style **data drift monitoring system** for machine learning pipelines. It continuously validates incoming data, detects distribution shifts, and exposes drift metrics and reports via an API.

**Why this matters:**
In real ML systems, models rarely fail because of bad code — they fail because data silently changes.
This system catches those failures before they impact downstream predictions, dashboards, or business decisions.

**What Problem This Solves:**

In production environments:
Training data ≠ live data
Schema changes go unnoticed
Feature distributions drift over time
Model performance degrades silently

**This project addresses those issues by:**

Enforcing data quality contracts
Detecting statistical drift
Persisting historical monitoring state
Making drift observable via APIs and reports

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
```text
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



```

##  Usage - How to run the system

This project runs as two Docker services:
- A monitoring job that computes data quality checks and data drift metrics
- A FastAPI service that serves reports and metrics via HTTP endpoints

### Prerequisites

Ensure the following are installed and running:

- Docker Desktop
- Docker Compose (included with Docker Desktop)

Verify Docker is running:
docker info


### Build Docker Images

Build all required images before running the services.

```bash
docker compose build
```


This step is required on first setup or after code or dependency changes.

### Start the API Service

Start the FastAPI service that serves drift reports and metrics.

```bash
docker compose up api
```


Once running, the service is available at:

http://localhost:8000/latest-report
 – View the latest drift report

http://localhost:8000/metrics
 – View drift metrics in JSON format

http://localhost:8000/health
 – API health check

Keep this service running while using the system.

### Run the Drift Monitoring Job

Execute the monitoring job to analyze data and generate reports.

```bash
docker compose run --rm monitor
``` 

This job performs the following steps:

Loads reference and current datasets

Runs data quality validation using Great Expectations

Computes data drift metrics using Evidently

Saves HTML reports and JSON metrics

After completion, refresh the /latest-report endpoint to view updated results.

### Typical Workflow
docker compose up api
docker compose run --rm monitor


The API service remains running, and the monitoring job is executed whenever new data arrives.

### Stop Services

To stop the running API service:

CTRL + C


To remove containers:

```bash
docker compose down
```

### Verify the System

Verify the system is working by calling the metrics endpoint:

```bash
curl http://localhost:8000/metrics
```
