"""
Librería: math
Descripción: Operaciones matemáticas con entrada por teclado.
"""
import math

print("=== EJEMPLO INTERACTIVO: MATH ===")

# Entrada de datos
num_texto = input("Ingresa un número (ejemplo: 16.7): ").strip()
num = float(num_texto) if num_texto else 16.7

angulo_texto = input("Ingresa un ángulo en grados (ejemplo: 45): ").strip()
grados = float(angulo_texto) if angulo_texto else 45.0

# Operaciones
print("\n--- Resultados ---")
print(f"Número ingresado:            {num}")
print(f"Raíz cuadrada (sqrt):        {math.sqrt(abs(num)):.4f}")
print(f"Redondeo hacia arriba (ceil):{math.ceil(num)}")
print(f"Redondeo hacia abajo (floor):{math.floor(num)}")
print(f"Valor absoluto (fabs):       {math.fabs(num)}")

# Factorial (usando la parte entera positiva)
entero = int(abs(num))
if entero <= 20:
    print(f"Factorial de {entero}:          {math.factorial(entero)}")

# Trigonometría
radianes = math.radians(grados)
print(f"\nPara el ángulo de {grados}° ({radianes:.4f} rad):")
print(f"Seno:                        {math.sin(radianes):.4f}")
print(f"Coseno:                      {math.cos(radianes):.4f}")
print(f"Constante Pi:                {math.pi:.6f}")
