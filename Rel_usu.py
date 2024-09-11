from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from Usuarios import *

def gerar_relatorio(caminho_arquivo):
    c = canvas.Canvas(caminho_arquivo, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 16)
    c.drawString(1 * inch, height - 1 * inch, "Relatório de Usuários")

    c.setLineWidth(1)
    c.line(0.5 * inch, height - 1.2 * inch, width - 0.5 * inch, height - 1.2 * inch)

    c.setFont("Helvetica-Bold", 12)
    c.drawString(0.5 * inch, height - 1.5 * inch, "ID")
    c.drawString(1.5 * inch, height - 1.5 * inch, "Nome")
    c.drawString(3.5 * inch, height - 1.5 * inch, "Telefone")
    c.drawString(5 * inch, height - 1.5 * inch, "Email")
    c.drawString(6.5 * inch, height - 1.5 * inch, "Usuário")

    c.setLineWidth(0.5)
    c.line(0.5 * inch, height - 1.7 * inch, width - 0.5 * inch, height - 1.7 * inch)

    y = height - 2 * inch
    c.setFont("Helvetica", 10)

    usu = Usuarios()
    usuarios = usu.selectAllUsers()
    for u in usuarios:
        c.drawString(0.5 * inch, y, str(u[0]))
        c.drawString(1.5 * inch, y, u[1])
        c.drawString(3.5 * inch, y, u[2])
        c.drawString(5 * inch, y, u[3])
        c.drawString(6.5 * inch, y, u[4])
        y -= 0.3 * inch

        if y < 1 * inch:
            c.showPage()
            c.setFont("Helvetica-Bold", 16)
            c.drawString(1 * inch, height - 1 * inch, "Relatório de Usuários")
            c.setFont("Helvetica-Bold", 12)
            c.drawString(0.5 * inch, height - 1.5 * inch, "ID")
            c.drawString(1.5 * inch, height - 1.5 * inch, "Nome")
            c.drawString(3.5 * inch, height - 1.5 * inch, "Telefone")
            c.drawString(5 * inch, height - 1.5 * inch, "Email")
            c.drawString(6.5 * inch, height - 1.5 * inch, "Usuário")
            c.setLineWidth(0.5)
            c.line(0.5 * inch, height - 1.7 * inch, width - 0.5 * inch, height - 1.7 * inch)
            y = height - 2 * inch

    c.save()
