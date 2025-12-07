import paho.mqtt.client as mqtt
import json
import time
import random

# ----------------------------------------
# My details
# ----------------------------------------
student_name = "AMBEDKAR T M"
unique_id = "42110069"
topic = "home/ambedkar-2025/sensor"
# ----------------------------------------

broker = "192.168.56.1"   # Mosquitto broker IP
port = 1883

client = mqtt.Client()

client.connect(broker, port, 60)

while True:
    data = {
        "temperature": 25,
        "humidity": 60,
        "vibration": random.randint(1, 5),   # extra custom sensor
        "student_name": student_name,
        "unique_id": unique_id
    }

    payload = json.dumps(data)
    client.publish(topic, payload)
    print("Published :", payload)

    time.sleep(2)
