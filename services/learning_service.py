from fpdf import FPDF


def generate_cv(user_name):
    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt=f"CV FOR {user_name}")

    file_name = f"storage/resumes/{user_name}.pdf"

    pdf.output(file_name)

    return file_name