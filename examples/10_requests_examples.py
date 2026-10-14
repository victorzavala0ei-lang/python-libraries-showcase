"""
Ejemplos de la librería 'requests' para peticiones HTTP en Python.

Requests es una librería elegante y sencilla para realizar peticiones HTTP
('HTTP for Humans'), facilitando interactuar con APIs RESTful.

Instalación:
    pip install requests
"""

import sys

try:
    import requests
    REQUESTS_INSTALADO = True
except ImportError:
    REQUESTS_INSTALADO = False


def demostracion_peticion_get():
    print("=" * 60)
    print("1. PETICIÓN HTTP GET (OBTENER RECURSOS Y PARÁMETROS)")
    print("=" * 60)
    
    url = "https://jsonplaceholder.typicode.com/posts"
    parametros = {"userId": 1}
    
    print(f"Enviando GET a: {url} con parámetros: {parametros}")
    try:
        respuesta = requests.get(url, params=parametros, timeout=5)
        print(f"Código de estado (Status Code): {respuesta.status_code}")
        print(f"Tipo de contenido (Content-Type): {respuesta.headers.get('content-type')}")
        
        datos = respuesta.json()
        print(f"Total de publicaciones recibidas: {len(datos)}")
        print("\nPrimera publicación obtenida:")
        primer_post = datos[0]
        print(f"  ID:     {primer_post['id']}")
        print(f"  Título: {primer_post['title']}")
        print(f"  Cuerpo: {primer_post['body'][:60]}...")
    except requests.exceptions.RequestException as e:
        print(f"[Aviso de red] No fue posible conectar con el servidor ({e}).")
        print("Demostración simulada en modo local:")
        print("  Status code esperado: 200 OK")
        print("  Respuesta JSON típica: [{'userId': 1, 'id': 1, 'title': 'ejemplo', 'body': 'texto'}]")
    print()

def demostracion_peticion_post():
    print("=" * 60)
    print("2. PETICIÓN HTTP POST (ENVIAR DATOS JSON)")
    print("=" * 60)
    
    url = "https://jsonplaceholder.typicode.com/posts"
    nuevo_post = {
        "title": "Aprender Python y Requests",
        "body": "Requests hace que consumir APIs sea sumamente intuitivo y limpio.",
        "userId": 42
    }
    cabeceras = {
        "Content-Type": "application/json; charset=UTF-8",
        "User-Agent": "PythonShowcase/1.0"
    }
    
    print(f"Enviando POST a: {url}")
    print(f"Payload JSON: {nuevo_post}")
    try:
        respuesta = requests.post(url, json=nuevo_post, headers=cabeceras, timeout=5)
        print(f"Código de estado: {respuesta.status_code} (201 = Created)")
        print(f"Respuesta del servidor:")
        print(respuesta.json())
    except requests.exceptions.RequestException as e:
        print(f"[Aviso de red] No fue posible conectar con el servidor ({e}).")
        print("Demostración simulada de POST exitoso:")
        print("  Status code esperado: 201 Created")
        print("  Respuesta devuelta: {'id': 101, 'title': '...', 'userId': 42}")
    print()

def demostracion_manejo_errores_y_status():
    print("=" * 60)
    print("3. MANEJO DE ERRORES Y TIMEOUTS (raise_for_status)")
    print("=" * 60)
    
    url_inexistente = "https://jsonplaceholder.typicode.com/recurso_inexistente_404"
    print(f"Consultando URL con error intencional: {url_inexistente}")
    
    try:
        respuesta = requests.get(url_inexistente, timeout=5)
        # raise_for_status() lanza una excepción HTTPError si el código es 4xx o 5xx
        respuesta.raise_for_status()
    except requests.exceptions.HTTPError as error_http:
        print(f" Captura de error HTTP esperado: {error_http}")
    except requests.exceptions.Timeout:
        print(" La petición excedió el tiempo límite (Timeout).")
    except requests.exceptions.RequestException as error_general:
        print(f" Error general de conexión: {error_general}")
    print()

def main():
    print("\n>>> DEMOSTRACIÓN DE LA LIBRERÍA 'requests' EN PYTHON <<<\n")
    if not REQUESTS_INSTALADO:
        print("[AVISO] La librería 'requests' no está instalada.")
        print("Para instalarla ejecuta: pip install requests\n")
        return
    demostracion_peticion_get()
    demostracion_peticion_post()
    demostracion_manejo_errores_y_status()
    print("¡Demostración de 'requests' completada con éxito!\n")

if __name__ == "__main__":
    main()
