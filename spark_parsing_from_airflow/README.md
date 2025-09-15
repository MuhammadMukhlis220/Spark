---
**This section contain how to parse argument or variable from airflow to spark (pyspark)**

Before we receive the argument from airflow, we need send the argument from airflow (so better look at [how to send argument from airflow to spark](https://github.com/MuhammadMukhlis220/Airflow/tree/main/parsing_argument_to_spark) first before execute this section).

```python
# This is python code for our PySpark

# start receive argument from airflow
import argparse

parser = argparse.ArgumentParser(description="Spark Application")
parser.add_argument("--tahun", required=True) #--tahun is variable we declare in Airflow SparkSubmitOperator's parameter, so we called it back in here
args = parser.parse_args()  # year from airflow already stored in args var in args.tahun

today_year = args.tahun
```
Congrats, our `today_year` in spark is same like `today_year` in airflow~
