import threading
import paho.mqtt.client as mqtt

def start_worker(broker):
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    mqttBroker = broker
    t1 = threading.Thread(target=worker, args=(client, mqttBroker, "pipoca doce"))
    t1.start()
    return t1

def on_message(client, userdata, message):
    global my_temp
    my_temp = str(message.payload.decode("utf-8"))
    print("received message: " ,my_temp)

def worker(client, mqttBroker, topic: str):
    client.connect(mqttBroker)
    client.subscribe(topic)
    client.on_message=on_message
    client.loop_forever()
