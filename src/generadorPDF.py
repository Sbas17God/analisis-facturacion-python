from fpdf import FPDF

# 1. Captura de datos
proyecto = input("Escriba una breve descripcion del proyecto: ")
horas_estimadas = int(input("Escribas las horas estimadas para el proyecto: "))
valor_hora = int(input("¿Cual es el valor de la hora trabajada?: "))
tiempo_estimado = input("Escriba cuanto tiempo estima que tomara el proyecto: ")

# 2. Cálculos
valor_total = horas_estimadas * valor_hora

# 3. Generación del PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12) # Es importante definir el tamaño de la fuente

# Importante: Convertimos los números a string usando str() para que FPDF los acepte
pdf.text(115, 145, proyecto)
pdf.text(115, 160, str(horas_estimadas))
pdf.text(115, 175, str(valor_hora))
pdf.text(115, 190, tiempo_estimado)
pdf.text(115, 205, str(valor_total))

# 4. Salida
pdf.output("Presupuesto.pdf")
print("Presupuesto generado con éxito")