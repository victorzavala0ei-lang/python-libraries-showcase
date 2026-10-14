"""
Ejemplos de la librería estándar 'datetime' en Python.

La librería 'datetime' suministra clases para manipular fechas y horas.
Permite realizar operaciones aritméticas con fechas, formateo, análisis sintáctico
y manejo de zonas horarias.
"""

from datetime import date, time, datetime, timedelta, timezone

def demostracion_fechas_y_horas_basicas():
    print("=" * 60)
    print("1. FECHA Y HORA ACTUAL")
    print("=" * 60)
    hoy = date.today()
    ahora = datetime.now()
    
    print(f"Fecha de hoy (date.today()):       {hoy}")
    print(f"  Año: {hoy.year}, Mes: {hoy.month}, Día: {hoy.day}")
    print(f"Fecha y hora actual:               {ahora}")
    print(f"  Hora: {ahora.hour}, Minuto: {ahora.minute}, Segundo: {ahora.second}, Microsegundo: {ahora.microsecond}")
    
    hora_especifica = time(14, 30, 45)
    print(f"Objeto time específico:            {hora_especifica}")
    print()

def demostracion_formateo_y_parsing():
    print("=" * 60)
    print("2. FORMATEO (strftime) Y PARSING (strptime)")
    print("=" * 60)
    ahora = datetime.now()
    
    # strftime: convierte un datetime a texto con un formato definido
    formato_humano = ahora.strftime("%d/%m/%Y %I:%M:%S %p")
    formato_iso = ahora.strftime("%Y-%m-%d %H:%M:%S")
    formato_texto = ahora.strftime("%A, %d de %B de %Y")
    
    print(f"Formato DD/MM/AAAA 12h:            {formato_humano}")
    print(f"Formato ISO 24h:                   {formato_iso}")
    print(f"Formato legible descriptivo:       {formato_texto}")
    
    # strptime: convierte texto a objeto datetime
    cadena_fecha = "2026-12-25 18:45:00"
    fecha_parseada = datetime.strptime(cadena_fecha, "%Y-%m-%d %H:%M:%S")
    print(f"Texto original:                    '{cadena_fecha}'")
    print(f"Objeto datetime obtenido:          {fecha_parseada} (tipo: {type(fecha_parseada).__name__})")
    print()

def demostracion_aritmetica_fechas():
    print("=" * 60)
    print("3. ARITMÉTICA CON FECHAS (timedelta)")
    print("=" * 60)
    ahora = datetime.now()
    
    # Sumar y restar intervalos de tiempo
    en_tres_semanas = ahora + timedelta(weeks=3)
    ayer = ahora - timedelta(days=1)
    en_cinco_horas = ahora + timedelta(hours=5, minutes=30)
    
    print(f"Momento actual:                    {ahora.strftime('%Y-%m-%d %H:%M')}")
    print(f"En 3 semanas será:                 {en_tres_semanas.strftime('%Y-%m-%d %H:%M')}")
    print(f"Ayer a esta hora:                  {ayer.strftime('%Y-%m-%d %H:%M')}")
    print(f"En 5 horas y 30 minutos:           {en_cinco_horas.strftime('%Y-%m-%d %H:%M')}")
    
    # Calcular diferencia entre dos fechas
    año_nuevo = datetime(ahora.year + 1, 1, 1, 0, 0, 0)
    tiempo_restante = año_nuevo - ahora
    print(f"Tiempo restante para Año Nuevo:    {tiempo_restante.days} días y {tiempo_restante.seconds // 3600} horas")
    print()

def demostracion_zonas_horarias():
    print("=" * 60)
    print("4. MANEJO DE ZONAS HORARIAS (timezone)")
    print("=" * 60)
    # Fecha en UTC
    ahora_utc = datetime.now(timezone.utc)
    print(f"Hora actual UTC:                   {ahora_utc}")
    
    # Desplazamiento manual (ej. UTC-5, Ciudad de México / Bogotá)
    tz_utc_menos_5 = timezone(timedelta(hours=-5), name="UTC-5")
    ahora_tz = ahora_utc.astimezone(tz_utc_menos_5)
    print(f"Hora en zona horaria UTC-5:        {ahora_tz}")
    print()

def main():
    print("\n>>> DEMOSTRACIÓN DE LA LIBRERÍA 'datetime' EN PYTHON <<<\n")
    demostracion_fechas_y_horas_basicas()
    demostracion_formateo_y_parsing()
    demostracion_aritmetica_fechas()
    demostracion_zonas_horarias()
    print("¡Demostración de 'datetime' completada con éxito!\n")

if __name__ == "__main__":
    main()
