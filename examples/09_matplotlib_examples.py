"""
Ejemplos de la librería 'matplotlib' para visualización y trazado de gráficos en Python.

Matplotlib es una biblioteca integral para crear visualizaciones estáticas,
animadas e interactivas en Python (especialmente mediante su módulo pyplot).

Instalación:
    pip install matplotlib
"""

import os
import sys

try:
    import matplotlib
    # Usar backend 'Agg' que no requiere servidor gráfico/pantalla GUI interactiva
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    MATPLOTLIB_INSTALADO = True
except ImportError:
    MATPLOTLIB_INSTALADO = False


def generar_graficos_demostracion(nombre_archivo="graficos_demostracion.png"):
    print("=" * 60)
    print("DEMOSTRACIÓN DE LA LIBRERÍA 'matplotlib'")
    print("=" * 60)
    
    if not MATPLOTLIB_INSTALADO:
        print("[AVISO] La librería 'matplotlib' no está instalada.")
        print("Para instalarla ejecuta: pip install matplotlib")
        print("A continuación se muestra un ejemplo básico de uso:")
        print("-" * 60)
        print("""
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 9, 16, 25]
plt.plot(x, y, marker='o', color='royalblue')
plt.title("Gráfico Cuadrático")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("grafico.png")
        """)
        return False

    # Crear una figura con una cuadrícula de 2x2 subgráficos
    fig, axes = plt.subplots(2, 2, figsize=(12, 9))
    fig.suptitle("Visualizaciones Muestrales con Matplotlib", fontsize=16, fontweight='bold', color='#1E293B')

    # 1. Gráfico de Líneas (Tendencia Temporal)
    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun']
    ventas_2025 = [12, 19, 15, 25, 22, 30]
    ventas_2026 = [15, 24, 21, 31, 29, 38]
    
    ax1 = axes[0, 0]
    ax1.plot(meses, ventas_2025, marker='o', linestyle='--', color='#64748B', label='2025', linewidth=2)
    ax1.plot(meses, ventas_2026, marker='s', linestyle='-', color='#2563EB', label='2026', linewidth=2)
    ax1.set_title("1. Tendencia de Ventas (Líneas)", fontweight='bold')
    ax1.set_ylabel("Ventas (Miles de USD)")
    ax1.grid(True, linestyle=':', alpha=0.6)
    ax1.legend()

    # 2. Gráfico de Barras (Comparativa de Categorías)
    categorias = ['Python', 'JS', 'C++', 'Java', 'Rust']
    popularidad = [85, 78, 62, 70, 55]
    colores = ['#3B82F6', '#F59E0B', '#EF4444', '#10B981', '#8B5CF6']
    
    ax2 = axes[0, 1]
    barras = ax2.bar(categorias, popularidad, color=colores, edgecolor='black', alpha=0.85)
    ax2.set_title("2. Adopción de Lenguajes (Barras)", fontweight='bold')
    ax2.set_ylabel("Puntaje de Preferencia")
    # Agregar etiquetas sobre las barras
    for barra in barras:
        yval = barra.get_height()
        ax2.text(barra.get_x() + barra.get_width()/2, yval + 1, f"{int(yval)}%", ha='center', va='bottom', fontsize=9)
    ax2.set_ylim(0, 100)
    ax2.grid(axis='y', linestyle=':', alpha=0.6)

    # 3. Gráfico de Dispersión (Scatter Plot)
    horas_estudio = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    calificaciones = [52, 58, 65, 68, 74, 80, 83, 89, 94, 98]
    
    ax3 = axes[1, 0]
    ax3.scatter(horas_estudio, calificaciones, color='#DC2626', s=70, alpha=0.8, edgecolors='black')
    ax3.set_title("3. Horas de Estudio vs Calificación (Dispersión)", fontweight='bold')
    ax3.set_xlabel("Horas Semanales Dedicadas")
    ax3.set_ylabel("Calificación Obtenida")
    ax3.grid(True, linestyle=':', alpha=0.6)

    # 4. Histograma (Distribución de Frecuencias)
    edades = [22, 23, 24, 25, 25, 26, 26, 26, 27, 28, 29, 30, 31, 31, 32, 35, 38, 40, 42, 45]
    
    ax4 = axes[1, 1]
    ax4.hist(edades, bins=6, color='#10B981', edgecolor='black', alpha=0.7)
    ax4.set_title("4. Distribución de Edades (Histograma)", fontweight='bold')
    ax4.set_xlabel("Rango de Edad")
    ax4.set_ylabel("Frecuencia (Personas)")
    ax4.grid(axis='y', linestyle=':', alpha=0.6)

    # Ajuste de diseño y exportación
    plt.tight_layout()
    ruta_salida = os.path.join(os.path.dirname(__file__), nombre_archivo)
    plt.savefig(ruta_salida, dpi=150)
    plt.close()
    
    print(f" Figura gráfica generada exitosamente en: {ruta_salida}")
    return True


def main():
    generar_graficos_demostracion()


if __name__ == "__main__":
    main()
