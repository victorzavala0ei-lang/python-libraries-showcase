"""
Librería: matplotlib
Descripción: Creación de un gráfico de barras a partir de datos ingresados.
"""
try:
    import matplotlib
    matplotlib.use('Agg')  # Para guardar sin requerir ventana gráfica
    import matplotlib.pyplot as plt
except ImportError:
    print("[Error] La librería 'matplotlib' no está instalada. Ejecuta: pip install matplotlib")
    exit()

print("=== EJEMPLO INTERACTIVO: MATPLOTLIB ===")

# Entrada de datos
titulo = input("Título del gráfico (ejemplo: Ventas del Mes): ").strip() or "Ventas del Mes"
etiquetas_input = input("Ingresa 3 o 4 categorías separadas por coma (ejemplo: Ene, Feb, Mar): ").strip() or "Ene, Feb, Mar"
valores_input = input("Ingresa sus valores separados por coma (ejemplo: 120, 250, 180): ").strip() or "120, 250, 180"

categorias = [c.strip() for c in etiquetas_input.split(",")]
valores = [float(v.strip()) for v in valores_input.split(",")]

# Crear gráfico de barras
plt.figure(figsize=(7, 4))
plt.bar(categorias, valores, color="royalblue", edgecolor="black")
plt.title(titulo, fontsize=14, fontweight="bold")
plt.xlabel("Categorías")
plt.ylabel("Valores")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Guardar imagen
nombre_archivo = "mi_grafico.png"
plt.savefig(nombre_archivo, dpi=120)
plt.close()

print(f"\n ¡Gráfica guardada con éxito como '{nombre_archivo}'!")
