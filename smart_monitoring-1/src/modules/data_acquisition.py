from paho.mqtt import client as mqtt
import ssl
import json

class DataAcquisition:
    def __init__(self, broker, port, topic, username=None, password=None):
        self.broker = broker
        self.port = port
        self.topic = topic
        self.username = username
        self.password = password
        self.client = mqtt.Client()

        if username and password:
            self.client.username_pw_set(username, password)

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc):
        print(f"Connected to MQTT broker with result code {rc}")
        client.subscribe(self.topic)

    def on_message(self, client, userdata, msg):
        data = json.loads(msg.payload)
        self.process_data(data)

    def process_data(self, data):
        # Placeholder for processing incoming data
        print("Received data:", data)

    def start(self):
        self.client.tls_set(cert_reqs=ssl.CERT_REQUIRED)
        self.client.tls_insecure_set(False)
        self.client.connect(self.broker, self.port)
        self.client.loop_start()

    def stop(self):
        self.client.loop_stop()
        self.client.disconnect()