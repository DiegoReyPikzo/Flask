# Direcciones disponibles y direcciones especiales
IPS = ["192.168.1.10", "192.168.1.20", "192.168.1.30","192.168.1.40", "192.168.1.50"]

IP_BLOQUEADA = "192.168.1.20"
IP_REQUERIDA = "192.168.1.30"

# Diccionario anidado de dispositivos
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


# Función 1: validar la configuración de un dispositivo
def validar_politica(dispositivo):
    ip = dispositivo["ip"]
    politica = dispositivo["policy"]

    if ip not in IPS:
        return "Configuración inválida (IP incorrecta)"

    if politica == "ALLOW_ALL":
        return "Configuración válida"

    if politica == "BLOCK_IP":
        if ip == IP_BLOQUEADA:
            return "Configuración inválida (IP bloqueada)"
        return "Configuración válida"

    if politica == "REQUIRED_IP":
        if ip == IP_REQUERIDA:
            return "Configuración válida"
        return "Configuración inválida (IP incorrecta)"

    return "Configuración inválida (política desconocida)"


# Función 2: mostrar todos los dispositivos
def mostrar_dispositivos():
    for identificador, dispositivo in dispositivos.items():
        print("ID:", identificador)
        print("Nombre:", dispositivo["device_name"])
        print("IP:", dispositivo["ip"])
        print("Política:", dispositivo["policy"])
        print("Estado:", dispositivo["status"])
        print("Resultado:", validar_politica(dispositivo))
        print()


# Función 3: generar estadísticas de la red
def generar_resumen():
    activos = 0
    validas = 0

    for dispositivo in dispositivos.values():
        if dispositivo["status"] == "Activo":
            activos += 1

        if validar_politica(dispositivo) == "Configuración válida":
            validas += 1

    total = len(dispositivos)

    print("RESUMEN DE LA RED")
    print("Dispositivos activos:", activos)
    print("Dispositivos inactivos:", total - activos)
    print("Configuraciones válidas:", validas)
    print("Configuraciones inválidas:", total - validas)


# Ejecución del programa
mostrar_dispositivos()
generar_resumen()
