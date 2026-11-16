import requests

# 1. Conexión local al controlador
CONTROLLER_URL = "http://127.0.0.1:58000"

login_payload = {
    "username": "admin",
    "password": "Cisco123!"
}

# 2. Pedir el Ticket
resp_auth = requests.post(f"{CONTROLLER_URL}/api/v1/ticket", json=login_payload)
token = resp_auth.json()["response"]["serviceTicket"]

# 3. Consultar los dispositivos
headers = {"X-Auth-Token": token}
resp_devices = requests.get(f"{CONTROLLER_URL}/api/v1/network-device", headers=headers)
devices = resp_devices.json().get("response", [])

# 4. Mostrar el semáforo en consola
print("\n" + "="*45)
print("       ESTADO DE DISPOSITIVOS EN RED")
print("="*45)

for dev in devices:
    nombre = dev.get("hostname", "Desconocido")
    ip = dev.get("managementIpAddress", "Sin IP")
    estado = dev.get("reachabilityStatus", "Unknown")

    if estado == "Reachable":
        print(f" [OK]      {nombre:<10} | IP: {ip:<15} | Estado: OPERATIVO")
    else:
        print(f" [ALERTA]  {nombre:<10} | IP: {ip:<15} | Estado: CAÍDO")

print("="*45 + "\n")