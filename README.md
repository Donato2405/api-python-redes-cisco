# Entorno de virtualización Python

# Pasos de instalación en Linux:

## 1. Clonación del proyecto

Desde la terminal ejecutar:

**git clone** <URL_del_repositorio> <nombre_de_la_carpeta_de_destino>

Luego ejecutar **cd** <nombre_de_la_carpeta_de_destino>. Esta carpeta será la raíz de nuestro proyecto en Python.

## 2. Creación del entorno virtual

Supongamos que el nombre que le damos al entorno virtual es **cisco**, entonces se creará una carpeta **cisco** con todas las librerías y dependencias necesarias paea nuestro proyecto. 

La manera de realizarlo es la siguiente:

# python3 -m venv <nombre_del_entorno>
Ejemplo: python3 -m venv cisco

Para activar el entorno escribimos **source cisco/bin/activate**, en la carpeta raíz del proyecto. El nombre del entorno virtual aparecerá entre paréntesis ().

## 3. Instalación de las dependencias, en este caso las librerías requests y tabulate

En la carpeta raíz de nuestro proyecto y dentro del entorno virtual escribimos: **pip install -r requirements.txt**

## 4. Selección del intérprete Python para nuestro entorno virtual

<img width="881" height="118" alt="image" src="https://github.com/user-attachments/assets/18c41d8e-d338-48b6-953c-b2499c57319f" />

<img width="736" height="412" alt="image" src="https://github.com/user-attachments/assets/2a795fcd-2cf8-47ef-a5a6-d21e09ce967f" />

Tal como se ve en la figura seleccionamos Python 3.10.12 (cisco) que se mostrará como entorno recomendado.

## 5. Desactivación del entorno virtual

Simplemente escribimos en la línea de comandos: **deactivate**



## Antes de ejecutar los scripts

- **Credenciales del controlador:** los scripts usan el usuario `cisco` y la clave `cisco123!`. Si en tu Network Controller creaste otro usuario, cambialos en `01_get-ticket.py` y en `04_tabulate.py`.
- **Ticket (X-Auth-Token):** `02_get-network-device.py` y `03_get-host.py` traen escrito un ticket de ejemplo que **no va a funcionar** en tu Packet Tracer, porque el controlador genera uno nuevo en cada sesión y vence. Ejecutá primero `01_get-ticket.py`, copiá el ticket que muestra y reemplazalo en el header `X-Auth-Token` de esos dos scripts. `04_tabulate.py` no necesita este paso: pide el ticket solo.


# TP4 Integrador — Redes de Computadoras

**Universidad Nacional de La Matanza (UNLaM)**  
**Materia:** Redes de Computadoras (3643)  
**Año:** 2026 — Segundo cuatrimestre

## Descripción del proyecto

Este repositorio contiene los scripts de Python utilizados en el Trabajo Práctico N.º 4 Integrador de Redes de Computadoras.

Los programas interactúan con la API REST del Network Controller de Cisco Packet Tracer para realizar consultas, obtener información de los dispositivos y supervisar su estado.

## Descripción de los scripts

### 1. 01_get-ticket.py — Autenticación

Realiza una petición POST a la API REST del Network Controller para autenticar un usuario y obtener un `serviceTicket`, necesario para autorizar las siguientes solicitudes.

### 2. 02_get-network-device.py — Consulta de dispositivos

Realiza una petición GET al controlador para obtener información de los dispositivos de red. Muestra sus nombres, modelos y direcciones IP de administración.

### 3. 03_get-host.py — Consulta de hosts

Consulta los hosts registrados en el Network Controller mediante una petición GET. Muestra el nombre, la dirección IP, la dirección MAC y la interfaz de conexión de cada host.

### 4. 04_tabulate.py — Inventario en tablas

Obtiene un ticket de autenticación y consulta los dispositivos de red y los hosts registrados. Utiliza la biblioteca `tabulate` para organizar y presentar los resultados en tablas.

### 5. 5-ScriptPropio-Semaforo.py — Monitoreo de dispositivos

Script desarrollado por el grupo que consulta el estado de accesibilidad de los dispositivos mediante la API REST del Network Controller.

Implementa un sistema de indicadores que clasifica los dispositivos como operativos (`OK`) o en alerta (`ALERTA`), mostrando sus nombres y direcciones IP.

Su objetivo es facilitar la identificación de dispositivos que podrían presentar problemas de conectividad.
