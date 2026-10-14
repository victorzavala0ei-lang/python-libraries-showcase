"""
Librería: pandas
Descripción: Creación y filtrado de tablas estructuradas (DataFrames).
"""
try:
    import pandas as pd
except ImportError:
    print("[Error] La librería 'pandas' no está instalada. Ejecuta: pip install pandas")
    exit()

print("=== EJEMPLO INTERACTIVO: PANDAS ===")

print("Vamos a registrar 3 productos y sus precios:")
productos = []
precios = []

for i in range(1, 4):
    prod = input(f"Producto {i}: ").strip() or f"Producto_{i}"
    precio = float(input(f"Precio de {prod}: ") or f"{i * 15.5}")
    productos.append(prod)
    precios.append(precio)

# Crear DataFrame
df = pd.DataFrame({
    "Producto": productos,
    "Precio": precios
})

print("\n--- DataFrame generado ---")
print(df)

# Cálculos con Pandas
print(f"\nPrecio promedio: ${df['Precio'].mean():.2f}")
print(f"Producto más costoso: ${df['Precio'].max():.2f}")

# Filtrado interactivo
limite = float(input("\nFiltrar productos con precio mayor a: ") or "20")
filtrados = df[df["Precio"] > limite]
print(f"\n--- Productos con precio > ${limite} ---")
print(filtrados if not filtrados.empty else "No hay productos que cumplan la condición.")
