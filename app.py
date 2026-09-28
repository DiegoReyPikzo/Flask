from flask import Flask, jsonify
import json

import json

with open("API.json", "r") as json_api:
    datos_json = json.load(json_api)

app = Flask(__name__)

# Diccionario compartido por todas las funciones
IPS = ["192.168.1.10", "192.168.1.20", "192.168.1.30", "192.168.1.40", "192.168.1.50"]

dispositivos = {
    "101": {
        "ip": IPS[0],
        "device_name": "Router Principal",
        "policy": "ALLOW_ALL",
        "status": "Activo"
    },
    "102": {
        "ip": IPS[1],
        "device_name": "Teléfono móvil",
        "policy": "BLOCK_IP",
        "status": "Activo"
    },
    "103": {
        "ip": IPS[2],
        "device_name": "Impresora",
        "policy": "REQUIRED_IP",
        "status": "Inactivo"
    },
    "104": {
        "ip": IPS[3],
        "device_name": "TV Inteligente",
        "policy": "ALLOW_ALL",
        "status": "Activo"
    },
    "105": {
        "ip": IPS[4],
        "device_name": "Computadora",
        "policy": "REQUIRED_IP",
        "status": "Inactivo"
    }
}

# Endpoint HTML (independiente, con su propio decorador)
@app.route('/')
def inicio():
    return """
    <html>
    <body>
    <h1>Hola mundo </h1>
    <a href="http://127.0.0.1:5000/api/saludo">Buscar datos </a>
    </body>
    </html>
    """

#  HTML (el del endpoint pues (version json) jaja)
@app.route('/json/<mac>')
def jason_data(mac):
    print(datos_json[mac]["Name"])
    print(datos_json[mac]["Protocolos"])
    print(datos_json[mac]["VLANs"])
    print(datos_json[mac]["Status"])
    return datos_json[mac]["Name"]
    """
    <html>
    <body>
    <h1>Hola mundo </h1>
    <a href="http://127.0.0.1:5000/api/saludo">Buscar datos </a>
    </body>
    </html>

    """


# Endpoint JSON original (diccionario completo)
@app.route('/api/saludo')
def saludo():
    return jsonify(dispositivos)


# ---------- 5 funciones que muestran datos REALES (uno por dispositivo) ----------

@app.route('/api/dispositivo/101')
def obtener_router():
    return jsonify(dispositivos["101"])


@app.route('/api/dispositivo/102')
def obtener_telefono():
    return jsonify(dispositivos["102"])


@app.route('/api/dispositivo/103')
def obtener_impresora():
    return jsonify(dispositivos["103"])


@app.route('/api/dispositivo/104')
def obtener_tv():
    return jsonify(dispositivos["104"])


@app.route('/api/dispositivo/105')
def obtener_computadora():
    return jsonify(dispositivos["105"])


# ---------- 5 funciones con datos INVENTADOS ----------

@app.route('/api/dispositivo/106')
def obtener_camara():
    dispositivo_inventado = {
        "ip": "192.168.1.60",
        "device_name": "Cámara de seguridad",
        "policy": "BLOCK_IP",
        "status": "Activo"
    }
    return jsonify(dispositivo_inventado)


@app.route('/api/dispositivo/107')
def obtener_consola():
    dispositivo_inventado = {
        "ip": "192.168.1.70",
        "device_name": "Consola de videojuegos",
        "policy": "ALLOW_ALL",
        "status": "Activo"
    }
    return jsonify(dispositivo_inventado)


@app.route('/api/dispositivo/108')
def obtener_laptop():
    dispositivo_inventado = {
        "ip": "192.168.1.80",
        "device_name": "Laptop de trabajo",
        "policy": "REQUIRED_IP",
        "status": "Inactivo"
    }
    return jsonify(dispositivo_inventado)


@app.route('/api/dispositivo/109')
def obtener_termostato():
    dispositivo_inventado = {
        "ip": "192.168.1.90",
        "device_name": "Termostato inteligente",
        "policy": "BLOCK_IP",
        "status": "Inactivo"
    }
    return jsonify(dispositivo_inventado)


@app.route('/api/dispositivo/110')
def obtener_altavoz():
    dispositivo_inventado = {
        "ip": "192.168.1.100",
        "device_name": "Altavoz inteligente",
        "policy": "ALLOW_ALL",
        "status": "Activo"
    }
    return jsonify(dispositivo_inventado)

def diccionarios ():
    return jsonify(dispositivos)
if __name__ == '__main__':
    app.run(debug=True)
