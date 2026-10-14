"""
Librería: reportlab
Descripción: Generar un PDF con diseño y formato usando ReportLab.
"""
try:
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib import colors
except ImportError:
    print("[Error] La librería 'reportlab' no está instalada. Ejecuta: pip install reportlab")
    exit()

print("=== EJEMPLO INTERACTIVO: REPORTLAB ===")

# Entrada de datos
titulo = input("Ingresa el título del reporte: ").strip() or "Reporte con ReportLab"
contenido = input("Escribe el contenido o nota que deseas incluir: ").strip() or "ReportLab permite estructurar documentos PDF profesionales con soporte de estilos avanzados."

nombre_archivo = "reporte_reportlab.pdf"
doc = SimpleDocTemplate(nombre_archivo, pagesize=letter)
estilos = getSampleStyleSheet()

# Estilo personalizado para el título
estilo_titulo = ParagraphStyle(
    'TituloAzul',
    parent=estilos['Heading1'],
    fontName='Helvetica-Bold',
    fontSize=18,
    textColor=colors.navy,
    spaceAfter=15
)

# Estructurar contenido del PDF
elementos = [
    Paragraph(titulo, estilo_titulo),
    Spacer(1, 10),
    Paragraph(contenido, estilos['Normal']),
    Spacer(1, 20),
    Paragraph("<i>Documento generado automáticamente con Python y ReportLab.</i>", estilos['Italic'])
]

# Construir PDF
doc.build(elementos)
print(f"\n ¡Archivo PDF generado con éxito: '{nombre_archivo}'!")
