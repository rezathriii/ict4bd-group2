import paho.mqtt.client as mqtt


class MQTTPublisher:
    def __init__(self, broker, port, topic):
        self.broker = broker
        self.port = port
        self.topic = topic
        self.client = mqtt.Client()

        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_publish = self.on_publish

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected successfully.")
        else:
            print(f"Failed to connect with result code {rc}")

    def on_disconnect(self, client, userdata, rc):
        print("Disconnected.")

    def on_publish(self, client, userdata, mid):
        print(f"Message {mid} published.")

    def connect(self):
        self.client.connect(self.broker, self.port, 60)

    def publish(self, message):
        self.client.loop_start()
        result = self.client.publish(self.topic, message)
        result.wait_for_publish()
        self.client.loop_stop()
