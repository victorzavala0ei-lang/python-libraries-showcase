"""
Librería: requests
Descripción: Consultar información desde una API pública por internet.
"""
try:
    import requests
except ImportError:
    print("[Error] La librería 'requests' no está instalada. Ejecuta: pip install requests")
    exit()

print("=== EJEMPLO INTERACTIVO: REQUESTS ===")

# Pedir ID al usuario
user_id = input("Ingresa un número de usuario del 1 al 10 para consultar sus datos: ").strip() or "1"
url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

print(f"\nConsultando: {url} ...")

try:
    respuesta = requests.get(url, timeout=5)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        print("\n--- Datos recibidos del servidor ---")
        print(f"Nombre:   {datos.get('name')}")
        print(f"Usuario:  {datos.get('username')}")
        print(f"Email:    {datos.get('email')}")
        print(f"Ciudad:   {datos.get('address', {}).get('city')}")
        print(f"Empresa:  {datos.get('company', {}).get('name')}")
    else:
        print(f"No se encontró el usuario. Código de respuesta: {respuesta.status_code}")
except Exception as e:
    print(f"No se pudo conectar a la API ({e}). Verifica tu conexión a internet.")
