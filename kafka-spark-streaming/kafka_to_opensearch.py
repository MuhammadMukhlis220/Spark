from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, DoubleType


# Config
kafka_bootstrap = "localhost:9092"
topic_name = "sensor-data"

spark = SparkSession.builder \
    .appName("test-kafka-opensearch") \
    .master("local[2]") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

spark.sparkContext.setLogLevel("ERROR")

schema = StructType([
    StructField("timestamp", StringType(), True),
    StructField("temperature", DoubleType(), True),
    StructField("humidity", DoubleType(), True)
])

kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_bootstrap) \
    .option("subscribe", topic_name) \
    .option("startingOffsets", "latest") \
    .load()

df = kafka_df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

def send_partition_to_opensearch(iterator):
    from opensearchpy import OpenSearch, helpers
    
    client = OpenSearch(
        hosts=[{'host': '172.28.176.140', 'port': 9200}],
        http_compress=True,
        use_ssl=False
    )
    
    actions = []
    for row in iterator:
        doc = row.asDict()
        action = {
            "_index": "sensor_logs",
            "_source": doc
        }
        actions.append(action)
        
        if len(actions) >= 500:
            helpers.bulk(client, actions)
            actions = []
            
    if actions:
        helpers.bulk(client, actions)

def process_batch(batch_df, batch_id):
    batch_df.foreachPartition(send_partition_to_opensearch)

print("Streaming starting...")
query = df.writeStream \
    .foreachBatch(process_batch) \
    .option("checkpointLocation", "/tmp/checkpoint_spark_stream") \
    .queryName("kafka-sensor-v1") \
    .start()

query.awaitTermination()
