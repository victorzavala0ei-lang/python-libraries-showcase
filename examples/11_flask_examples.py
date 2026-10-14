"""
Librería: Flask
Descripción: Crear una aplicación web sencilla y responder peticiones.
"""
try:
    from flask import Flask, jsonify
except ImportError:
    print("[Error] La librería 'Flask' no está instalada. Ejecuta: pip install Flask")
    exit()

print("=== EJEMPLO INTERACTIVO: FLASK ===")

# Pedir datos al usuario
nombre = input("Ingresa tu nombre para personalizar la API: ").strip() or "Estudiante"
mensaje = input("Ingresa un mensaje de bienvenida: ").strip() or "Bienvenido a mi primera aplicación web con Flask"

app = Flask(__name__)

@app.route("/")
def inicio():
    return f"<h1>Hola {nombre}!</h1><p>{mensaje}</p><p>Visita <a href='/api'>/api</a> para ver la respuesta JSON.</p>"

@app.route("/api")
def api():
    return jsonify({
        "usuario": nombre,
        "mensaje": mensaje,
        "estado": "Servidor funcionando correctamente"
    })

print("\n¿Cómo deseas ejecutar Flask?")
print("1. Modo prueba rápida en consola (sin bloquear)")
print("2. Iniciar servidor web en vivo (http://127.0.0.1:5000)")
opcion = input("Elige una opción (1 o 2): ").strip() or "1"

if opcion == "2":
    print("\n Servidor iniciado. Abre tu navegador en: http://127.0.0.1:5000")
    print("Para detener el servidor presiona Ctrl + C en la terminal.")
    app.run(port=5000, debug=False)
else:
    # Prueba en memoria con el cliente de Flask
    cliente = app.test_client()
    respuesta_home = cliente.get("/")
    respuesta_api = cliente.get("/api")
    
    print("\n--- Resultado de la prueba en memoria ---")
    print(f"Respuesta ruta '/': {respuesta_home.data.decode('utf-8')[:60]}...")
    print(f"Respuesta ruta '/api' (JSON): {respuesta_api.get_json()}")
