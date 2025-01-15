import paho.mqtt.client as mqtt


class MQTTSubscriber:
    def __init__(self, broker, port, topic):
        self.broker = broker
        self.port = port
        self.topic = topic
        self.client = mqtt.Client()

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect
        self.client.on_subscribe = self.on_subscribe
        self.client.on_unsubscribe = self.on_unsubscribe

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected successfully.")
            client.subscribe(self.topic)
        else:
            print(f"Failed to connect with result code {rc}")

    def on_disconnect(self):
        self.client.disconnect()
        print("Disconnected.")

    def on_subscribe(self, client, userdata, mid, granted_qos):
        print(f"Subscribed to {mid}")

    def on_unsubscribe(self, client, userdata, mid, granted_qos):
        print(f"Unsubscribed from {mid}")

    def on_message(self, client, userdata, msg):
        print(f"Received message '{msg.payload.decode()}' on topic '{msg.topic}'")

    def connect(self):
        self.client.connect(self.broker, self.port, 60)
        self.client.loop_forever()
