from flask import Flask, jsonify
import mysql.connector
from dotenv import load_dotenv
import os
import threading
import paho.mqtt.client as mqtt

# Carregando .env
load_dotenv()

# Setup da Aplicação Flask e do broker MQTT
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('secret_key')
con = mysql.connector.connect(
    host='localhost',
    user=os.getenv('user'),
    password=os.getenv('password'),
    database='teste'
)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttBroker = os.getenv('BROKER')

@app.route("/ajuda")
def main():
    cursor = con.cursor()
    cursor.execute("SELECT * FROM usuarios")
    dados = cursor.fetchall() 
    cursor.close()
    chaves = ['id', 'nome', 'senha']
    usuarios = [dict(zip(chaves, linha)) for linha in dados]
    return jsonify(usuarios)

def on_message(client, userdata, message):
    global my_temp
    my_temp = str(message.payload.decode("utf-8"))
    print("received message: " ,my_temp)

def worker():
    client.connect(mqttBroker)
    client.subscribe("focusCube")
    client.on_message=on_message
    client.loop_forever()

threading.Thread(target=worker).start()

if __name__ == "__main__":
    app.run()

