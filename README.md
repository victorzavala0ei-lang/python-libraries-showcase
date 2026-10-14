# 🚀 Python Libraries Showcase (Guía Práctica y Ejemplos)

Este repositorio contiene una colección organizada, documentada y ejecutable de códigos en **Python** que ilustran el uso práctico de **12 librerías esenciales**, abarcando desde módulos estándar de matemáticas y fechas hasta potentes librerías externas de ciencia de datos, machine learning, desarrollo web y generación de documentos PDF.

---

## 📋 Tabla de Contenidos

- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Instalación y Configuración](#-instalación-y-configuración)
- [Explicación Detallada de cada Librería y Ejemplo](#-explicación-detallada-de-cada-librería-y-ejemplo)
  - [1. math](#1-math)
  - [2. random](#2-random)
  - [3. datetime](#3-datetime)
  - [4. csv](#4-csv)
  - [5. fpdf (fpdf2)](#5-fpdf-fpdf2)
  - [6. reportlab](#6-reportlab)
  - [7. NumPy](#7-numpy)
  - [8. Pandas](#8-pandas)
  - [9. Matplotlib](#9-matplotlib)
  - [10. Requests](#10-requests)
  - [11. Flask](#11-flask)
  - [12. scikit-learn](#12-scikit-learn)
- [Ejecutor Central (Menu Interactivo)](#-ejecutor-central-mainpy)
- [Publicación y Subida a GitHub](#-cómo-subir-este-proyecto-a-tu-github)

---

## 📂 Estructura del Proyecto

```text
python-libraries-showcase/
├── README.md                          # Documentación completa y explicaciones
├── requirements.txt                   # Dependencias de paquetes externos
├── .gitignore                         # Reglas para omitir archivos temporales y venv
├── main.py                            # Menú interactivo para ejecutar cualquier ejemplo
└── examples/
    ├── 01_math_examples.py            # Operaciones matemáticas y funciones avanzadas
    ├── 02_random_examples.py          # Generación pseudoaleatoria y probabilidades
    ├── 03_datetime_examples.py        # Manipulación de fechas, horas y zonas horarias
    ├── 04_csv_examples.py             # Lectura y escritura tabular CSV / TSV
    ├── 05_fpdf_examples.py            # Generación ágil de PDFs y tablas con FPDF
    ├── 06_reportlab_examples.py       # Creación de PDFs empresariales con Platypus
    ├── 07_numpy_examples.py           # Arreglos n-dimensionales y álgebra lineal
    ├── 08_pandas_examples.py          # DataFrames, filtrado, agregaciones y nulos
    ├── 09_matplotlib_examples.py      # Trazado de gráficos (líneas, barras, scatter, hist)
    ├── 10_requests_examples.py        # Peticiones HTTP REST (GET, POST, headers, errores)
    ├── 11_flask_examples.py           # API web RESTful con rutas y cliente de pruebas
    └── 12_scikit_learn_examples.py    # Clasificación, regresión y clustering con ML
```

---

## ⚙️ Instalación y Configuración

### 1. Prerrequisitos
- Tener instalado **Python 3.9 o superior** (compatible con Python 3.10, 3.11, 3.12 y 3.13+).
- Gestor de paquetes `pip` y control de versiones `git`.

### 2. Crear y Activar un Entorno Virtual

Se recomienda utilizar un entorno virtual para aislar las dependencias:

**En macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**En Windows (PowerShell / CMD):**
```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instalar Dependencias

Las librerías `math`, `random`, `datetime` y `csv` forman parte de la biblioteca estándar de Python (no requieren instalación adicional). Para las 8 librerías externas restantes, ejecuta:

```bash
pip install -r requirements.txt
```

---

## 📚 Explicación Detallada de cada Librería y Ejemplo

---

### 1. `math`
- **Tipo**: Biblioteca estándar de Python (Built-in).
- **Archivo**: [`examples/01_math_examples.py`](examples/01_math_examples.py)
- **¿Qué es y para qué sirve?**: Proporciona acceso a funciones matemáticas básicas y avanzadas definidas por el estándar C (trigonometría, logaritmos, constantes fundamentales, combinatoria y teoría de números).

#### Funciones Clave Demostradas:
- `math.pi`, `math.e`, `math.tau`: Constantes universales con alta precisión flotante.
- `math.ceil()`, `math.floor()`, `math.trunc()`: Control estricto de redondeo hacia arriba, abajo o eliminación de decimales.
- `math.sqrt()`, `math.isqrt()`: Raíz cuadrada real y raíz cuadrada entera de alto rendimiento.
- `math.sin()`, `math.cos()`, `math.tan()`, `math.radians()`: Funciones trigonométricas sobre ángulos convertidos a radianes.
- `math.gcd()`, `math.lcm()`, `math.factorial()`, `math.comb()`: Máximo común divisor, mínimo común múltiplo, factoriales y combinatoria.

#### Ejecución:
```bash
python examples/01_math_examples.py
```

---

### 2. `random`
- **Tipo**: Biblioteca estándar de Python (Built-in).
- **Archivo**: [`examples/02_random_examples.py`](examples/02_random_examples.py)
- **¿Qué es y para qué sirve?**: Implementa generadores de números pseudoaleatorios basados en el algoritmo Mersenne Twister para modelado estocástico, simulaciones, juegos y muestreo.

#### Funciones Clave Demostradas:
- `random.randint(a, b)`: Entero aleatorio en rango cerrado $[a, b]$.
- `random.random()`, `random.uniform(a, b)`: Flotantes en $[0.0, 1.0)$ o dentro de un intervalo arbitrario.
- `random.gauss(mu, sigma)`: Generación de valores con distribución normal (gaussiana).
- `random.choice(seq)` / `random.sample(seq, k)`: Selección individual o muestreo de $k$ elementos únicos sin reemplazo.
- `random.choices(seq, weights=...)`: Sorteo con ponderaciones o probabilidades diferenciadas.
- `random.shuffle(lista)`: Mezcla in-place de elementos dentro de una lista.
- `random.seed(x)`: Fijación de la semilla para garantizar reproducibilidad exacta en experimentos.

#### Ejecución:
```bash
python examples/02_random_examples.py
```

---

### 3. `datetime`
- **Tipo**: Biblioteca estándar de Python (Built-in).
- **Archivo**: [`examples/03_datetime_examples.py`](examples/03_datetime_examples.py)
- **¿Qué es y para qué sirve?**: Permite crear, manipular, formatear y comparar fechas, horas e intervalos temporales con soporte para zonas horarias.

#### Funciones Clave Demostradas:
- `date.today()`, `datetime.now()`: Obtención del momento actual en el sistema.
- `strftime(formato)`: Conversión de objetos fecha a texto con formato personalizado (`%d/%m/%Y`, `%H:%M:%S`).
- `strptime(cadena, formato)`: Análisis sintáctico (parsing) de cadenas de texto hacia objetos `datetime`.
- `timedelta(days=..., hours=...)`: Aritmética de fechas (adición o sustracción de intervalos, cálculo de días restantes).
- `timezone`, `timezone.utc`: Normalización a UTC y conversión a zonas horarias locales con offset específico.

#### Ejecución:
```bash
python examples/03_datetime_examples.py
```

---

### 4. `csv`
- **Tipo**: Biblioteca estándar de Python (Built-in).
- **Archivo**: [`examples/04_csv_examples.py`](examples/04_csv_examples.py)
- **¿Qué es y para qué sirve?**: Facilita la lectura y escritura eficiente de archivos con datos tabulares delimitados por comas, puntos y coma o tabuladores.

#### Funciones Clave Demostradas:
- `csv.writer()` y `csv.reader()`: Procesamiento secuencial fila por fila basado en listas.
- `csv.DictWriter()` y `csv.DictReader()`: Mapeo automático de filas a diccionarios usando los nombres de las columnas en la cabecera.
- `delimiter=...`: Soporte de delimitadores personalizados (como `\t` para TSV o `;` para dialectos regionales europeos y latinoamericanos).

#### Ejecución:
```bash
python examples/04_csv_examples.py
```

---

### 5. `fpdf` (fpdf2)
- **Tipo**: Librería externa (`pip install fpdf2`).
- **Archivo**: [`examples/05_fpdf_examples.py`](examples/05_fpdf_examples.py)
- **¿Qué es y para qué sirve?**: Herramienta simple y liviana para crear documentos PDF desde cero, ideal para recibos, certificados y reportes directos con control posicional de celdas.

#### Funciones Clave Demostradas:
- Herencia de clase `FPDF`: Personalización automática de métodos `header()` y `footer()`.
- `add_page()`, `set_font()`, `set_text_color()`, `set_draw_color()`: Configuración de lienzo, tipografías y paletas.
- `cell()` y `multi_cell()`: Creación de bloques de texto unilínea y párrafos justificados con ajuste automático.
- Creación de tablas estilizadas con bordes y celdas con color de relleno alternado.

#### Ejecución:
```bash
python examples/05_fpdf_examples.py
```

---

### 6. `reportlab`
- **Tipo**: Librería externa (`pip install reportlab`).
- **Archivo**: [`examples/06_reportlab_examples.py`](examples/06_reportlab_examples.py)
- **¿Qué es y para qué sirve?**: La biblioteca empresarial de referencia para generar documentos PDF profesionales complejos, con arquitectura de maquetación avanzada (Platypus: Page Layout and Typography Using Scripts).

#### Funciones Clave Demostradas:
- `SimpleDocTemplate`: Plantilla estructurada con márgenes y dimensiones de página estándar (`letter`, `A4`).
- `getSampleStyleSheet()`, `ParagraphStyle`: Definición de jerarquías tipográficas (títulos, subtítulos, cuerpo de texto).
- Etiquetas XML enriquecidas dentro de `Paragraph` (`<b>`, `<i>`, `<font color="...">`).
- `Table` y `TableStyle`: Tablas con formateo granular (alineación, colores de fondo por cuadrante o filas alternas, grillas).

#### Ejecución:
```bash
python examples/06_reportlab_examples.py
```

---

### 7. `NumPy`
- **Tipo**: Librería externa (`pip install numpy`).
- **Archivo**: [`examples/07_numpy_examples.py`](examples/07_numpy_examples.py)
- **¿Qué es y para qué sirve?**: Base del ecosistema científico en Python. Ofrece estructuras de arreglos homogéneos multidimensionales (`ndarray`) optimizadas en C y operaciones matemáticas vectorizadas de alta velocidad.

#### Funciones Clave Demostradas:
- Creación de matrices: `np.array()`, `np.zeros()`, `np.ones()`, `np.arange()`, `np.linspace()`.
- Inspección estructural: `.shape`, `.ndim`, `.dtype`, `.size`.
- Operaciones vectorizadas y **Broadcasting**: Aritmética eficiente sin bucles explícitos `for`.
- Indexación booleana: Filtrado condicional directo (`datos[datos > 50]`).
- Álgebra lineal y estadística: Multiplicación de matrices (`@`), determinante (`np.linalg.det()`), media, mediana, varianza y desviación estándar.

#### Ejecución:
```bash
python examples/07_numpy_examples.py
```

---

### 8. `Pandas`
- **Tipo**: Librería externa (`pip install pandas`).
- **Archivo**: [`examples/08_pandas_examples.py`](examples/08_pandas_examples.py)
- **¿Qué es y para qué sirve?**: Biblioteca líder para manipulación, limpieza y análisis exploratorio de datos heterogéneos y relacionales mediante `Series` y `DataFrame`.

#### Funciones Clave Demostradas:
- Estructuración de datos: Creación a partir de diccionarios y colecciones.
- Inspección inicial: `.describe()`, `.shape`, `.columns`.
- Filtrado y consultas: Filtros lógicos combinados (`(df['Salario'] > 4000) & (df['Departamento'] == 'Ventas')`).
- Limpieza y tratamiento de nulos: Detección con `.isna()` e imputación con `.fillna()`.
- Agrupaciones (`.groupby()`): Agregaciones agregadas multifunción (conteos, promedios, máximos).

#### Ejecución:
```bash
python examples/08_pandas_examples.py
```

---

### 9. `Matplotlib`
- **Tipo**: Librería externa (`pip install matplotlib`).
- **Archivo**: [`examples/09_matplotlib_examples.py`](examples/09_matplotlib_examples.py)
- **¿Qué es y para qué sirve?**: Biblioteca integral para crear visualizaciones estáticas, gráficos estadísticos y figuras con calidad de publicación científica.

#### Funciones Clave Demostradas:
- Subplots en cuadrícula: `plt.subplots(2, 2)` para organizar múltiples visualizaciones en un solo panel.
- Gráfico de Líneas (`ax.plot`): Seguimiento de series temporales con leyendas y marcadores.
- Gráfico de Barras (`ax.bar`): Comparación de métricas con etiquetas numéricas directas.
- Gráfico de Dispersión (`ax.scatter`): Relación y correlación entre dos variables numéricas.
- Histograma (`ax.hist`): Distribución de frecuencias continuas agrupadas en intervalos (*bins*).
- Exportación gráfica: Guardado en disco con alta resolución (`plt.savefig(..., dpi=150)`).

#### Ejecución:
```bash
python examples/09_matplotlib_examples.py
```

---

### 10. `Requests`
- **Tipo**: Librería externa (`pip install requests`).
- **Archivo**: [`examples/10_requests_examples.py`](examples/10_requests_examples.py)
- **¿Qué es y para qué sirve?**: La biblioteca estándar de facto para realizar peticiones HTTP amigables (*HTTP for Humans*), comunicarse con servicios web y consumir APIs REST.

#### Funciones Clave Demostradas:
- `requests.get()`: Peticiones de lectura con paso de query parameters (`params={...}`).
- `requests.post()`: Creación de recursos enviando cargas útiles JSON estructuradas (`json={...}`).
- Inspección de respuestas: Códigos de estado (`.status_code`), cabeceras (`.headers`) y deserialización automática (`.json()`).
- Manejo robusto de errores: `response.raise_for_status()`, captura de `Timeout`, `HTTPError` y `RequestException`.

#### Ejecución:
```bash
python examples/10_requests_examples.py
```

---

### 11. `Flask`
- **Tipo**: Librería externa (`pip install Flask`).
- **Archivo**: [`examples/11_flask_examples.py`](examples/11_flask_examples.py)
- **¿Qué es y para qué sirve?**: Microframework web ágil y modular para construir APIs RESTful, microservicios y aplicaciones web completas.

#### Funciones Clave Demostradas:
- Inicialización de la aplicación: `app = Flask(__name__)`.
- Enrutamiento y vistas: `@app.route("/")` para páginas HTML simples.
- Rutas dinámicas: `@app.route("/api/saludo/<nombre>")` para procesar variables en la URL.
- Endpoints RESTful: `@app.route("/api/tareas", methods=["GET", "POST"])` con lectura de `request.get_json()` y respuestas JSON mediante `jsonify()`.
- Manejador de errores personalizado: `@app.errorhandler(404)`.
- **Test Client Integrado**: Demostración que ejecuta pruebas unitarias en memoria (`app.test_client()`) sin necesidad de bloquear la terminal.
- Opción de servidor en vivo con `--servidor`.

#### Ejecución:
```bash
# Modo prueba en memoria (rápido):
python examples/11_flask_examples.py

# Modo servidor web activo (escuchando en http://127.0.0.1:5000):
python examples/11_flask_examples.py --servidor
```

---

### 12. `scikit-learn`
- **Tipo**: Librería externa (`pip install scikit-learn`).
- **Archivo**: [`examples/12_scikit_learn_examples.py`](examples/12_scikit_learn_examples.py)
- **¿Qué es y para qué sirve?**: Biblioteca fundamental para Machine Learning y Data Science en Python, con algoritmos de aprendizaje supervisado y no supervisado.

#### Funciones Clave Demostradas:
- **Clasificación Supervisada**:
  - Carga del dataset `Iris` y partición con `train_test_split(..., test_size=0.2)`.
  - Entrenamiento de un clasificador `RandomForestClassifier`.
  - Evaluación rigurosa con `accuracy_score` y reporte de métricas (`classification_report` con precisión, recall y F1-score).
- **Regresión Supervisada**:
  - Modelo de regresión lineal `LinearRegression`.
  - Coeficientes de recta, intercepto, cálculo de $R^2$ y error cuadrático medio (MSE).
- **Aprendizaje No Supervisado**:
  - Agrupamiento de muestras mediante `KMeans(n_clusters=3)` e inspección de centroides.

#### Ejecución:
```bash
python examples/12_scikit_learn_examples.py
```

---

## 🎮 Ejecutor Central (`main.py`)

Para comodidad del usuario o evaluador, el archivo [`main.py`](main.py) permite ejecutar los ejemplos desde un menú interactivo en consola o por argumentos:

```bash
# Menú interactivo:
python main.py

# Ejecutar TODOS los módulos en secuencia:
python main.py all

# Ejecutar un módulo específico (por número o nombre):
python main.py 1       # Ejecuta math
python main.py flask   # Ejecuta Flask
```

---

## 🌐 Cómo Subir este Proyecto a tu GitHub

Sigue estos sencillos pasos para publicar este repositorio en tu cuenta de GitHub:

### Paso 1: Crear un nuevo repositorio en GitHub
1. Ingresa a [github.com/new](https://github.com/new).
2. Nombre sugerido: `python-libraries-showcase` (o el nombre de tu preferencia).
3. Selecciona la opción **Public** (Público).
4. **No** selecciones "Add a README file" ni ".gitignore" (ya están creados en este proyecto).
5. Haz clic en **Create repository**.

### Paso 2: Vincular y subir desde tu terminal
En la raíz de este proyecto (`python-libraries-showcase`), ejecuta:

```bash
# 1. Asegurarte de que tus cambios estén confirmados localmente:
git add .
git commit -m "feat: ejemplos completos de 12 librerías en Python y documentación detallada"

# 2. Configurar la rama principal como 'main':
git branch -M main

# 3. Conectar tu repositorio remoto de GitHub (sustituye TU_USUARIO):
git remote add origin https://github.com/TU_USUARIO/python-libraries-showcase.git

# 4. Subir todos los archivos:
git push -u origin main
```

---

## 🔗 Liga del Repositorio

> [!NOTE]
> Coloca aquí la URL final de tu repositorio una vez subido a tu cuenta:
> **`https://github.com/TU_USUARIO/python-libraries-showcase`**
