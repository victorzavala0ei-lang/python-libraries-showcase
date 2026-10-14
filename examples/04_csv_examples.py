"""
Librería: csv
Descripción: Guardar y leer datos tabulares en formato CSV.
"""
import csv

print("=== EJEMPLO INTERACTIVO: CSV ===")

archivo_csv = "contactos.csv"

# Pedir datos al usuario
print("Vamos a guardar 2 contactos en un archivo CSV:")
contactos = []

for i in range(1, 3):
    print(f"\nContacto #{i}:")
    nombre = input("  Nombre: ") or f"Persona {i}"
    correo = input("  Correo: ") or f"persona{i}@correo.com"
    telefono = input("  Teléfono: ") or f"555-010{i}"
    contactos.append([nombre, correo, telefono])

# 1. Escribir en el archivo CSV
with open(archivo_csv, mode="w", newline="", encoding="utf-8") as f:
    escritor = csv.writer(f)
    escritor.writerow(["Nombre", "Correo", "Telefono"])  # Cabecera
    escritor.writerows(contactos)

print(f"\n Datos guardados con éxito en '{archivo_csv}'.")

# 2. Leer y mostrar el archivo CSV
print("\n--- Leyendo el archivo CSV guardado ---")
with open(archivo_csv, mode="r", encoding="utf-8") as f:
    lector = csv.reader(f)
    for fila in lector:
        print(f"| {fila[0]:<15} | {fila[1]:<25} | {fila[2]:<12} |")
