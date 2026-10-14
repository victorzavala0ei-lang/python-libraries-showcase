"""
Script principal (Menu / Runner) para ejecutar los ejemplos de las librerías de Python.

Permite ejecutar demostraciones individuales o todas en secuencia.
"""

import os
import sys
import subprocess

MODULOS = [
    ("1", "Math", "01_math_examples.py"),
    ("2", "Random", "02_random_examples.py"),
    ("3", "datetime", "03_datetime_examples.py"),
    ("4", "csv", "04_csv_examples.py"),
    ("5", "fpdf (fpdf2)", "05_fpdf_examples.py"),
    ("6", "reportlab", "06_reportlab_examples.py"),
    ("7", "NumPy", "07_numpy_examples.py"),
    ("8", "Pandas", "08_pandas_examples.py"),
    ("9", "Matplotlib", "09_matplotlib_examples.py"),
    ("10", "Requests", "10_requests_examples.py"),
    ("11", "Flask", "11_flask_examples.py"),
    ("12", "scikit-learn", "12_scikit_learn_examples.py"),
]

DIRECTORIO_EJEMPLOS = os.path.join(os.path.dirname(__file__), "examples")


def ejecutar_script(archivo):
    ruta = os.path.join(DIRECTORIO_EJEMPLOS, archivo)
    print("\n" + "#" * 70)
    print(f"# Ejecutando: {archivo}")
    print("#" * 70 + "\n")
    resultado = subprocess.run([sys.executable, ruta])
    return resultado.returncode


def mostrar_menu():
    print("\n" + "=" * 60)
    print("      PYTHON LIBRARIES SHOWCASE - MENÚ PRINCIPAL")
    print("=" * 60)
    for num, nombre, archivo in MODULOS:
        print(f"  [{num:>2}] {nombre:<20} ({archivo})")
    print("  [A ] Ejecutar TODOS los módulos")
    print("  [0 ] Salir")
    print("=" * 60)


def main():
    if len(sys.argv) > 1:
        param = sys.argv[1].lower()
        if param in ["all", "todos", "a"]:
            for _, _, archivo in MODULOS:
                ejecutar_script(archivo)
            return
        for num, _, archivo in MODULOS:
            if param == num or param in archivo.lower():
                ejecutar_script(archivo)
                return
        print(f"No se reconoció la opción '{sys.argv[1]}'.")
        return

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "0":
            print("¡Hasta luego!")
            break
        elif opcion.upper() == "A":
            for _, _, archivo in MODULOS:
                ejecutar_script(archivo)
            break
        else:
            encontrado = False
            for num, _, archivo in MODULOS:
                if opcion == num:
                    ejecutar_script(archivo)
                    encontrado = True
                    break
            if not encontrado:
                print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
