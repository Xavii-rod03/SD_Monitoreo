from flask import Flask
import requests
import json
import time
import random
import threading

app = Flask(__name__)

BARRIOS = ["Palermo", "Recoleta", "Belgrano", "Caballito"]
COLLECTOR_URL = "http://collector_service:5001/datos"

def generar_datos():
    while True:
        data = {
            "barrio": random.choice(BARRIOS),
            "temperatura": round(random.uniform(20, 40), 2),
            "humedad": round(random.uniform(30, 80), 2),
            "calidad_aire": random.choice(["Buena", "Moderada", "Mala"]),
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S")
        }
        try:
            requests.post(COLLECTOR_URL, json=data)
            print(f"Enviado: {data}")
        except Exception as e:
            print(f"Error al enviar datos: {e}")
        time.sleep(5)

@app.route("/")
def index():
    return "Sensor activo"

if __name__ == "__main__":
    threading.Thread(target=generar_datos).start()
    app.run(host="0.0.0.0", port=5000)

