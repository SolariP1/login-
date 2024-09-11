from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from apliCidade import Cidades  # Certifique-se de que a importação está correta

def gerar_relatorio_cidades(caminho_arquivo):
    c = canvas.Canvas(caminho_arquivo, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 16)
    c.drawString(1 * inch, height - 1 * inch, "Relatório de Cidades")

    c.setLineWidth(1)
    c.line(0.5 * inch, height - 1.2 * inch, width - 0.5 * inch, height - 1.2 * inch)

    c.setFont("Helvetica-Bold", 12)
    c.drawString(0.5 * inch, height - 1.5 * inch, "ID")
    c.drawString(2.0 * inch, height - 1.5 * inch, "Cidade")
    c.drawString(5.0 * inch, height - 1.5 * inch, "UF")

    c.setLineWidth(0.5)
    c.line(0.5 * inch, height - 1.7 * inch, width - 0.5 * inch, height - 1.7 * inch)

    y = height - 2 * inch
    c.setFont("Helvetica", 10)

    cidades_db = Cidades()
    cidades = cidades_db.selectAllCidades()
    for cidade in cidades:
        c.drawString(0.5 * inch, y, str(cidade[0]))  # ID
        c.drawString(2.0 * inch, y, cidade[1])       # Nome da cidade
        c.drawString(5.0 * inch, y, cidade[2])       # UF
        y -= 0.3 * inch

        if y < 1 * inch:
            c.showPage()
            c.setFont("Helvetica-Bold", 16)
            c.drawString(1 * inch, height - 1 * inch, "Relatório de Cidades")
            c.setFont("Helvetica-Bold", 12)
            c.drawString(0.5 * inch, height - 1.5 * inch, "ID")
            c.drawString(2.0 * inch, height - 1.5 * inch, "Cidade")
            c.drawString(5.0 * inch, height - 1.5 * inch, "UF")
            c.setLineWidth(0.5)
            c.line(0.5 * inch, height - 1.7 * inch, width - 0.5 * inch, height - 1.7 * inch)
            y = height - 2 * inch

    c.save()
