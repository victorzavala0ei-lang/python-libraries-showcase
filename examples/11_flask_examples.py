"""
Ejemplos del microframework web 'Flask' en Python.

Flask es un microframework ligero y extensible para construir aplicaciones web
y APIs RESTful en Python.

Instalación:
    pip install Flask
"""

import sys

try:
    from flask import Flask, jsonify, request, render_template_string
    FLASK_INSTALADO = True
except ImportError:
    FLASK_INSTALADO = False

if FLASK_INSTALADO:
    app = Flask(__name__)

    # Base de datos en memoria para el ejemplo
    TAREAS = [
        {"id": 1, "titulo": "Aprender Flask", "completada": True},
        {"id": 2, "titulo": "Crear repositorio GitHub", "completada": True},
        {"id": 3, "titulo": "Documentar ejemplos en README", "completada": False}
    ]

    @app.route("/")
    def inicio():
        """Ruta principal que responde con HTML simple."""
        html = """
        <html>
            <head><title>Demostración Flask</title></head>
            <body style="font-family: Arial, sans-serif; margin: 40px;">
                <h1 style="color: #2c3e50;">¡Bienvenido a la API con Flask!</h1>
                <p>Microframework para desarrollo web rápido en Python.</p>
                <ul>
                    <li><a href="/api/saludo/Estudiante">/api/saludo/Estudiante</a> - Saludo dinámico JSON</li>
                    <li><a href="/api/tareas">/api/tareas</a> - Lista de tareas REST en JSON</li>
                </ul>
            </body>
        </html>
        """
        return render_template_string(html)

    @app.route("/api/saludo/<nombre>", methods=["GET"])
    def saludo_personalizado(nombre):
        """Ruta con parámetro dinámico en la URL."""
        return jsonify({
            "mensaje": f"¡Hola, {nombre}! Bienvenido a Flask.",
            "version": "1.0",
            "exito": True
        })

    @app.route("/api/tareas", methods=["GET"])
    def obtener_tareas():
        """Endpoint GET para listar tareas con filtro opcional por query string."""
        completada_str = request.args.get("completada")
        if completada_str is not None:
            es_completada = completada_str.lower() in ["true", "1"]
            resultado = [t for t in TAREAS if t["completada"] == es_completada]
        else:
            resultado = TAREAS
        return jsonify({"total": len(resultado), "tareas": resultado})

    @app.route("/api/tareas", methods=["POST"])
    def crear_tarea():
        """Endpoint POST para agregar una nueva tarea mediante payload JSON."""
        datos = request.get_json()
        if not datos or "titulo" not in datos:
            return jsonify({"error": "El campo 'titulo' es obligatorio"}), 400
        
        nueva_tarea = {
            "id": len(TAREAS) + 1,
            "titulo": datos["titulo"],
            "completada": datos.get("completada", False)
        }
        TAREAS.append(nueva_tarea)
        return jsonify({"mensaje": "Tarea creada exitosamente", "tarea": nueva_tarea}), 201

    @app.errorhandler(404)
    def ruta_no_encontrada(error):
        """Manejador global para error 404."""
        return jsonify({"error": "Ruta no encontrada", "codigo": 404}), 404


def probar_aplicacion_con_cliente_de_pruebas():
    """Ejecuta pruebas en memoria utilizando el test_client oficial de Flask."""
    print("=" * 60)
    print("DEMOSTRACIÓN DE LA APLICACIÓN FLASK (VÍA TEST CLIENT)")
    print("=" * 60)
    
    if not FLASK_INSTALADO:
        print("[AVISO] La librería 'Flask' no está instalada.")
        print("Para instalarla ejecuta: pip install Flask")
        return

    cliente = app.test_client()
    
    # 1. Probar ruta raíz GET /
    print("\n1. Probando GET / (Página de inicio HTML):")
    res1 = cliente.get("/")
    print(f"  Status: {res1.status_code}")
    print(f"  Contenido preliminar: {res1.data.decode('utf-8')[:100].strip()}...")
    
    # 2. Probar ruta dinámica GET /api/saludo/Pythonista
    print("\n2. Probando GET /api/saludo/Pythonista (Ruta con parámetros):")
    res2 = cliente.get("/api/saludo/Pythonista")
    print(f"  Status: {res2.status_code}")
    print(f"  Respuesta JSON: {res2.get_json()}")
    
    # 3. Probar GET /api/tareas
    print("\n3. Probando GET /api/tareas (Listado de tareas):")
    res3 = cliente.get("/api/tareas")
    print(f"  Status: {res3.status_code}")
    print(f"  JSON recibido: {res3.get_json()}")
    
    # 4. Probar POST /api/tareas creando un recurso
    print("\n4. Probando POST /api/tareas (Crear nueva tarea en JSON):")
    nueva = {"titulo": "Subir repositorio a GitHub", "completada": False}
    res4 = cliente.post("/api/tareas", json=nueva)
    print(f"  Status: {res4.status_code}")
    print(f"  JSON respuesta: {res4.get_json()}")
    
    # 5. Probar ruta inexistente (404)
    print("\n5. Probando ruta no existente (Manejo de error 404):")
    res5 = cliente.get("/ruta/desconocida")
    print(f"  Status: {res5.status_code}")
    print(f"  JSON error: {res5.get_json()}")
    print()


def main():
    if "--servidor" in sys.argv:
        print("Iniciando servidor web Flask en http://127.0.0.1:5000 ...")
        app.run(host="127.0.0.1", port=5000, debug=True)
    else:
        probar_aplicacion_con_cliente_de_pruebas()
        print("Para levantar el servidor web en vivo ejecuta:")
        print("    python examples/11_flask_examples.py --servidor\n")


if __name__ == "__main__":
    main()
