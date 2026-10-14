"""
Ejemplos de la librería 'scikit-learn' (sklearn) para Machine Learning en Python.

scikit-learn es la biblioteca líder para aprendizaje automático en Python,
incluyendo algoritmos de clasificación, regresión, agrupamiento (clustering) y métricas.

Instalación:
    pip install scikit-learn
"""

import sys

try:
    from sklearn.datasets import load_iris, make_regression
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.linear_model import LinearRegression
    from sklearn.cluster import KMeans
    from sklearn.metrics import accuracy_score, classification_report, mean_squared_error, r2_score
    SKLEARN_INSTALADO = True
except ImportError:
    SKLEARN_INSTALADO = False


def demostracion_clasificacion_supervisada():
    print("=" * 60)
    print("1. CLASIFICACIÓN SUPERVISADA (RANDOM FOREST CON DATASET IRIS)")
    print("=" * 60)
    
    # Cargar dataset clásico de Iris (3 clases de flores)
    iris = load_iris()
    X, y = iris.data, iris.target
    nombres_clases = iris.target_names
    nombres_caracteristicas = iris.feature_names
    
    print(f"Dimensiones del dataset Iris:  {X.shape} (150 muestras, 4 características)")
    print(f"Características:               {nombres_caracteristicas}")
    print(f"Clases a predecir:             {list(nombres_clases)}")
    
    # Dividir datos en entrenamiento (80%) y prueba (20%)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    print(f"Muestras de entrenamiento:     {len(X_train)}")
    print(f"Muestras de prueba:            {len(X_test)}")
    
    # Entrenar un modelo de Bosques Aleatorios
    modelo_rf = RandomForestClassifier(n_estimators=50, random_state=42)
    modelo_rf.fit(X_train, y_train)
    
    # Realizar predicciones sobre el conjunto de prueba
    predicciones = modelo_rf.predict(X_test)
    exactitud = accuracy_score(y_test, predicciones)
    
    print(f"\nExactitud del modelo (Accuracy): {exactitud * 100:.2f}%")
    print("\nReporte de Clasificación:")
    print(classification_report(y_test, predicciones, target_names=nombres_clases))
    print()

def demostracion_regresion_lineal():
    print("=" * 60)
    print("2. REGRESIÓN SUPERVISADA (LINEAR REGRESSION)")
    print("=" * 60)
    
    # Generar datos sintéticos para regresión
    X, y = make_regression(n_samples=100, n_features=1, noise=15.0, random_state=42)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Entrenar regresión lineal
    regresor = LinearRegression()
    regresor.fit(X_train, y_train)
    
    predicciones_y = regresor.predict(X_test)
    mse = mean_squared_error(y_test, predicciones_y)
    r2 = r2_score(y_test, predicciones_y)
    
    print(f"Pendiente (Coeficiente):           {regresor.coef_[0]:.4f}")
    print(f"Intercepto (Término independiente):{regresor.intercept_:.4f}")
    print(f"Error Cuadrático Medio (MSE):       {mse:.4f}")
    print(f"Coeficiente de Determinación (R²):  {r2:.4f}")
    print()

def demostracion_clustering_no_supervisado():
    print("=" * 60)
    print("3. APRENDIZAJE NO SUPERVISADO (AGRUPAMIENTO K-MEANS)")
    print("=" * 60)
    
    # Usar características de Iris sin etiquetas para agrupar en 3 clusters
    iris = load_iris()
    X = iris.data
    
    kmeans = KMeans(n_clusters=3, random_state=42, n_init='auto')
    clusters = kmeans.fit_predict(X)
    
    print(f"Número de clusters definidos:       3")
    print(f"Centroides de los clusters (dimensiones 3x4):")
    for idx, centroide in enumerate(kmeans.cluster_centers_):
        valores_fmt = [f"{v:.2f}" for v in centroide]
        print(f"  Cluster {idx}: {valores_fmt}")
    print(f"Inercia del modelo (suma de distancias al cuadrado): {kmeans.inertia_:.2f}")
    print()

def main():
    print("\n>>> DEMOSTRACIÓN DE LA LIBRERÍA 'scikit-learn' EN PYTHON <<<\n")
    if not SKLEARN_INSTALADO:
        print("[AVISO] La librería 'scikit-learn' no está instalada.")
        print("Para instalarla ejecuta: pip install scikit-learn\n")
        return
    demostracion_clasificacion_supervisada()
    demostracion_regresion_lineal()
    demostracion_clustering_no_supervisado()
    print("¡Demostración de 'scikit-learn' completada con éxito!\n")

if __name__ == "__main__":
    main()
