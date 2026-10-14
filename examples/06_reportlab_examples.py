"""
Ejemplos de generación de documentos PDF avanzados con 'reportlab'.

ReportLab es la librería estándar empresarial en Python para crear
documentos PDF complejos, reportes automatizados, gráficos vectoriales y facturas.

Instalación:
    pip install reportlab
"""

import os
import sys

try:
    from reportlab.lib.pagesizes import letter
    from reportlab.lib import colors
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    REPORTLAB_INSTALADO = True
except ImportError:
    REPORTLAB_INSTALADO = False


def generar_pdf_reportlab(nombre_archivo="reporte_reportlab_ejemplo.pdf"):
    print("=" * 60)
    print("DEMOSTRACIÓN DE LA LIBRERÍA 'reportlab'")
    print("=" * 60)
    
    if not REPORTLAB_INSTALADO:
        print("[AVISO] La librería 'reportlab' no está instalada en el entorno.")
        print("Para instalarla ejecuta: pip install reportlab")
        print("A continuación se muestra la estructura recomendada con PLATYPUS:")
        print("-" * 60)
        print("""
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

doc = SimpleDocTemplate("salida.pdf")
styles = getSampleStyleSheet()
historia = [
    Paragraph("Título Principal", styles['Heading1']),
    Spacer(1, 10),
    Paragraph("Este es un párrafo formateado.", styles['BodyText'])
]
doc.build(historia)
        """)
        return False

    ruta_salida = os.path.join(os.path.dirname(__file__), nombre_archivo)
    doc = SimpleDocTemplate(
        ruta_salida,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )
    
    estilos = getSampleStyleSheet()
    
    # Estilo personalizado
    estilo_titulo = ParagraphStyle(
        'TituloPersonalizado',
        parent=estilos['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#1E3A8A'),
        spaceAfter=14
    )
    
    estilo_subtitulo = ParagraphStyle(
        'SubtituloPersonalizado',
        parent=estilos['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=colors.HexColor('#2563EB'),
        spaceBefore=12,
        spaceAfter=8
    )
    
    historia = []
    
    # 1. Título y encabezado
    historia.append(Paragraph("Reporte Financiero y Operativo", estilo_titulo))
    historia.append(Paragraph("Generado automáticamente con Python & ReportLab Platypus", estilo_subtitulo))
    historia.append(Spacer(1, 12))
    
    # 2. Párrafo con formato HTML/XML enriquecido
    texto_intro = (
        "ReportLab permite utilizar <b>etiquetas enriquecidas</b> como negrita, "
        "<i>cursiva</i> y <font color='#059669'>colores personalizados</font> directamente en los párrafos. "
        "Su motor de flujo (Flowables) ajusta dinámicamente las páginas y el flujo del texto."
    )
    historia.append(Paragraph(texto_intro, estilos['Normal']))
    historia.append(Spacer(1, 16))
    
    # 3. Tabla con TableStyle profesional
    datos_tabla = [
        ["Categoría", "Q1 (USD)", "Q2 (USD)", "Crecimiento"],
        ["Suscripciones SaaS", "$120,000", "$145,000", "+20.8%"],
        ["Servicios de Consultoría", "$45,000", "$52,000", "+15.5%"],
        ["Licencias Empresariales", "$80,000", "$95,000", "+18.7%"],
        ["Total Consolidado", "$245,000", "$292,000", "+19.1%"]
    ]
    
    tabla = Table(datos_tabla, colWidths=[180, 100, 100, 100])
    tabla.setStyle(TableStyle([
        # Fondo cabecera
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1E3A8A')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('ALIGN', (0, 1), (0, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        # Filas alternas
        ('BACKGROUND', (0, 1), (-1, -2), colors.HexColor('#F8FAFC')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -2), [colors.white, colors.HexColor('#F1F5F9')]),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E1')),
        # Fila final (Total)
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#E2E8F0')),
        ('TEXTCOLOR', (0, -1), (-1, -1), colors.HexColor('#0F172A')),
    ]))
    
    historia.append(tabla)
    historia.append(Spacer(1, 20))
    historia.append(Paragraph("Nota: Este reporte cuenta con validación matemática automatizada.", estilos['Italic']))
    
    doc.build(historia)
    print(f" PDF con ReportLab generado exitosamente: {ruta_salida}")
    return True


def main():
    generar_pdf_reportlab()


if __name__ == "__main__":
    main()
