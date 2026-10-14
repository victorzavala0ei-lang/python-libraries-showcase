"""
Ejemplos de la librería 'numpy' para computación numérica y arreglos multidimensionales.

NumPy (Numerical Python) es la biblioteca fundamental para el cálculo científico en Python,
proporcionando estructuras de arreglos N-dimensionales de alto rendimiento y funciones matemáticas vectorizadas.

Instalación:
    pip install numpy
"""

import sys

try:
    import numpy as np
    NUMPY_INSTALADO = True
except ImportError:
    NUMPY_INSTALADO = False


def demostracion_creacion_arreglos():
    print("=" * 60)
    print("1. CREACIÓN E INSPECCIÓN DE ARREGLOS (NDARRAY)")
    print("=" * 60)
    
    # Arreglo 1D
    arr_1d = np.array([10, 20, 30, 40, 50], dtype=np.int32)
    print(f"Arreglo 1D:          {arr_1d}")
    print(f"  Forma (shape):     {arr_1d.shape}")
    print(f"  Dimensiones (ndim):{arr_1d.ndim}")
    print(f"  Tipo de dato:      {arr_1d.dtype}")
    
    # Arreglo 2D (Matriz 3x3)
    matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"\nMatriz 2D (3x3):\n{matriz}")
    
    # Métodos generadores
    ceros = np.zeros((2, 3))
    unos = np.ones((2, 2))
    rango = np.arange(0, 20, 5) # [0, 5, 10, 15]
    lineal = np.linspace(0, 1, 5) # 5 puntos equiespaciados entre 0 y 1
    
    print(f"\nnp.zeros((2,3)):\n{ceros}")
    print(f"np.arange(0, 20, 5): {rango}")
    print(f"np.linspace(0, 1, 5): {lineal}")
    print()

def demostracion_operaciones_vectorizadas_y_broadcasting():
    print("=" * 60)
    print("2. OPERACIONES VECTORIZADAS Y DIFUSIÓN (BROADCASTING)")
    print("=" * 60)
    
    a = np.array([1, 2, 3, 4])
    b = np.array([10, 20, 30, 40])
    
    print(f"Vector a:          {a}")
    print(f"Vector b:          {b}")
    print(f"Suma (a + b):      {a + b}")
    print(f"Multiplicación elemento a elemento (a * b): {a * b}")
    print(f"Escalar (a * 2):   {a * 2}  (Broadcasting de un escalar)")
    
    # Broadcasting entre matriz y vector
    matriz = np.ones((3, 3)) * 10
    fila_sumar = np.array([1, 2, 3])
    print(f"\nMatriz 3x3 base:\n{matriz}")
    print(f"Sumar vector [1, 2, 3] a cada fila:\n{matriz + fila_sumar}")
    print()

def demostracion_indexacion_y_filtrado_booleano():
    print("=" * 60)
    print("3. INDEXACIÓN, SLICING Y MÁSCARAS BOOLEANAS")
    print("=" * 60)
    
    datos = np.array([12, 45, 78, 23, 89, 34, 91, 56, 18, 67])
    print(f"Datos originales:                {datos}")
    
    # Slicing
    print(f"Elementos del índice 2 al 6:     {datos[2:7]}")
    
    # Máscara booleana
    mayores_50 = datos > 50
    print(f"Máscara booleana (> 50):         {mayores_50}")
    print(f"Elementos filtrados (> 50):      {datos[mayores_50]}")
    
    # Modificación condicional
    copia = datos.copy()
    copia[copia < 30] = 0
    print(f"Reemplazando valores < 30 por 0: {copia}")
    print()

def demostracion_algebra_lineal_y_estadisticas():
    print("=" * 60)
    print("4. ÁLGEBRA LINEAL Y ESTADÍSTICA")
    print("=" * 60)
    
    m1 = np.array([[1, 2], [3, 4]])
    m2 = np.array([[2, 0], [1, 2]])
    
    producto_matricial = m1 @ m2 # o np.dot(m1, m2)
    print(f"Matriz A:\n{m1}")
    print(f"Matriz B:\n{m2}")
    print(f"Producto Matricial (A @ B):\n{producto_matricial}")
    print(f"Transpuesta de A:\n{m1.T}")
    print(f"Determinante de A: {np.linalg.det(m1):.2f}")
    
    # Estadísticas
    valores = np.array([10, 25, 40, 55, 70, 85, 100])
    print(f"\nValores para estadística: {valores}")
    print(f"  Media (mean):           {np.mean(valores):.2f}")
    print(f"  Mediana (median):       {np.median(valores):.2f}")
    print(f"  Desviación Estándar:    {np.std(valores):.2f}")
    print(f"  Varianza:               {np.var(valores):.2f}")
    print(f"  Suma acumulada (cumsum):{np.cumsum(valores)}")
    print(f"  Índice del valor máximo: {np.argmax(valores)} (valor: {np.max(valores)})")
    print()

def main():
    print("\n>>> DEMOSTRACIÓN DE LA LIBRERÍA 'NumPy' EN PYTHON <<<\n")
    if not NUMPY_INSTALADO:
        print("[AVISO] La librería 'numpy' no está instalada.")
        print("Para instalarla ejecuta: pip install numpy\n")
        return
    demostracion_creacion_arreglos()
    demostracion_operaciones_vectorizadas_y_broadcasting()
    demostracion_indexacion_y_filtrado_booleano()
    demostracion_algebra_lineal_y_estadisticas()
    print("¡Demostración de 'numpy' completada con éxito!\n")

if __name__ == "__main__":
    main()
