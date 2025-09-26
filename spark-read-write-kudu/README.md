# Spark Read-Write Apache Kudu
---

![Alt Text](https://github.com/MuhammadMukhlis220/Spark/blob/main/spark-read-write-kudu/pic/kudu.png)

Apache Kudu is storage engine, so we need SQL engine to access Kudu table. One of application that can access Kudu is Apache Spark. Fortunately, Apache Kudu provides an official integration library for Apache Spark, allowing Spark applications to directly read from and write to Kudu tables.

We can access the **Jar** from Maven if we use Spark 3 in [here](https://mvnrepository.com/artifact/org.apache.kudu/kudu-spark3). Choose by pairing your Kudu version. Mine is __1.17.0__ so you can download directly in [here](https://repo1.maven.org/maven2/org/apache/kudu/kudu-spark3_2.12/1.17.0/kudu-spark3_2.12-1.17.0.jar).

## Example Read Kudu:

- I am using Apache Zeppelin and using pyspark. For production, you can switch it by using Spark Submit.
- My Kudu is using Impala catalog as metadata so there are some different style to call the table name.

### 1. Build Spark Session and Read Kudu Jar

Use this `.config("spark.jars", "<your/path/to/kudu/jar>/kudu-spark3_2.12-1.17.0.jar")` to use your kudu jar.
```python
%python
spark = SparkSession.builder.appName("Spark Read Kudu")\
        .master("yarn")\
        .config("spark.executor.instances", "2") \
        .config("spark.executor.memory", "2g") \
        .config("spark.executor.cores", "2") \
        .config("spark.jars", "/usr/odp/0.2.0.0-04/zeppelin/spark-jar/kudu-spark3_2.12-1.17.0.jar") \ # Access our jar in here
        .getOrCreate()
```

### 2. Build Connection to Kudu

To access Kudu with Impala catalog, we need write `impala::` in front of schema and table name. If we have `default` schema and `big_data`, it will be: `impala::default.big_data`.
```python
kudu_master = "100.100.100.11:7051" # your kudu master IP or FQDN
kudu_table = "impala::default.big_data" # your schema and table name

df = spark.read \
  .format("kudu") \
  .option("kudu.master", kudu_master) \
  .option("kudu.table", kudu_table) \
  .load().limit(100)
```
Your data will stored in `df` variable as Spark Dataframe. Unfortunately, we can't perform SQL query in here. Since Spark using lazy execution, __we can build temporary table in spark to perform SQL query__.

### 3. Information Data and Make Temporary Table for SQL Query
```python
%python
df.printSchema()
```
![Alt Text](https://github.com/MuhammadMukhlis220/Spark/blob/main/spark-read-write-kudu/pic/code_1.png)

```python
%python
print(" Row:", df.count(),"\n","Column:", len(df.columns))
```
![Alt Text](https://github.com/MuhammadMukhlis220/Spark/blob/main/spark-read-write-kudu/pic/code_2.png)

```python
%python
df.createOrReplaceTempView("table_kudu")
spark.sql("SELECT * FROM table_kudu limit 2").show() # Query in here
```
![Alt Text](https://github.com/MuhammadMukhlis220/Spark/blob/main/spark-read-write-kudu/pic/code_3.png)

## Write to Kudu?

It's easy, we just change `read` and `load` to `write` and `save`like other native API from Spark. But we only can use `append` because `overwrite` is not supported.

```python
df = spark.sql("SELECT * FROM table_kudu limit 2")

kudu_master = "100.100.100.11:7051" # your kudu master IP or FQDN
kudu_table = "impala::default.big_data"

df_cast.write \
  .format("kudu") \
  .option("kudu.master", kudu_master) \
  .option("kudu.table", kudu_table) \
  .mode("append") \
  .save()
```

#### Limitation:
Spark supports reading from and writing to existing Kudu tables, **but cannot create new Kudu tables**. <br>
For table creation, use Impala, such as via the [impyla](https://pypi.org/project/impyla/0.9.0/) Python library.

__That all, give it a try!__