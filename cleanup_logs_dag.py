from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os
import time

# Constants
MILLISECONDS_TO_KEEP = 7 * 86400 * 1000  # 7 days

def delete_rotated_dag_processor_logs(log_base_path):
    log_dir = os.path.join(log_base_path, "dag_processor_manager")
    if not os.path.isdir(log_dir):
        return

    for entry in os.listdir(log_dir):
        if entry.startswith("dag_processor_manager.log.") and entry[len("dag_processor_manager.log.") :].isdigit():
            rotated_log_path = os.path.join(log_dir, entry)
            print(f"Deleting rotated log: {rotated_log_path}")
            os.unlink(rotated_log_path)

def delete_old_logs_and_empty_dirs(log_base_path, age_threshold_ms):
    now_ms = time.time() * 1000

    for root, dirs, files in os.walk(log_base_path, topdown=False):
        if "dag_processor_manager" in root:
            continue

        for file in files:
            file_path = os.path.join(root, file)
            try:
                mtime_ms = os.path.getmtime(file_path) * 1000
                if now_ms - mtime_ms > age_threshold_ms:
                    print(f"Deleting old log file: {file_path}")
                    os.unlink(file_path)
            except Exception as e:
                print(f"Error deleting file {file_path}: {e}")

        try:
            if not os.listdir(root):
                print(f"Removing empty directory: {root}")
                os.rmdir(root)
        except Exception as e:
            print(f"Error removing directory {root}: {e}")

def cleanup_logs():
    base_dir = os.environ.get("AIRFLOW_HOME")
    if not base_dir:
        raise EnvironmentError("AIRFLOW_HOME environment variable not set.")

    log_dir = os.path.join(base_dir, "logs")

    delete_rotated_dag_processor_logs(log_dir)
    delete_old_logs_and_empty_dirs(log_dir, age_threshold_ms=MILLISECONDS_TO_KEEP)


# Define DAG arguments
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2025, 5, 14),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    "email_on_failure": False,
    "email_on_retry": False,
}

# Define the DAG, e.g., runs daily at 3 AM
with DAG(
    dag_id="cleanup_logs_dag",
    default_args=default_args,
    schedule_interval="0 3 * * *",
    catchup=False,
    tags=["maintenance", "logs"],
) as dag:

    cleanup_task = PythonOperator(
        task_id="cleanup_airflow_logs",
        python_callable=cleanup_logs,
    )
