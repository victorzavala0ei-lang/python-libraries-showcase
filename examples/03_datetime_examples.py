"""
Librería: datetime
Descripción: Manejo de fechas, horas y cálculos de días.
"""
from datetime import datetime, timedelta

print("=== EJEMPLO INTERACTIVO: DATETIME ===")

# Fecha y hora actual
ahora = datetime.now()
print(f"Fecha y hora actual: {ahora.strftime('%d/%m/%Y %H:%M:%S')}")

# Entrada de fecha por el usuario
fecha_str = input("\nIngresa una fecha en formato AAAA-MM-DD (ejemplo: 2000-05-15): ").strip()
if not fecha_str:
    fecha_str = "2000-05-15"

try:
    fecha_usuario = datetime.strptime(fecha_str, "%Y-%m-%d")
    print(f"Fecha convertida a objeto: {fecha_usuario.strftime('%A, %d de %B de %Y')}")
    
    # Calcular diferencia de días
    diferencia = ahora - fecha_usuario
    print(f"Días transcurridos desde esa fecha: {diferencia.days} días")
    
    # Sumar días
    dias_sumar = int(input("\n¿Cuántos días quieres sumarle a la fecha de hoy?: ") or "10")
    fecha_futura = ahora + timedelta(days=dias_sumar)
    print(f"Dentro de {dias_sumar} días será: {fecha_futura.strftime('%d/%m/%Y')}")

except ValueError:
    print("Formato de fecha inválido. Recuerda usar el formato AAAA-MM-DD.")
