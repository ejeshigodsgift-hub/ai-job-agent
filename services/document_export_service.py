from docx import Document
from fpdf import FPDF


def export_docx(content, path):
    doc = Document()

    doc.add_paragraph(content)

    doc.save(path)


def export_pdf(content, path):
    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=12)

    pdf.multi_cell(0, 10, content)

    pdf.output(path)