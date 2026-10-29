import json
import random
import time
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("Enviando datos de sensores a Kafka...")

try:
    while True:
        for i in range(1, 11):
            data = {
                "sensor_id": f"sensor_{i}",
                "temperatura": round(random.uniform(15.0, 35.0), 2),
                "humedad": round(random.uniform(40.0, 80.0), 2)
            }
            producer.send('sensores', value=data)
            print(f"Enviado: {data}")
        time.sleep(2)
except KeyboardInterrupt:
    print("\nProductor detenido.")
