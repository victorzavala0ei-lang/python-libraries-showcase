"""
Ejemplos de la librería 'pandas' para análisis y manipulación de datos.

Pandas proporciona estructuras de datos rápidas y flexibles (Series y DataFrames)
diseñadas para trabajar con datos estructurados y relacionales de forma intuitiva.

Instalación:
    pip install pandas
"""

import sys

try:
    import pandas as pd
    import numpy as np
    PANDAS_INSTALADO = True
except ImportError:
    PANDAS_INSTALADO = False


def demostracion_series_y_dataframe():
    print("=" * 60)
    print("1. CREACIÓN DE SERIES Y DATAFRAMES")
    print("=" * 60)
    
    # Serie de Pandas (1D etiquetada)
    poblacion = pd.Series([126.0, 51.5, 47.4, 45.8], index=["México", "Colombia", "España", "Argentina"], name="Poblacion_M")
    print("Serie de Población (en millones):")
    print(poblacion)
    print()
    
    # DataFrame (2D tabla estructurada)
    datos = {
        "Nombre": ["Laura", "Marcos", "Sofía", "Diego", "Valentina", "Andrés"],
        "Departamento": ["Ventas", "TI", "Ventas", "Marketing", "TI", "Marketing"],
        "Edad": [28, 34, 29, 41, 26, 38],
        "Salario": [3200.0, 4800.0, 3400.0, 3900.0, 4500.0, 4100.0],
        "Calificacion": [4.8, 4.2, 4.9, 3.8, 4.6, 4.1]
    }
    df = pd.DataFrame(datos)
    print("DataFrame de Empleados:")
    print(df)
    return df

def demostracion_inspeccion_y_filtrado(df):
    print("=" * 60)
    print("2. INSPECCIÓN Y FILTRADO DE DATOS")
    print("=" * 60)
    
    print("Dimensiones (filas, columnas):", df.shape)
    print("Nombres de columnas:", list(df.columns))
    print("\nResumen Estadístico Numérico (.describe()):")
    print(df.describe())
    
    # Filtrado booleano: Empleados con Salario > 4000
    altos_ingresos = df[df["Salario"] > 4000]
    print("\nEmpleados con Salario > $4,000:")
    print(altos_ingresos[["Nombre", "Departamento", "Salario"]])
    
    # Filtrado combinado con operadores lógicos (&, |)
    ventas_destacadas = df[(df["Departamento"] == "Ventas") & (df["Calificacion"] >= 4.8)]
    print("\nVentas con Calificación >= 4.8:")
    print(ventas_destacadas)
    print()

def demostracion_transformacion_y_nulos():
    print("=" * 60)
    print("3. MUTACIÓN DE COLUMNAS Y MANEJO DE VALORES FALTANTES (NaN)")
    print("=" * 60)
    
    datos_con_nulos = {
        "Producto": ["Laptop", "Teclado", "Mouse", "Monitor", "Webcam"],
        "Precio": [1200.0, 45.0, 25.0, np.nan, 75.0],
        "Stock": [10, np.nan, 50, 8, 20]
    }
    df_tienda = pd.DataFrame(datos_con_nulos)
    print("Datos originales con valores nulos:")
    print(df_tienda)
    
    print("\n¿Dónde hay valores nulos? (.isna()):")
    print(df_tienda.isna())
    
    # Relleno de valores nulos (fillna)
    precio_promedio = df_tienda["Precio"].mean()
    df_relleno = df_tienda.copy()
    df_relleno["Precio"] = df_relleno["Precio"].fillna(precio_promedio)
    df_relleno["Stock"] = df_relleno["Stock"].fillna(0)
    
    # Creación de nueva columna calculada
    df_relleno["Valor_Inventario"] = df_relleno["Precio"] * df_relleno["Stock"]
    print("\nDataFrame con nulos imputados y nueva columna 'Valor_Inventario':")
    print(df_relleno)
    print()

def demostracion_agrupacion_groupby(df):
    print("=" * 60)
    print("4. AGRUPACIÓN Y AGREGACIÓN (.groupby())")
    print("=" * 60)
    
    agrupado = df.groupby("Departamento").agg(
        Total_Empleados=("Nombre", "count"),
        Salario_Promedio=("Salario", "mean"),
        Salario_Maximo=("Salario", "max"),
        Calificacion_Promedio=("Calificacion", "mean")
    ).reset_index()
    
    print("Métricas agregadas por Departamento:")
    print(agrupado.to_string(index=False))
    print()

def main():
    print("\n>>> DEMOSTRACIÓN DE LA LIBRERÍA 'Pandas' EN PYTHON <<<\n")
    if not PANDAS_INSTALADO:
        print("[AVISO] La librería 'pandas' no está instalada.")
        print("Para instalarla ejecuta: pip install pandas\n")
        return
    df = demostracion_series_y_dataframe()
    demostracion_inspeccion_y_filtrado(df)
    demostracion_transformacion_y_nulos()
    demostracion_agrupacion_groupby(df)
    print("¡Demostración de 'pandas' completada con éxito!\n")

if __name__ == "__main__":
    main()
