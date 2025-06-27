# ---------------- alert_service/app.py ----------------
from flask import Flask, request

app = Flask(_name_)

@app.route("/analizar", methods=["POST"])
def analizar():
    data = request.get_json()
    barrio = data["barrio"]
    temp = data["temperatura"]
    calidad = data["calidad_aire"]
    if temp > 35:
        print(f"[ALERTA] {barrio} - Temperatura crítica: {temp}°C")
    if calidad == "Mala":
        print(f"[ALERTA] {barrio} - Calidad de aire MALA")
    return "Analizado", 200

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5003)
