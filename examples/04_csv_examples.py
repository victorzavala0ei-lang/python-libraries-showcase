"""
Ejemplos de la librería estándar 'csv' en Python.

El módulo 'csv' implementa clases para leer y escribir datos tabulares
en formato de valores separados por comas (CSV).
"""

import csv
import io
import os

def demostracion_escritura_y_lectura_estandar():
    print("=" * 60)
    print("1. ESCRITURA Y LECTURA ESTÁNDAR (csv.writer y csv.reader)")
    print("=" * 60)
    
    # Creamos un buffer en memoria para la demostración
    buffer = io.StringIO()
    
    # Escritura usando csv.writer
    escritor = csv.writer(buffer, delimiter=',', lineterminator='\n')
    cabecera = ["ID", "Producto", "Precio", "Stock"]
    filas = [
        [101, "Laptop Pro 14", 1299.99, 15],
        [102, "Mouse Inalámbrico", 25.50, 80],
        [103, "Teclado Mecánico", 89.90, 45],
        [104, "Monitor 4K 27\"", 349.00, 20]
    ]
    
    escritor.writerow(cabecera)
    escritor.writerows(filas)
    
    contenido_generado = buffer.getvalue()
    print("CSV Generado en memoria:")
    print(contenido_generado)
    
    # Lectura usando csv.reader
    buffer.seek(0)
    lector = csv.reader(buffer, delimiter=',')
    cabecera_leida = next(lector)
    print(f"Cabecera leída: {cabecera_leida}")
    
    print("Filas procesadas:")
    for num_fila, fila in enumerate(lector, start=1):
        print(f"  Fila {num_fila}: Producto='{fila[1]}', Precio=${fila[2]}")
    print()

def demostracion_dictwriter_y_dictreader():
    print("=" * 60)
    print("2. USO DE DICCIONARIOS (csv.DictWriter y csv.DictReader)")
    print("=" * 60)
    
    empleados = [
        {"id": 1, "nombre": "Ana Pérez", "puesto": "Data Scientist", "salario": 45000},
        {"id": 2, "nombre": "Carlos Gómez", "puesto": "Backend Developer", "salario": 42000},
        {"id": 3, "nombre": "Beatriz Ramos", "puesto": "DevOps Engineer", "salario": 48000},
        {"id": 4, "nombre": "David Silva", "puesto": "Frontend Developer", "salario": 39000}
    ]
    campos = ["id", "nombre", "puesto", "salario"]
    
    buffer = io.StringIO()
    escritor_dict = csv.DictWriter(buffer, fieldnames=campos, lineterminator='\n')
    
    # Escribir cabecera y filas basadas en diccionarios
    escritor_dict.writeheader()
    escritor_dict.writerows(empleados)
    
    # Lectura con DictReader
    buffer.seek(0)
    lector_dict = csv.DictReader(buffer)
    
    total_salarios = 0
    conteo = 0
    print("Lectura basada en llaves de diccionario:")
    for registro in lector_dict:
        salario = float(registro["salario"])
        total_salarios += salario
        conteo += 1
        print(f"  - {registro['nombre']} ({registro['puesto']}) -> ${salario:,.2f}")
    
    promedio = total_salarios / conteo if conteo else 0
    print(f"\nSalario promedio calculado: ${promedio:,.2f}")
    print()

def demostracion_delimitadores_y_dialectos():
    print("=" * 60)
    print("3. DELIMITADORES PERSONALIZADOS (Punto y coma / Tabulador)")
    print("=" * 60)
    
    # En muchos países europeos y de habla hispana, el CSV usa ';' para no confundir con decimales ','
    datos_tsv = "Pais\tCapital\tPoblacion_Millones\nEspaña\tMadrid\t47.4\nMéxico\tCDMX\t126.0\nColombia\tBogotá\t51.5\n"
    buffer = io.StringIO(datos_tsv)
    
    lector_tab = csv.reader(buffer, delimiter='\t')
    for fila in lector_tab:
        print(f"  Columna separada por TAB: {fila}")
    print()

def main():
    print("\n>>> DEMOSTRACIÓN DE LA LIBRERÍA 'csv' EN PYTHON <<<\n")
    demostracion_escritura_y_lectura_estandar()
    demostracion_dictwriter_y_dictreader()
    demostracion_delimitadores_y_dialectos()
    print("¡Demostración de 'csv' completada con éxito!\n")

if __name__ == "__main__":
    main()
