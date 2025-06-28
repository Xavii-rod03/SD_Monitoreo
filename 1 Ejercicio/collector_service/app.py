# ---------------- collector_service/app.py ----------------
from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/datos", methods=["POST"])
def recibir_datos():
    data = request.get_json()
    requests.post("http://storage_service:5002/guardar", json=data)
    requests.post("http://alert_service:5003/analizar", json=data)
    return "OK", 200

if __name__== "_main_":
    app.run(host="0.0.0.0", port=5001)