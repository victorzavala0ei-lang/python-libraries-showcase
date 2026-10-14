"""
Librería: numpy
Descripción: Operaciones estadísticas y matemáticas sobre arreglos numéricos.
"""
try:
    import numpy as np
except ImportError:
    print("[Error] La librería 'numpy' no está instalada. Ejecuta: pip install numpy")
    exit()

print("=== EJEMPLO INTERACTIVO: NUMPY ===")

# Entrada de números
entrada = input("Ingresa números separados por espacio (ejemplo: 10 25 40 55 70): ").strip()
if not entrada:
    entrada = "10 25 40 55 70"

# Crear arreglo NumPy
datos = np.array([float(x) for x in entrada.split()])
print(f"\nArreglo creado (numpy.ndarray): {datos}")

# Estadísticas básicas
print(f"Total de elementos:    {len(datos)}")
print(f"Suma total:            {np.sum(datos)}")
print(f"Promedio (media):      {np.mean(datos):.2f}")
print(f"Valor máximo:          {np.max(datos)}")
print(f"Valor mínimo:          {np.min(datos)}")
print(f"Desviación estándar:   {np.std(datos):.2f}")

# Multiplicar por un escalar
multiplicador = float(input("\n¿Por qué número deseas multiplicar todo el arreglo?: ") or "2")
print(f"Arreglo multiplicado por {multiplicador}: {datos * multiplicador}")
