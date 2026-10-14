"""
Librería: fpdf (fpdf2)
Descripción: Crear un archivo PDF básico a partir de texto ingresado.
"""
try:
    from fpdf import FPDF
except ImportError:
    print("[Error] La librería 'fpdf2' no está instalada. Ejecuta: pip install fpdf2")
    exit()

print("=== EJEMPLO INTERACTIVO: FPDF ===")

# Pedir datos al usuario
titulo = input("Ingresa el título del documento: ").strip() or "Mi Primer Documento PDF"
autor = input("Ingresa tu nombre (autor): ").strip() or "Estudiante Python"
mensaje = input("Ingresa un mensaje o párrafo para el PDF: ").strip() or "Este es un documento generado con la librería FPDF en Python de manera interactiva."

# Crear PDF
pdf = FPDF()
pdf.add_page()

# Título
pdf.set_font("Helvetica", "B", 18)
pdf.cell(0, 15, titulo, new_x="LMARGIN", new_y="NEXT", align="C")

# Autor
pdf.set_font("Helvetica", "I", 12)
pdf.cell(0, 10, f"Autor: {autor}", new_x="LMARGIN", new_y="NEXT", align="C")
pdf.ln(10)

# Contenido
pdf.set_font("Helvetica", size=11)
pdf.multi_cell(0, 8, mensaje)

# Guardar
nombre_archivo = "mi_documento_fpdf.pdf"
pdf.output(nombre_archivo)
print(f"\n ¡PDF creado exitosamente como '{nombre_archivo}'!")
