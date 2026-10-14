"""
Ejemplos de generación de documentos PDF con la librería 'fpdf2' (FPDF).

FPDF es una librería ligera y rápida para generar archivos PDF en Python
sin necesidad de herramientas externas o dependencias complejas de C.

Instalación:
    pip install fpdf2
"""

import sys
import os

try:
    from fpdf import FPDF
    FPDF_INSTALADO = True
except ImportError:
    FPDF_INSTALADO = False


class ReportePersonalizadoPDF(FPDF if FPDF_INSTALADO else object):
    """Clase personalizada para cabeceras y pies de página automáticos."""
    
    def header(self):
        # Fuente Arial negrita 12
        self.set_font("Helvetica", "B", 12)
        # Título en la cabecera
        self.cell(0, 10, "Empresa de Tecnología Global S.A. - Reporte Anual", border=0, align="C")
        self.ln(12)
        # Línea divisoria decorativa
        self.set_draw_color(52, 152, 219) # Azul
        self.set_line_width(0.8)
        self.line(10, 22, 200, 22)
        self.ln(5)

    def footer(self):
        # Posición a 1.5 cm del final
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(128, 128, 128)
        # Número de página dinámico
        self.cell(0, 10, f"Página {self.page_no()}/{{nb}}", align="C")


def generar_pdf_fpdf(nombre_archivo="reporte_fpdf_ejemplo.pdf"):
    print("=" * 60)
    print("DEMOSTRACIÓN DE LA LIBRERÍA 'fpdf' (fpdf2)")
    print("=" * 60)
    
    if not FPDF_INSTALADO:
        print("[AVISO] La librería 'fpdf2' no está instalada en el entorno.")
        print("Para instalarla ejecuta: pip install fpdf2")
        print("A continuación se muestra el código y estructura requerida para usarla:")
        print("-" * 60)
        print("""
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", size=12)
pdf.cell(200, 10, text="¡Hola Mundo en PDF con FPDF!", new_x="LMARGIN", new_y="NEXT", align="C")
pdf.output("ejemplo.pdf")
        """)
        return False

    pdf = ReportePersonalizadoPDF(orientation="P", unit="mm", format="A4")
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # 1. Título principal
    pdf.set_font("Helvetica", "B", 16)
    pdf.set_text_color(44, 62, 80)
    pdf.cell(0, 12, "Resumen Ejecutivo de Rendimiento", align="L")
    pdf.ln(10)
    
    # 2. Párrafo descriptivo (MultiCell)
    pdf.set_font("Helvetica", size=10)
    pdf.set_text_color(50, 50, 50)
    texto_parrafo = (
        "Este documento ha sido generado automáticamente utilizando la librería fpdf2 de Python. "
        "FPDF permite un control milimétrico sobre el diseño del documento, márgenes, estilos "
        "de fuente, colores y estructuración en tablas tabuladas de alto rendimiento."
    )
    pdf.multi_cell(0, 6, texto_parrafo)
    pdf.ln(6)
    
    # 3. Sección de Datos Tabulares
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(41, 128, 185)
    pdf.cell(0, 8, "Métricas Clave del Trimestre", align="L")
    pdf.ln(8)
    
    # Cabecera de la tabla
    columnas = [("Indicador", 70), ("Meta", 40), ("Obtenido", 40), ("Cumplimiento", 40)]
    pdf.set_fill_color(52, 152, 219)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Helvetica", "B", 10)
    for col_titulo, col_ancho in columnas:
        pdf.cell(col_ancho, 8, col_titulo, border=1, align="C", fill=True)
    pdf.ln()
    
    # Filas de datos
    filas = [
        ("Nuevos Usuarios", "10,000", "12,450", "+124.5%"),
        ("Tasa de Conversión", "3.5%", "4.1%", "+117.1%"),
        ("Ingresos Recurrentes", "$50,000", "$54,200", "+108.4%"),
        ("Satisfacción CSAT", "90%", "94%", "+104.4%")
    ]
    
    pdf.set_font("Helvetica", size=9)
    pdf.set_text_color(30, 30, 30)
    relleno = False
    for fila in filas:
        if relleno:
            pdf.set_fill_color(240, 244, 248)
        else:
            pdf.set_fill_color(255, 255, 255)
            
        pdf.cell(70, 7, fila[0], border=1, align="L", fill=True)
        pdf.cell(40, 7, fila[1], border=1, align="C", fill=True)
        pdf.cell(40, 7, fila[2], border=1, align="C", fill=True)
        pdf.cell(40, 7, fila[3], border=1, align="C", fill=True)
        pdf.ln()
        relleno = not relleno
        
    pdf.ln(10)
    
    # Guardar archivo
    ruta_salida = os.path.join(os.path.dirname(__file__), nombre_archivo)
    pdf.output(ruta_salida)
    print(f" PDF generado exitosamente: {ruta_salida}")
    return True


def main():
    generar_pdf_fpdf()


if __name__ == "__main__":
    main()
