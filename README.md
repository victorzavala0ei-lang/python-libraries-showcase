# 🚀 Python Libraries Showcase (Ejemplos Sencillos e Interactivos)

Colección de códigos en **Python** claros, concisos (aproximadamente 25 a 35 líneas cada uno) y **100% interactivos por teclado (`input()`)**, diseñados para aprender de forma práctica y directa las **12 librerías esenciales**.

---

## 📋 Lista de Librerías y Ejemplos

Cada archivo se encuentra en la carpeta [`examples/`](examples/) y pide datos por consola:

| # | Librería | Archivo | ¿Qué pide por teclado? | ¿Qué hace? |
|---|---|---|---|---|
| 1 | **math** | [`01_math_examples.py`](examples/01_math_examples.py) | Un número y un ángulo en grados | Calcula raíz cuadrada, redondeos (`ceil`/`floor`), factorial y seno/coseno. |
| 2 | **random** | [`02_random_examples.py`](examples/02_random_examples.py) | Rango mínimo/máximo y opciones separadas por coma | Genera enteros y decimales al azar, elige un ganador (`choice`) y mezcla la lista (`shuffle`). |
| 3 | **datetime** | [`03_datetime_examples.py`](examples/03_datetime_examples.py) | Una fecha (AAAA-MM-DD) y días a sumar | Muestra fecha/hora actual, calcula días transcurridos y proyecta fechas futuras con `timedelta`. |
| 4 | **csv** | [`04_csv_examples.py`](examples/04_csv_examples.py) | Nombre, correo y teléfono de contactos | Guarda los datos en `contactos.csv` con `csv.writer` y los lee de vuelta con `csv.reader`. |
| 5 | **fpdf** | [`05_fpdf_examples.py`](examples/05_fpdf_examples.py) | Título, autor y un mensaje | Crea un archivo PDF con formato limpio y lo guarda como `mi_documento_fpdf.pdf`. |
| 6 | **reportlab** | [`06_reportlab_examples.py`](examples/06_reportlab_examples.py) | Título y contenido del reporte | Genera un PDF estructurado con estilos y lo guarda como `reporte_reportlab.pdf`. |
| 7 | **NumPy** | [`07_numpy_examples.py`](examples/07_numpy_examples.py) | Números separados por espacio y un multiplicador | Crea un `ndarray`, calcula suma, promedio, máximo, desviación estándar y multiplica el arreglo. |
| 8 | **Pandas** | [`08_pandas_examples.py`](examples/08_pandas_examples.py) | 3 productos con sus precios y un límite de filtro | Construye un `DataFrame`, muestra estadísticas (`mean`/`max`) y filtra filas según el precio. |
| 9 | **Matplotlib** | [`09_matplotlib_examples.py`](examples/09_matplotlib_examples.py) | Título, nombres de categorías y valores | Dibuja un gráfico de barras personalizado y lo guarda como `mi_grafico.png`. |
| 10 | **Requests** | [`10_requests_examples.py`](examples/10_requests_examples.py) | Un ID de usuario (1 al 10) | Consulta una API pública REST (`jsonplaceholder`) y muestra los datos en formato JSON. |
| 11 | **Flask** | [`11_flask_examples.py`](examples/11_flask_examples.py) | Tu nombre y un mensaje de bienvenida | Levanta una app web personalizable con rutas HTML y API JSON (permite prueba rápida o servidor en vivo). |
| 12 | **scikit-learn** | [`12_scikit_learn_examples.py`](examples/12_scikit_learn_examples.py) | Horas de estudio que planeas dedicar | Entrena un modelo de Machine Learning (`LinearRegression`) y predice tu calificación de examen. |

---

## ⚙️ Instalación de Dependencias

Las primeras 4 librerías (`math`, `random`, `datetime`, `csv`) vienen integradas por defecto en Python.

Para instalar las librerías externas restantes, ejecuta en tu terminal:

```bash
pip install -r requirements.txt
```

---

## 🎮 Cómo Ejecutar los Códigos

### Opción 1: Menú interactivo
Ejecuta el menú central para elegir qué ejemplo quieres probar:
```bash
python3 main.py
```

### Opción 2: Ejecutar un script directamente
```bash
python3 examples/01_math_examples.py
python3 examples/02_random_examples.py
python3 examples/03_datetime_examples.py
python3 examples/04_csv_examples.py
python3 examples/11_flask_examples.py
```
*(O simplemente ábrelo en VS Code y haz clic en el botón **Play ▶️**).*

---

## 🌐 Subir a GitHub

```bash
git add .
git commit -m "feat: ejemplos interactivos sencillos con entrada por teclado"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/python-libraries-showcase.git
git push -u origin main
```
