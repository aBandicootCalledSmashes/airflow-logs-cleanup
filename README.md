# Airflow Logs Cleanup

This repository provides scripts and an Airflow DAG to automatically clean up old Airflow log files, helping you save disk space and keep your environment tidy.

## Features

- **Deletes rotated `dag_processor_manager` logs** (e.g., `dag_processor_manager.log.1`, `.2`, etc.)
- **Removes log files older than 7 days** (configurable)
- **Cleans up empty directories** left after log deletion
- **Can be run as a standalone script or as an Airflow DAG**

## Usage

### 1. Standalone Script

You can run `cleanup_logs.py` directly to clean up logs:

```bash
python cleanup_logs.py
```

**Requirements:**
- The `AIRFLOW_HOME` environment variable must be set to your Airflow home directory.

### 2. Airflow DAG

The `cleanup_logs_dag.py` file defines a DAG that runs the cleanup task daily at 3 AM.

**To use:**
1. Copy `cleanup_logs_dag.py` to your Airflow DAGs folder.
2. Ensure the `AIRFLOW_HOME` environment variable is set for your Airflow environment.
3. The DAG will appear in the Airflow UI as `cleanup_logs_dag`.

## Configuration

- **Retention Period:** By default, logs older than 7 days are deleted. You can change this by modifying the `MILLISECONDS_TO_KEEP` constant in the scripts.