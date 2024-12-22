import os
import time

# Constants
MILLISECONDS_TO_KEEP = 7 * 86400 * 1000 # 7 days

def delete_rotated_dag_processor_logs(log_base_path):
    """
    Delete rotated dag_processor_manager logs like:
    dag_processor_manager.log.1, dag_processor_manager.log.2, etc.
    """
    log_dir = os.path.join(log_base_path, "dag_processor_manager")
    if not os.path.isdir(log_dir):
        return

    for entry in os.listdir(log_dir):
        if entry.startswith("dag_processor_manager.log.") and entry[len("dag_processor_manager.log.") :].isdigit():
            rotated_log_path = os.path.join(log_dir, entry)
            print(f"Deleting rotated log: {rotated_log_path}")
            os.unlink(rotated_log_path)

def delete_old_logs_and_empty_dirs(log_base_path, age_threshold_ms):
    """
    Recursively delete:
    - Files older than `age_threshold_ms`
    - Folders that become empty (excluding dag_processor_manager)
    """
    now_ms = time.time() * 1000

    for root, dirs, files in os.walk(log_base_path, topdown=False):
        if "dag_processor_manager" in root:
            continue

        # Delete old files
        for file in files:
            file_path = os.path.join(root, file)
            try:
                mtime_ms = os.path.getmtime(file_path) * 1000
                if now_ms - mtime_ms > age_threshold_ms:
                    print(f"Deleting old log file: {file_path}")
                    os.unlink(file_path)
            except Exception as e:
                print(f"Error deleting file {file_path}: {e}")

        # Delete empty dirs
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

if __name__ == "__main__":
    cleanup_logs()
