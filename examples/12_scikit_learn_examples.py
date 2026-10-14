"""
Librería: scikit-learn
Descripción: Modelo básico de Machine Learning (Regresión Lineal) para predecir una calificación.
"""
try:
    from sklearn.linear_model import LinearRegression
    import numpy as np
except ImportError:
    print("[Error] La librería 'scikit-learn' no está instalada. Ejecuta: pip install scikit-learn numpy")
    exit()

print("=== EJEMPLO INTERACTIVO: SCIKIT-LEARN ===")

# Datos históricos de entrenamiento: [Horas de estudio] -> Calificación obtenida (0 a 100)
X_entrenamiento = np.array([[1], [2], [3], [4], [5], [6], [8]])
y_calificaciones = np.array([50, 60, 68, 77, 85, 92, 98])

# 1. Crear y entrenar el modelo de Regresión Lineal
modelo = LinearRegression()
modelo.fit(X_entrenamiento, y_calificaciones)

print("El modelo de Inteligencia Artificial ha aprendido los datos de estudio:")
for h, c in zip(X_entrenamiento.flatten(), y_calificaciones):
    print(f"  {h} horas estudiadas -> Calificación: {c}")

# 2. Entrada del usuario para predecir
horas_input = input("\nIngresa cuántas horas planeas estudiar (ejemplo: 7): ").strip() or "7"
horas_usuario = float(horas_input)

# 3. Predicción
prediccion = modelo.predict([[horas_usuario]])[0]
calificacion_final = min(100.0, max(0.0, prediccion))  # Limitar entre 0 y 100

print(f"\n--- Resultado de la Predicción con scikit-learn ---")
print(f"Si estudias {horas_usuario} horas, tu calificación estimada es: {calificacion_final:.1f} / 100")
print(f"Ecuación del modelo: Calificación = ({modelo.coef_[0]:.2f} * Horas) + {modelo.intercept_:.2f}")
