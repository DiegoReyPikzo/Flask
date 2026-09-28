# Políticas de seguridad
ALLOW_ALL = "ALLOW_ALL"
BLOCK_IP = "BLOCK_IP"
REQUIRED_IP = "REQUIRED_IP"

# Estados posibles
ACTIVO = "Activo"
INACTIVO = "Inactivo"

# Lista de direcciones IP disponibles :D
direcciones_ip = [
    "192.168.1.10",
    "192.168.1.20",
    "192.168.1.30",
    "192.168.1.40",
    "192.168.1.50"
]

# Dirección que debe utilizar un dispositivo con REQUIRED_IP asi de q pro:D
IP_REQUERIDA = "192.168.1.30"

# Diccionario principal de dispositivos bien deidades
dispositivos = {
    "101": {
        "ip": direcciones_ip[0],
        "device_name": "Router Principal",
        "policy": ALLOW_ALL,
        "status": ACTIVO
    },
    "102": {
        "ip": direcciones_ip[1],
        "device_name": "Teléfono móvil",
        "policy": BLOCK_IP,
        "status": ACTIVO
    },
    "103": {
        "ip": direcciones_ip[2],
        "device_name": "Impresora",
        "policy": REQUIRED_IP,
        "status": INACTIVO
    },
    "104": {
        "ip": direcciones_ip[3],
        "device_name": "TV Inteligente",
        "policy": ALLOW_ALL,
        "status": ACTIVO
    },
    "105": {
        "ip": direcciones_ip[4],
        "device_name": "PC",
        "policy": BLOCK_IP,
        "status": INACTIVO
    }
}

# Función 1: mostrar todos los dispositivos (Imprimirlos pues xd)
def mostrar_dispositivos(diccionario_dispositivos):

    numero = 1

    for identificador, dispositivo in diccionario_dispositivos.items():

        resultado = validar_politica(dispositivo)

        print(numero, "- ID:", identificador)
        print("   Nombre:", dispositivo["device_name"])
        print("   IP:", dispositivo["ip"])
        print("   Política:", dispositivo["policy"])
        print("   Estado:", dispositivo["status"])
        print("   Resultado:", resultado)
        print()

        numero = numero + 1

#Función 2: validar la política de un dispositivo :/
def validar_politica(dispositivo):

    ip = dispositivo["ip"]
    politica = dispositivo["policy"]

    # Primero se comprueba que la IP esté disponible
    if ip not in direcciones_ip:
        return "Configuración inválida (IP incorrecta)"

    # ALLOW_ALL permite cualquier IP de la lista
    if politica == ALLOW_ALL:
        return "Configuración válida"

    # BLOCK_IP representa una dirección bloqueada
    elif politica == BLOCK_IP:
        return "Configuración inválida (IP bloqueada)"

    # REQUIRED_IP exige una IP determinada
    elif politica == REQUIRED_IP:

        if ip == IP_REQUERIDA:
            return "Configuración válida"
        else:
            return "Configuración inválida (IP incorrecta)"

    # Si la política no existe
    else:
        return "Configuración inválida (política desconocida)"

# Función 3: generar el resumen de la red
def generar_resumen(diccionario_dispositivos):

    dispositivos_activos = 0
    dispositivos_inactivos = 0
    configuraciones_validas = 0
    configuraciones_invalidas = 0

    for identificador, dispositivo in diccionario_dispositivos.items():

        # Contar estados
        if dispositivo["status"] == ACTIVO:
            dispositivos_activos = dispositivos_activos + 1

        elif dispositivo["status"] == INACTIVO:
            dispositivos_inactivos = dispositivos_inactivos + 1

        # Validar y contar configuraciones
        resultado = validar_politica(dispositivo)

        if resultado == "Configuración válida":
            configuraciones_validas = configuraciones_validas + 1
        else:
            configuraciones_invalidas = configuraciones_invalidas + 1

    print("RESUMEN DE LA RED")
    print("1. Dispositivos activos:", dispositivos_activos)
    print("2. Dispositivos inactivos:", dispositivos_inactivos)
    print("3. Configuraciones válidas:", configuraciones_validas)
    print("4. Configuraciones inválidas:", configuraciones_invalidas)

# Ejecución del programa
mostrar_dispositivos(dispositivos)
generar_resumen(dispositivos)