# __Log Streaming (Kafka, Spark, and Opensearch) and Alerting__

![alt_text](pic/title-picture.jpg) 

__This example is running from WSL 2__<br>
Requirements running in your system:
1. WSL 2 (Windows 11)
2. Python 3.10
3. Kafka 3.5.1
4. Spark 3.5.1
5. Opensearch 2.19

__There will be 4 step to run this example__:
1. Kafka Configuration
2. Generate Log as Source
3. Spark Stream Read Kafka and Send to Opensearch
4. Opensearch Configuration for Alert


### 1. Kafka Configuration

Let's set up the Kafka by creating new topic called `sensor-data`. Topic is used to store log. To create topic, use:

~/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic sensor-data


### 2. Generate Log as Source

Since i dont have real log from IOT, you can configure your source log from anything (IOT MQTT, API, Metric, etc) and send to Kafka's topic. In here i'am using python to generate the logs.

