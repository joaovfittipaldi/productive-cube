import json
import threading
from app import timer
from datetime import datetime
import paho.mqtt.client as mqtt

temporizador = None  # criado APENAS AQUI

def start_worker(broker, topic):
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    mqttBroker = broker
    t1 = threading.Thread(target=worker, args=(client, mqttBroker, topic))
    t1.start()

def on_message(client, userdata, message):
    global temporizador
        
    mensagem = message.payload.decode("utf-8")
    payload = payload_format(mensagem=mensagem)

    print(f"Mensagem: {mensagem} \n Payload: {payload}")

    if payload.get('interrupcao'):
        timer.stop_event.set()
        return

    if temporizador is not None and temporizador.is_alive():
        timer.stop_event.set() 
        temporizador.join() 

    if temporizador is None or not temporizador.is_alive():
        horario = datetime.now().strftime("%H:%M:%S")
        data_atual = datetime.now().strftime("%Y-%m-%d")
        dia_semana = datetime.now().strftime("%A")
        temporizador = threading.Thread(
        target=timer.timer, 
        args=(payload.get('modo'), horario, dia_semana, data_atual ))
        temporizador.daemon = True

        temporizador.start()

def payload_format(mensagem: str) -> dict:
    if mensagem.lower() == "parado":
        return {"interrupcao": True}

    mensagem = mensagem.lower()
    mensagem = mensagem.strip()

    if mensagem.startswith("foco:"):
        try:
            valor = int(mensagem.split(":")[1].strip())
            return {"modo": valor}
        except ValueError:
            return {"erro": "Valor numérico inválido para Modo"}
    return {"erro": "Formato de mensagem desconhecido"}


def worker(client, mqttBroker, topic: str):
        client.connect(mqttBroker)
        client.subscribe(topic)
        client.on_message = on_message
        client.loop_forever()
