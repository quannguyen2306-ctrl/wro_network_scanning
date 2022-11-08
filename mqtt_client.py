import paho.mqtt.client as mqtt
import time 
import json

class Mqtt:
    def __init__(self, initialized_topic):
        self.received_message = 0
        self.main_topic = initialized_topic
        self.mqtt_server = "test.mosquitto.org"
        self.port = 1883
        self.client = mqtt.Client()
    def on_connect(self,client, userdata, flags, rc):
        print("Connected with data code "+str(rc))
        print("Standby")
        client.subscribe(self.main_topic)

    def on_message(self,client, userdata, msg):
        self.received_message = msg.payload.decode()
        self.client.disconnect()

    def awaiting_message(self):
        self.client = mqtt.Client()
        self.client.connect(self.mqtt_server,self.port)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.loop_forever()
        self.client.disconnect()
    def publish_message(self,message):
        self.client = mqtt.Client()
        self.client.connect(self.mqtt_server,self.port)
        self.client.publish(self.main_topic, message)
        self.client.disconnect() 

    def send_message(self, data):
        self.publish_message(data)
        self.awaiting_message()
        if received_message == "Done":
            print("Send prescription data successfully")
        time.sleep(2)

    def get_message(self):
        self.awaiting_message()
        return self.recievd_message


network = Mqtt("topic/network")
while True:
    wait = network.awaiting_message()
    if wait == "asking":
        data = 
        network.send_message()



