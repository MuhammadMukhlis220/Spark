import random
import time
import json
from datetime import datetime, timezone
from kafka import KafkaProducer

KAFKA_BOOTSTRAP_SERVERS = ['localhost:9092']
TOPIC_NAME = "sensor-data"

# Setup Producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

def generate_data():
    temperature = round(random.uniform(24.0, 85.0), 2)
    humidity = round(random.uniform(30.0, 90.0), 2)
    
    timestamp = datetime.now(timezone.utc).isoformat() #timezone setting
    
    return {
        "timestamp": timestamp,
        "temperature": temperature,
        "humidity": humidity
    }

print(f"Mulai mengirim data ke topik: {TOPIC_NAME} (Tekan Ctrl+C untuk berhenti)")

try:
    while True:
        data = generate_data()
        
        producer.send(TOPIC_NAME, value=data)
        
        print(f"Sent: {data}")
        
        time.sleep(1)
except KeyboardInterrupt:
    print("\nForced Stop.")
    producer.close()
