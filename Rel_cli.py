from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from apliClientes import Clientes

def gerar_relatorio_clientes(caminho_arquivo):
    c = canvas.Canvas(caminho_arquivo, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 22)
    c.drawString(1 * inch, height - 1 * inch, "Relatório de Clientes")

    c.setLineWidth(1)
    c.line(0.5 * inch, height - 1.2 * inch, width - 0.5 * inch, height - 1.2 * inch)

    c.setFont("Helvetica-Bold", 12)
    c.drawString(0.5 * inch, height - 1.5 * inch, "ID")
    c.drawString(2.0 * inch, height - 1.5 * inch, "Nome")
    c.drawString(4.0 * inch, height - 1.5 * inch, "Nascimento")
    c.drawString(5.5 * inch, height - 1.5 * inch, "CPF")
    c.drawString(7.0 * inch, height - 1.5 * inch, "Gênero")

    c.setLineWidth(0.5)
    c.line(0.5 * inch, height - 1.7 * inch, width - 0.5 * inch, height - 1.7 * inch)

    y = height - 2 * inch
    c.setFont("Helvetica", 10)

    clientes_db = Clientes()
    clientes = clientes_db.selectAllClientes()
    for cliente in clientes:
        c.drawString(0.5 * inch, y, str(cliente[0]))
        c.drawString(2.0 * inch, y, cliente[1])
        c.drawString(4.0 * inch, y, cliente[2])
        c.drawString(5.5 * inch, y, cliente[3])
        c.drawString(7.0 * inch, y, cliente[4])
        y -= 0.3 * inch

        if y < 1 * inch:
            c.showPage()
            c.setFont("Helvetica-Bold", 16)
            c.drawString(1 * inch, height - 1 * inch, "Relatório de Clientes")
            c.setFont("Helvetica-Bold", 12)
            c.drawString(0.5 * inch, height - 1.5 * inch, "ID")
            c.drawString(2.0 * inch, height - 1.5 * inch, "Nome")
            c.drawString(4.0 * inch, height - 1.5 * inch, "Nascimento")
            c.drawString(5.5 * inch, height - 1.5 * inch, "CPF")
            c.drawString(7.0 * inch, height - 1.5 * inch, "Gênero")
            y = height - 2 * inch

    c.save()
