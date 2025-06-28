# ---------------- storage_service/app.py ----------------
from flask import Flask, request, jsonify
from collections import defaultdict

app = Flask(__name__)

datos_por_barrio = defaultdict(list)

@app.route("/guardar", methods=["POST"])
def guardar():
    data = request.get_json()
    barrio = data["barrio"]
    datos_por_barrio[barrio].append(data)
    return "Guardado", 200

@app.route("/datos", methods=["GET"])
def consultar():
    barrio = request.args.get("barrio")
    return jsonify(datos_por_barrio.get(barrio, []))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)