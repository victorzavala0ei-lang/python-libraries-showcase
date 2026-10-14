"""
Librería: random
Descripción: Generación de números aleatorios y selección en listas.
"""
import random

print("=== EJEMPLO INTERACTIVO: RANDOM ===")

# 1. Rango de números
min_val = int(input("Ingresa el valor mínimo (ejemplo: 1): ") or "1")
max_val = int(input("Ingresa el valor máximo (ejemplo: 100): ") or "100")

numero_azar = random.randint(min_val, max_val)
decimal_azar = random.uniform(min_val, max_val)
print(f"\nNúmero entero aleatorio entre {min_val} y {max_val}: {numero_azar}")
print(f"Número decimal aleatorio: {decimal_azar:.2f}")

# 2. Selección en lista
items_input = input("\nIngresa opciones separadas por coma (ejemplo: Pizza, Tacos, Hamburguesa): ").strip()
if not items_input:
    items_input = "Pizza, Tacos, Hamburguesa"

opciones = [item.strip() for item in items_input.split(",")]
ganador = random.choice(opciones)
print(f"Opción elegida al azar (choice): {ganador}")

# 3. Barajar lista
random.shuffle(opciones)
print(f"Lista desordenada al azar (shuffle): {opciones}")
