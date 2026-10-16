# 🚀 Python Libraries Showcase

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1%2B-black.svg?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![NumPy](https://img.shields.io/badge/NumPy-2.0%2B-013243.svg?logo=numpy&logoColor=white)](https://numpy.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.2%2B-150458.svg?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.4%2B-F7931E.svg?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Repository](https://img.shields.io/badge/GitHub-victorzavala0ei--lang-181717.svg?logo=github&logoColor=white)](https://github.com/victorzavala0ei-lang/python-libraries-showcase)

Colección interactiva y didáctica de ejemplos prácticos en **Python** para dominar **12 librerías esenciales**. Cada script está optimizado para ejecutarse en terminal con entrada por teclado (`input()`), cuenta con valores por defecto inmediatos y genera salidas tangibles (archivos PDF, imágenes PNG, datos CSV y una aplicación web profesional).

🔗 **Liga del repositorio en GitHub:**  
👉 **[https://github.com/victorzavala0ei-lang/python-libraries-showcase](https://github.com/victorzavala0ei-lang/python-libraries-showcase)**

---

## 📁 Estructura del Repositorio

```text
python-libraries-showcase/
├── README.md                  # Documentación completa del proyecto
├── requirements.txt           # Dependencias externas del proyecto
├── main.py                    # Menú interactivo central para ejecutar los ejemplos
└── examples/                  # Carpeta con los 12 ejemplos individuales
    ├── 01_math_examples.py
    ├── 02_random_examples.py
    ├── 03_datetime_examples.py
    ├── 04_csv_examples.py
    ├── 05_fpdf_examples.py
    ├── 06_reportlab_examples.py
    ├── 07_numpy_examples.py
    ├── 08_pandas_examples.py
    ├── 09_matplotlib_examples.py
    ├── 10_requests_examples.py
    ├── 11_flask_examples.py
    └── 12_scikit_learn_examples.py
```

---

## ⚙️ Instalación y Configuración

### 1. Clonar el repositorio
```bash
git clone https://github.com/victorzavala0ei-lang/python-libraries-showcase.git
cd python-libraries-showcase
```

### 2. Crear y activar entorno virtual
```bash
# macOS / Linux:
python3 -m venv .venv
source .venv/bin/activate

# Windows:
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instalar dependencias
Las librerías estándar (`math`, `random`, `datetime`, `csv`) vienen integradas en Python. Para instalar las librerías externas:
```bash
pip install -r requirements.txt
```

---

## 🎮 Cómo Ejecutar los Ejemplos

### Opción A: Menú Interactivo Central (Recomendado)
Ejecuta el menú para correr cualquier ejemplo escribiendo solo su número:
```bash
python main.py
```

### Opción B: Ejecutar un script específico
```bash
python examples/01_math_examples.py
python examples/08_pandas_examples.py
python examples/11_flask_examples.py
```
*(O abre el archivo en VS Code / Antigravity y haz clic en el botón de **Ejecutar ▶️**).*

---

## 📚 Explicación Detallada de Cada Uno de los 12 Ejemplos

---

### 1. Librería `math` — Operaciones Matemáticas y Trigonometría
* **Archivo:** [`examples/01_math_examples.py`](examples/01_math_examples.py)
* **Categoría:** Biblioteca estándar de Python (no requiere instalación externa).
* **¿Qué hace?**  
  Demuestra funciones matemáticas avanzadas y constantes numéricas de alta precisión que superan los operadores básicos (`+`, `-`, `*`).
* **Conceptos y métodos clave:**
  * `math.sqrt(x)`: Raíz cuadrada de un número real.
  * `math.ceil(x)` y `math.floor(x)`: Redondeo hacia arriba y hacia abajo al entero más próximo.
  * `math.factorial(n)`: Cálculo de permutaciones y combinatoria para números enteros.
  * `math.radians(grados)`: Conversión de ángulos sexagesimales a radianes.
  * `math.sin(rad)`, `math.cos(rad)` y `math.pi`: Funciones trigonométricas fundamentales.
* **Entrada por teclado:** Solicita un número decimal (ej. `16.7`) y un ángulo en grados (ej. `45`).

---

### 2. Librería `random` — Generación Pseudoaleatoria y Muestreo
* **Archivo:** [`examples/02_random_examples.py`](examples/02_random_examples.py)
* **Categoría:** Biblioteca estándar de Python.
* **¿Qué hace?**  
  Implementa algoritmos de aleatoriedad para simulación de datos, sorteos y juegos de azar.
* **Conceptos y métodos clave:**
  * `random.randint(a, b)`: Genera un número entero aleatorio dentro del intervalo cerrado `[a, b]`.
  * `random.uniform(a, b)`: Genera un número decimal continuo en punto flotante.
  * `random.choice(secuencia)`: Selecciona un elemento aleatorio de una lista de opciones.
  * `random.shuffle(secuencia)`: Reordena aleatoriamente los elementos de una lista in-situ.
* **Entrada por teclado:** Rango numérico (mínimo y máximo) y lista de opciones separadas por coma para el sorteo.

---

### 3. Librería `datetime` — Gestión de Fechas, Horas y Aritmética Temporal
* **Archivo:** [`examples/03_datetime_examples.py`](examples/03_datetime_examples.py)
* **Categoría:** Biblioteca estándar de Python.
* **¿Qué hace?**  
  Facilita el manejo de sellos de tiempo, cálculo de lapsos transcurridos y proyección de eventos futuros.
* **Conceptos y métodos clave:**
  * `datetime.now()`: Obtiene la fecha y hora exacta del sistema local.
  * `datetime.strptime(cadena, formato)`: Parsea una cadena de texto a un objeto `datetime` tipado.
  * `datetime.strftime(formato)`: Formatea objetos de fecha a texto legible para el usuario.
  * `timedelta(days=n)`: Objeto para sumar o restar duraciones de tiempo a una fecha determinada.
* **Entrada por teclado:** Una fecha histórica en formato `AAAA-MM-DD` y el número de días a proyectar hacia el futuro.

---

### 4. Librería `csv` — Lectura y Escritura de Datos Tabulares
* **Archivo:** [`examples/04_csv_examples.py`](examples/04_csv_examples.py)
* **Categoría:** Biblioteca estándar de Python.
* **¿Qué hace?**  
  Almacena y recupera información tabular estructurada en formato delimitado por comas (`.csv`), compatible con Excel y bases de datos.
* **Conceptos y métodos clave:**
  * `csv.writer(f)` y `escritor.writerow()`: Escritura de encabezados de columna y registros de datos con manejo adecuado de saltos de línea.
  * `csv.reader(f)`: Parseo línea por línea del archivo CSV para procesar filas de datos.
* **Entrada por teclado:** Datos de contactos (Nombre, Correo electrónico y Teléfono).
* **Salida generada:** Archivo físico [`contactos.csv`](examples/contactos.csv) guardado en disco.

---

### 5. Librería `fpdf2` — Generación Básica y Rápida de Documentos PDF
* **Archivo:** [`examples/05_fpdf_examples.py`](examples/05_fpdf_examples.py)
* **Categoría:** Librería externa (`pip install fpdf2`).
* **¿Qué hace?**  
  Crea documentos PDF sencillos de forma procedural, ideal para recibos, certificados y notas rápidas.
* **Conceptos y métodos clave:**
  * `FPDF()` y `pdf.add_page()`: Inicialización del lienzo y adición de páginas en blanco.
  * `pdf.set_font(familia, estilo, tamaño)`: Selección tipográfica (ej. Helvetica negrita o cursiva).
  * `pdf.cell(ancho, alto, texto, ...)`: Renderizado de celdas y títulos centrados.
  * `pdf.multi_cell()`: Párrafos de texto multilínea con ajuste automático de margen.
  * `pdf.output(nombre)`: Compilación y guardado del archivo binario PDF.
* **Entrada por teclado:** Título del documento, nombre del autor y mensaje a incluir.
* **Salida generada:** Archivo [`mi_documento_fpdf.pdf`](examples/mi_documento_fpdf.pdf).

---

### 6. Librería `reportlab` — Maquetación y Publicación Profesional de PDFs
* **Archivo:** [`examples/06_reportlab_examples.py`](examples/06_reportlab_examples.py)
* **Categoría:** Librería externa (`pip install reportlab`).
* **¿Qué hace?**  
  Genera documentos PDF de calidad editorial y corporativa utilizando el motor estructurado Platypus (diseño basado en flujo de elementos).
* **Conceptos y métodos clave:**
  * `SimpleDocTemplate`: Gestor del documento con especificación de dimensiones de página (`letter`).
  * `getSampleStyleSheet()` y `ParagraphStyle`: Creación y herencia de hojas de estilo tipográficas avanzadas (fuentes, tamaños, espacios y colores CMYK/RGB).
  * `Paragraph`: Elemento de texto con soporte de micro-etiquetas HTML (como `<i>` para cursiva o `<b>` para negrita).
  * `Spacer`: Control de espaciado vertical milimétrico entre elementos.
  * `doc.build(elementos)`: Renderizado declarativo de la lista de elementos en el PDF.
* **Entrada por teclado:** Título corporativo y notas de contenido para el reporte.
* **Salida generada:** Archivo [`reporte_reportlab.pdf`](examples/reporte_reportlab.pdf).

---

### 7. Librería `NumPy` — Computación Científica y Arreglos Multidimensionales
* **Archivo:** [`examples/07_numpy_examples.py`](examples/07_numpy_examples.py)
* **Categoría:** Librería externa (`pip install numpy`).
* **¿Qué hace?**  
  Proporciona estructuras de datos vectoriales optimizadas en C (`ndarray`) y operaciones matemáticas de alto rendimiento sin requerir bucles lentos en Python.
* **Conceptos y métodos clave:**
  * `np.array(lista)`: Creación de arreglos homogéneos en memoria contigua.
  * `np.sum()`, `np.mean()`, `np.max()`, `np.min()`: Operaciones de agregación y estadística descriptiva.
  * `np.std()`: Cálculo de la desviación estándar poblacional/muestral.
  * Vectorización (`datos * multiplicador`): Operaciones aritméticas escalares aplicadas instantáneamente a todos los elementos del arreglo.
* **Entrada por teclado:** Serie de números separados por espacio (ej. `10 25 40 55 70`) y un número multiplicador.

---

### 8. Librería `Pandas` — Análisis y Manipulación de Datos Estructurados
* **Archivo:** [`examples/08_pandas_examples.py`](examples/08_pandas_examples.py)
* **Categoría:** Librería externa (`pip install pandas`).
* **¿Qué hace?**  
  Crea y manipula tablas bidimensionales (`DataFrames`) con etiquetas de filas y columnas, facilitando tareas de ciencia de datos, limpieza y filtrado.
* **Conceptos y métodos clave:**
  * `pd.DataFrame(diccionario)`: Construcción tabular a partir de colecciones de datos.
  * `df['Columna'].mean()` y `df['Columna'].max()`: Métricas analíticas de series numéricas.
  * Filtrado booleano (`df[df['Precio'] > limite]`): Extracción condicional de registros que cumplen un criterio.
* **Entrada por teclado:** Nombres y precios de 3 productos, más un valor límite para aplicar el filtro de precios.

---

### 9. Librería `Matplotlib` — Visualización de Datos y Gráficos Estadísticos
* **Archivo:** [`examples/09_matplotlib_examples.py`](examples/09_matplotlib_examples.py)
* **Categoría:** Librería externa (`pip install matplotlib`).
* **¿Qué hace?**  
  Genera figuras, gráficos interactivos y visualizaciones estáticas para análisis cuantitativo.
* **Conceptos y métodos clave:**
  * `matplotlib.use('Agg')`: Configuración del backend sin interfaz gráfica para renderizado seguro en servidores y scripts sin bloqueo.
  * `plt.figure(figsize=(7, 4))`: Dimensionamiento del lienzo de dibujo.
  * `plt.bar(categorias, valores)`: Creación del diagrama de barras categórico.
  * `plt.title()`, `plt.xlabel()`, `plt.ylabel()`, `plt.grid()`: Anotaciones, leyendas y cuadrículas de apoyo visual.
  * `plt.savefig('mi_grafico.png', dpi=120)`: Exportación a mapa de bits de alta resolución.
* **Entrada por teclado:** Título de la gráfica, nombres de categorías separadas por coma y sus respectivos valores numéricos.
* **Salida generada:** Imagen [`mi_grafico.png`](examples/mi_grafico.png).

---

### 10. Librería `Requests` — Comunicación HTTP y Consumo de APIs REST
* **Archivo:** [`examples/10_requests_examples.py`](examples/10_requests_examples.py)
* **Categoría:** Librería externa (`pip install requests`).
* **¿Qué hace?**  
  Envía peticiones de red HTTP/1.1 de forma sencilla para consumir servicios web, microservicios y APIs públicas en internet.
* **Conceptos y métodos clave:**
  * `requests.get(url, timeout=5)`: Ejecución de una petición `GET` con temporizador de seguridad contra bloqueos.
  * `respuesta.status_code`: Comprobación del código de respuesta del servidor (ej. `200 OK`).
  * `respuesta.json()`: Deserialización automática del payload JSON a un diccionario nativo de Python.
  * Manejo robusto de excepciones ante cortes de red o caídas del servidor.
* **Entrada por teclado:** ID numérico de usuario (del 1 al 10) para consultar en la API pública JSONPlaceholder.

---

### 11. Librería `Flask` — Servidor Web y API REST (Edición Profesional)
* **Archivo:** [`examples/11_flask_examples.py`](examples/11_flask_examples.py)
* **Categoría:** Librería externa (`pip install Flask`).
* **¿Qué hace?**  
  Implementa un servidor web WSGI moderno con una interfaz de **Dashboard Profesional** completa, estilizada con **Tailwind CSS** y **Glassmorphism**, más una API REST documentada en tiempo real.
* **Conceptos y métodos clave:**
  * `Flask(__name__)`: Instanciación del servidor web y enrutador.
  * `@app.route("/")`: Enrutamiento del dashboard principal renderizado con `render_template_string`.
  * `jsonify()`: Respuestas serializadas estándar en JSON para clientes móviles y front-ends.
  * `request.args.get()` y `request.remote_addr`: Captura de parámetros en Query String y metadatos de red del cliente.
  * `app.test_client()`: Cliente de pruebas unitarias en memoria para validar rutas sin levantar sockets de red.
* **Endpoints incluidos:**
  * `/`: Dashboard SaaS moderno responsivo con tarjetas de KPIs en vivo.
  * `/api`: Metadatos generales del estado de la aplicación.
  * `/api/saludo`: Saludo interactivo personalizado dinámicamente.
  * `/api/metricas`: Diagnóstico en tiempo real (arquitectura, procesador, hora y visitas).
  * `/api/librerias`: Catálogo clasificado de las 12 librerías del proyecto.
* **Consola interactiva en el navegador:** Incluye un probador de endpoints integrado con `fetch()` en JavaScript y botón para copiar respuestas al portapapeles.
* **Entrada por teclado:** Tu nombre y un mensaje de bienvenida para personalizar todo el diseño web.

---

### 12. Librería `scikit-learn` — Inteligencia Artificial y Regresión Lineal
* **Archivo:** [`examples/12_scikit_learn_examples.py`](examples/12_scikit_learn_examples.py)
* **Categoría:** Librería externa (`pip install scikit-learn numpy`).
* **¿Qué hace?**  
  Aplica algoritmos de aprendizaje automático (*Machine Learning*) supervisado para modelar tendencias y realizar predicciones numéricas continuas.
* **Conceptos y métodos clave:**
  * `LinearRegression()`: Inicialización del estimador de regresión por mínimos cuadrados ordinarios.
  * `modelo.fit(X, y)`: Fase de entrenamiento donde el algoritmo calcula los pesos óptimos a partir de datos históricos (horas de estudio vs. calificación obtenida).
  * `modelo.predict([[horas]])`: Inferencia de nuevos valores no vistos previamente.
  * `modelo.coef_` y `modelo.intercept_`: Parámetros matemáticos aprendidos (pendiente y ordenada al origen de la recta de regresión).
* **Entrada por teclado:** Número de horas que planeas estudiar para predecir tu calificación estimada en una escala de 0 a 100.

---

## 👨‍💻 Autor y Licencia

* **Autor:** [victorzavala0ei-lang](https://github.com/victorzavala0ei-lang)
* **Repositorio Oficial:** [https://github.com/victorzavala0ei-lang/python-libraries-showcase](https://github.com/victorzavala0ei-lang/python-libraries-showcase)
* **Licencia:** Proyecto educativo de código abierto bajo la Licencia MIT.
