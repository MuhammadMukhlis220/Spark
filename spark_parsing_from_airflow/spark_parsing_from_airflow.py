from pyspark.sql import SparkSession
from datetime import datetime
import sys
import argparse

# start receive argument from airflow
parser = argparse.ArgumentParser(description = "Spark Application")
parser.add_argument("--tahun", required = True)
args = parser.parse_args() # year from airflow already stored in args var in args.tahun

today_year = args.tahun

spark = SparkSession.builder \
    .appName("dagri_spark_apbdgeser_last") \
    .config("spark.driver.memory", "8g") \
    .config("spark.executor.instances", "5") \
    .config("spark.executor.memory", "12g") \
    .config("spark.executor.cores", "10") \
    .getOrCreate()

data_dir = f"hdfs://mydir/{today_year}"

try:
    a = spark.read.option("recursiveFileLookup", "true").orc(data_dir) # read orc file from data_dir
    a.createOrReplaceTempView("myOrcTable") # create table (myOrcTable) for SQL from orc file we just read

    df = spark.sql(f"""
    SELECT * FROM myOrcTable WHERE year = {today_year} LIMIT 1
    """)

    output_path = f"hdfs://mydir/{today_year}/write.orc"
    output_path = f"{data_dir}/write.orc"

    df.write.mode("overwrite").orc(output_path) # write orc file from SQL result

except Exception as e:
    print(f"""
<><><><><><><><><><><><><><>><><><><><><><><><><><><><><><>
Error reading from {data_dir}: {str(e)}
File in directory not found or cannot be read
Skipping all tasks in the program
<><><><><><><><><><><><><><>><><><><><><><><><><><><><><><>
""")
    sys.exit(0)

spark.stop