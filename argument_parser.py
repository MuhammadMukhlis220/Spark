# airflow:

today_year = 2025
today_month = 9

t1 = SparkSubmitOperator(
    task_id='spark_write_orc_file',
    application="/usr/odp/0.2.0.0-04/airflow/spark-job/sparksubmit.py",
    name='spark_job_task',
    dag=dag,
    application_args=[
        '--tahun', str(today_year),
        '--bulan', str(today_month)
    ],
    yarn_queue="default"
)


# spark:

import argparse

parser = argparse.ArgumentParser(description='Spark Application')
parser.add_argument('--tahun', required=True)
parser.add_argument('--bulan', required=True)
args = parser.parse_args()

tahun = args.tahun
bulan = args.bulan

print(f"Tahun: {tahun}, Bulan: {bulan}")
