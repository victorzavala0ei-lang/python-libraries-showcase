"""
Librería: Flask
Descripción: Servidor web profesional y API REST moderna desarrollada con Flask.
"""
import sys
import platform
import datetime

try:
    from flask import Flask, jsonify, render_template_string, request
except ImportError:
    print("[Error] La librería 'Flask' no está instalada. Ejecuta: pip install Flask")
    sys.exit(1)

print("=== EJEMPLO INTERACTIVO: FLASK (EDICIÓN PROFESIONAL) ===")

# Entrada de datos interactiva por teclado
nombre = input("Ingresa tu nombre para personalizar la aplicación: ").strip() or "Desarrollador Python"
mensaje = input("Ingresa un mensaje de bienvenida o eslogan: ").strip() or "Construyendo aplicaciones web modernas, rápidas y escalables con Python."

app = Flask(__name__)

# Contador de visitas en memoria
contador_visitas = 0

PLANTILLA_HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Flask Pro Dashboard | {{ nombre }}</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <script>
    tailwind.config = {
      theme: {
        extend: {
          fontFamily: {
            sans: ['"Plus Jakarta Sans"', 'sans-serif'],
            mono: ['"JetBrains Mono"', 'monospace'],
          },
          colors: {
            brand: {
              50: '#eef2ff',
              100: '#e0e7ff',
              500: '#6366f1',
              600: '#4f46e5',
              700: '#4338ca',
            }
          }
        }
      }
    }
  </script>
  <style>
    body { font-family: 'Plus Jakarta Sans', sans-serif; }
    .code-font { font-family: 'JetBrains Mono', monospace; }
    .glass {
      background: rgba(30, 41, 59, 0.7);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1px solid rgba(255, 255, 255, 0.08);
    }
    .glow {
      box-shadow: 0 0 50px -10px rgba(99, 102, 241, 0.25);
    }
  </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen antialiased selection:bg-indigo-500 selection:text-white">

  <!-- Background decorative glows -->
  <div class="fixed inset-0 overflow-hidden pointer-events-none -z-10">
    <div class="absolute -top-40 -right-40 w-96 h-96 bg-indigo-500/15 rounded-full blur-3xl"></div>
    <div class="absolute top-1/3 -left-40 w-96 h-96 bg-purple-500/15 rounded-full blur-3xl"></div>
    <div class="absolute -bottom-40 right-1/3 w-96 h-96 bg-emerald-500/10 rounded-full blur-3xl"></div>
  </div>

  <!-- Navbar -->
  <header class="border-b border-slate-800/80 bg-slate-950/80 backdrop-blur-md sticky top-0 z-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
      <div class="flex items-center gap-3">
        <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-indigo-600 via-indigo-500 to-purple-500 flex items-center justify-center shadow-lg shadow-indigo-500/30">
          <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
          </svg>
        </div>
        <div>
          <span class="font-extrabold text-lg tracking-tight bg-gradient-to-r from-white via-slate-100 to-indigo-200 bg-clip-text text-transparent">Flask Showcase</span>
          <span class="ml-2 px-2 py-0.5 text-[10px] font-semibold tracking-wider uppercase rounded-full bg-indigo-500/10 text-indigo-400 border border-indigo-500/20">v3.1 Pro</span>
        </div>
      </div>

      <div class="flex items-center gap-4">
        <div class="hidden sm:flex items-center gap-2 px-3 py-1.5 rounded-full bg-slate-900 border border-slate-800 text-xs">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
          <span class="text-slate-400">Servidor en línea:</span>
          <span class="font-mono text-emerald-400 font-semibold">127.0.0.1:5000</span>
        </div>
        <div class="flex items-center gap-2 pl-2 border-l border-slate-800">
          <div class="w-8 h-8 rounded-full bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center font-bold text-xs text-white">
            {{ nombre[:2].upper() }}
          </div>
          <span class="text-xs font-medium text-slate-300 hidden md:inline">{{ nombre }}</span>
        </div>
      </div>
    </div>
  </header>

  <!-- Main Container -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-10">

    <!-- Hero Section -->
    <section class="relative rounded-3xl glass p-8 sm:p-12 overflow-hidden glow">
      <div class="relative z-10 max-w-3xl space-y-5">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-500/10 border border-indigo-500/20 text-indigo-400 text-xs font-semibold">
          <svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 20 20">
            <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/>
          </svg>
          Microframework Web de Alto Rendimiento
        </div>

        <h1 class="text-3xl sm:text-5xl font-extrabold tracking-tight text-white leading-tight">
          ¡Hola, <span class="bg-gradient-to-r from-indigo-400 via-purple-300 to-pink-400 bg-clip-text text-transparent">{{ nombre }}</span>!
        </h1>

        <p class="text-base sm:text-lg text-slate-300 leading-relaxed font-normal">
          {{ mensaje }}
        </p>

        <div class="pt-2 flex flex-wrap gap-3">
          <a href="#playground" class="px-5 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-semibold text-sm shadow-lg shadow-indigo-600/30 transition-all flex items-center gap-2">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"/>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
            Probar API en Vivo
          </a>
          <a href="/api" target="_blank" class="px-5 py-2.5 rounded-xl bg-slate-800/80 hover:bg-slate-700/80 text-slate-200 font-semibold text-sm border border-slate-700 transition-all flex items-center gap-2">
            <svg class="w-4 h-4 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"/>
            </svg>
            Ver JSON (/api)
          </a>
        </div>
      </div>
    </section>

    <!-- Key Metrics Cards -->
    <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
      <div class="glass p-5 rounded-2xl space-y-2 border-l-4 border-l-indigo-500">
        <div class="flex items-center justify-between text-slate-400 text-xs uppercase tracking-wider font-semibold">
          <span>Servidor Web</span>
          <svg class="w-4 h-4 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h14M5 12a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v4a2 2 0 01-2 2M5 12a2 2 0 00-2 2v4a2 2 0 002 2h14a2 2 0 002-2v-4a2 2 0 00-2-2m-2-4h.01M17 16h.01"/>
          </svg>
        </div>
        <div class="text-2xl font-extrabold text-white">Flask WSGI</div>
        <div class="text-xs text-slate-400">Puerto <span class="text-indigo-300 font-mono">5000</span> • HTTP 1.1</div>
      </div>

      <div class="glass p-5 rounded-2xl space-y-2 border-l-4 border-l-purple-500">
        <div class="flex items-center justify-between text-slate-400 text-xs uppercase tracking-wider font-semibold">
          <span>Lenguaje</span>
          <svg class="w-4 h-4 text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"/>
          </svg>
        </div>
        <div class="text-2xl font-extrabold text-white">Python {{ python_version }}</div>
        <div class="text-xs text-slate-400">Plataforma <span class="text-purple-300 font-mono">{{ sistema }}</span></div>
      </div>

      <div class="glass p-5 rounded-2xl space-y-2 border-l-4 border-l-emerald-500">
        <div class="flex items-center justify-between text-slate-400 text-xs uppercase tracking-wider font-semibold">
          <span>Estado del API</span>
          <svg class="w-4 h-4 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
          </svg>
        </div>
        <div class="text-2xl font-extrabold text-emerald-400 flex items-center gap-2">
          200 OK
          <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-ping"></span>
        </div>
        <div class="text-xs text-slate-400">Endpoints activos y funcionales</div>
      </div>

      <div class="glass p-5 rounded-2xl space-y-2 border-l-4 border-l-pink-500">
        <div class="flex items-center justify-between text-slate-400 text-xs uppercase tracking-wider font-semibold">
          <span>Peticiones Atendidas</span>
          <svg class="w-4 h-4 text-pink-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
          </svg>
        </div>
        <div class="text-2xl font-extrabold text-white font-mono" id="live-counter">{{ visitas }}</div>
        <div class="text-xs text-slate-400">Contador en tiempo real</div>
      </div>
    </section>

    <!-- Interactive API Playground -->
    <section id="playground" class="glass rounded-3xl p-6 sm:p-8 space-y-6">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-800 pb-5">
        <div>
          <h2 class="text-xl sm:text-2xl font-bold text-white flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-indigo-500"></span>
            Consola Interactiva de API REST
          </h2>
          <p class="text-sm text-slate-400 mt-1">
            Haz clic en los botones para enviar solicitudes HTTP reales al servidor Flask y ver la respuesta JSON al instante.
          </p>
        </div>
        <div class="flex items-center gap-2 text-xs font-mono text-slate-400 bg-slate-900/90 px-3 py-1.5 rounded-lg border border-slate-800">
          <span class="text-indigo-400">Base URL:</span> http://127.0.0.1:5000
        </div>
      </div>

      <!-- Action Buttons -->
      <div class="flex flex-wrap gap-2.5">
        <button onclick="consumirAPI('/api')" class="px-4 py-2 rounded-xl bg-indigo-600/90 hover:bg-indigo-600 text-white font-medium text-xs transition flex items-center gap-2">
          <span class="px-1.5 py-0.5 rounded bg-indigo-800 text-[10px] font-mono">GET</span>
          <span>/api</span>
        </button>

        <button onclick="consumirAPI('/api/saludo')" class="px-4 py-2 rounded-xl bg-purple-600/90 hover:bg-purple-600 text-white font-medium text-xs transition flex items-center gap-2">
          <span class="px-1.5 py-0.5 rounded bg-purple-800 text-[10px] font-mono">GET</span>
          <span>/api/saludo</span>
        </button>

        <button onclick="consumirAPI('/api/metricas')" class="px-4 py-2 rounded-xl bg-emerald-600/90 hover:bg-emerald-600 text-white font-medium text-xs transition flex items-center gap-2">
          <span class="px-1.5 py-0.5 rounded bg-emerald-800 text-[10px] font-mono">GET</span>
          <span>/api/metricas</span>
        </button>

        <button onclick="consumirAPI('/api/librerias')" class="px-4 py-2 rounded-xl bg-amber-600/90 hover:bg-amber-600 text-white font-medium text-xs transition flex items-center gap-2">
          <span class="px-1.5 py-0.5 rounded bg-amber-800 text-[10px] font-mono">GET</span>
          <span>/api/librerias</span>
        </button>
      </div>

      <!-- Response Box -->
      <div class="rounded-2xl bg-slate-950 border border-slate-800 overflow-hidden shadow-2xl">
        <div class="flex items-center justify-between px-4 py-2.5 bg-slate-900/90 border-b border-slate-800 text-xs">
          <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-red-500/80 inline-block"></span>
            <span class="w-3 h-3 rounded-full bg-yellow-500/80 inline-block"></span>
            <span class="w-3 h-3 rounded-full bg-green-500/80 inline-block"></span>
            <span class="font-mono text-slate-400 ml-2" id="endpoint-name">Respuesta JSON</span>
          </div>
          <div class="flex items-center gap-3">
            <span id="response-status" class="px-2 py-0.5 rounded text-[11px] font-mono font-semibold bg-emerald-500/20 text-emerald-400">Listo</span>
            <button onclick="copiarRespuesta()" class="text-slate-400 hover:text-white transition text-xs flex items-center gap-1">
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"/>
              </svg>
              Copiar
            </button>
          </div>
        </div>

        <pre class="p-5 text-sm code-font overflow-x-auto text-emerald-400 max-h-96 leading-relaxed" id="json-viewer">// Haz clic en cualquiera de los botones de arriba para consultar el API en tiempo real.</pre>
      </div>
    </section>

    <!-- Table of Endpoints -->
    <section class="glass rounded-3xl p-6 sm:p-8 space-y-4">
      <h3 class="text-lg font-bold text-white flex items-center gap-2">
        <svg class="w-5 h-5 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 10h16M4 14h16M4 18h16"/>
        </svg>
        Documentación de Endpoints del Proyecto
      </h3>
      <div class="overflow-x-auto">
        <table class="w-full text-left text-sm text-slate-300">
          <thead class="text-xs uppercase bg-slate-900/60 text-slate-400 border-b border-slate-800">
            <tr>
              <th class="py-3 px-4">Método</th>
              <th class="py-3 px-4">Ruta</th>
              <th class="py-3 px-4">Descripción</th>
              <th class="py-3 px-4">Tipo de Retorno</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-800/60 font-mono text-xs">
            <tr>
              <td class="py-3 px-4"><span class="px-2 py-0.5 rounded bg-indigo-500/20 text-indigo-300 font-bold">GET</span></td>
              <td class="py-3 px-4 text-white">/</td>
              <td class="py-3 px-4 font-sans text-slate-300">Dashboard interactivo profesional con Tailwind CSS</td>
              <td class="py-3 px-4 text-indigo-300">HTML5 / Responsive</td>
            </tr>
            <tr>
              <td class="py-3 px-4"><span class="px-2 py-0.5 rounded bg-indigo-500/20 text-indigo-300 font-bold">GET</span></td>
              <td class="py-3 px-4 text-white">/api</td>
              <td class="py-3 px-4 font-sans text-slate-300">Estado general de la aplicación y autor</td>
              <td class="py-3 px-4 text-emerald-400">JSON</td>
            </tr>
            <tr>
              <td class="py-3 px-4"><span class="px-2 py-0.5 rounded bg-indigo-500/20 text-indigo-300 font-bold">GET</span></td>
              <td class="py-3 px-4 text-white">/api/saludo</td>
              <td class="py-3 px-4 font-sans text-slate-300">Saludo personalizado dinámico (admite ?nombre=...)</td>
              <td class="py-3 px-4 text-emerald-400">JSON</td>
            </tr>
            <tr>
              <td class="py-3 px-4"><span class="px-2 py-0.5 rounded bg-indigo-500/20 text-indigo-300 font-bold">GET</span></td>
              <td class="py-3 px-4 text-white">/api/metricas</td>
              <td class="py-3 px-4 font-sans text-slate-300">Métricas de ejecución, hora del servidor y sistema</td>
              <td class="py-3 px-4 text-emerald-400">JSON</td>
            </tr>
            <tr>
              <td class="py-3 px-4"><span class="px-2 py-0.5 rounded bg-indigo-500/20 text-indigo-300 font-bold">GET</span></td>
              <td class="py-3 px-4 text-white">/api/librerias</td>
              <td class="py-3 px-4 font-sans text-slate-300">Catálogo de las 12 librerías del showcase</td>
              <td class="py-3 px-4 text-emerald-400">JSON</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

  </main>

  <!-- Footer -->
  <footer class="border-t border-slate-800/80 mt-16 py-8 text-center text-xs text-slate-400">
    <div class="max-w-7xl mx-auto px-4 space-y-2">
      <p class="font-medium text-slate-300">
        Python Libraries Showcase • Servidor Web impulsado por Flask
      </p>
      <p class="text-slate-400">
        Personalizado para <span class="text-indigo-400 font-semibold">{{ nombre }}</span> • {{ ahora }}
      </p>
    </div>
  </footer>

  <!-- Client Script -->
  <script>
    async function consumirAPI(endpoint) {
      const viewer = document.getElementById('json-viewer');
      const endpointName = document.getElementById('endpoint-name');
      const statusPill = document.getElementById('response-status');
      
      endpointName.textContent = 'Consultando: ' + endpoint + ' ...';
      statusPill.className = 'px-2 py-0.5 rounded text-[11px] font-mono font-semibold bg-amber-500/20 text-amber-400';
      statusPill.textContent = 'Cargando...';

      try {
        const respuesta = await fetch(endpoint);
        const data = await respuesta.json();
        
        endpointName.textContent = endpoint;
        statusPill.className = 'px-2 py-0.5 rounded text-[11px] font-mono font-semibold bg-emerald-500/20 text-emerald-400';
        statusPill.textContent = respuesta.status + ' OK';
        
        viewer.textContent = JSON.stringify(data, null, 2);
      } catch (err) {
        endpointName.textContent = endpoint;
        statusPill.className = 'px-2 py-0.5 rounded text-[11px] font-mono font-semibold bg-rose-500/20 text-rose-400';
        statusPill.textContent = 'Error';
        viewer.textContent = '// Error al conectar con el endpoint:\\n' + err.message;
      }
    }

    function copiarRespuesta() {
      const viewer = document.getElementById('json-viewer');
      navigator.clipboard.writeText(viewer.textContent).then(() => {
        alert('¡JSON copiado al portapapeles!');
      });
    }

    // Cargar automáticamente /api al inicio
    window.addEventListener('DOMContentLoaded', () => {
      consumirAPI('/api');
    });
  </script>
</body>
</html>
"""

@app.route("/")
def inicio():
    global contador_visitas
    contador_visitas += 1
    return render_template_string(
        PLANTILLA_HTML,
        nombre=nombre,
        mensaje=mensaje,
        visitas=contador_visitas,
        python_version=platform.python_version(),
        sistema=f"{platform.system()} {platform.machine()}",
        ahora=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    )

@app.route("/api")
def api():
    global contador_visitas
    return jsonify({
        "status": "success",
        "codigo": 200,
        "aplicacion": "Flask Showcase API Pro",
        "desarrollador": nombre,
        "mensaje": mensaje,
        "servidor": {
            "framework": "Flask",
            "version_python": platform.python_version(),
            "sistema_operativo": platform.system(),
            "visitas_totales": contador_visitas
        },
        "endpoints_disponibles": [
            "/",
            "/api",
            "/api/saludo",
            "/api/metricas",
            "/api/librerias"
        ]
    })

@app.route("/api/saludo")
def saludo():
    usuario_query = request.args.get("nombre", nombre)
    return jsonify({
        "saludo": f"¡Hola, {usuario_query}!",
        "mensaje": mensaje,
        "timestamp": datetime.datetime.now().isoformat(),
        "cliente_ip": request.remote_addr or "127.0.0.1"
    })

@app.route("/api/metricas")
def metricas():
    return jsonify({
        "estado_sistema": "OPTIMO",
        "tiempo_servidor": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "arquitectura": platform.architecture()[0],
        "procesador": platform.processor() or platform.machine(),
        "contador_peticiones": contador_visitas,
        "protocolo": request.environ.get('SERVER_PROTOCOL', 'HTTP/1.1')
    })

@app.route("/api/librerias")
def librerias():
    return jsonify({
        "total_librerias": 12,
        "categoria_estandar": ["math", "random", "datetime", "csv"],
        "categoria_pdf": ["fpdf2", "reportlab"],
        "categoria_datos_ia": ["numpy", "pandas", "matplotlib", "scikit-learn"],
        "categoria_red_web": ["requests", "Flask"]
    })

print("\n¿Cómo deseas ejecutar Flask?")
print("1. Iniciar servidor web en vivo (http://127.0.0.1:5000) [Recomendado]")
print("2. Modo prueba rápida en consola (sin bloquear)")
opcion = input("Elige una opción (1 o 2, por defecto 1): ").strip() or "1"

if opcion == "1":
    print("\n" + "=" * 70)
    print(" ¡SERVIDOR WEB FLASK EN VIVO INICIADO!")
    print(" Abre tu navegador web en: http://127.0.0.1:5000")
    print(" Para detener el servidor presiona Ctrl + C en tu terminal.")
    print("=" * 70 + "\n")
    app.run(host="127.0.0.1", port=5000, debug=False)
else:
    # Modo de prueba rápida en memoria
    print("\n--- Ejecutando prueba de endpoints en memoria ---")
    cliente = app.test_client()
    r_home = cliente.get("/")
    r_api = cliente.get("/api")
    r_metricas = cliente.get("/api/metricas")
    
    print(f"✓ Ruta '/' (HTML): Código {r_home.status_code} - Tamaño {len(r_home.data)} bytes")
    print(f"✓ Ruta '/api' (JSON): Código {r_api.status_code}")
    print(f"  Datos recibidos: {r_api.get_json()['aplicacion']}")
    print(f"✓ Ruta '/api/metricas' (JSON): Código {r_metricas.status_code}")
    print(f"  Estado sistema: {r_metricas.get_json()['estado_sistema']}")
    print("\n¡Prueba completada con éxito!")
