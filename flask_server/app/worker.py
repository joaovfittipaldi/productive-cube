import json
import threading
import paho.mqtt.client as mqtt

def start_worker(broker, topic):
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    mqttBroker = broker
    t1 = threading.Thread(target=worker, args=(client, mqttBroker, topic))
    t1.start()

def on_message(client, userdata, message):
    global my_temp
    mensagem = message.payload.decode("utf-8")
    payload = payload_format(mensagem_pre_formatacao=mensagem)

    print("received message: " , payload.get("AcX"))

def payload_format(mensagem_pre_formatacao) -> dict:
    payload_dict = {}
    caracteres_remover = ['"', '}', '{']
    novo_texto = ''.join(ch for ch in mensagem_pre_formatacao if ch not in caracteres_remover)
    values = novo_texto.split(",")
    for i in range(len(values)-1):
        key, value = values[i].split(":")
        payload_dict.update({key: value})

    return payload_dict

def worker(client, mqttBroker, topic: str):
    print("Conectado!")
    client.connect(mqttBroker)
    client.subscribe(topic)
    client.on_message=on_message
    client.loop_forever()
