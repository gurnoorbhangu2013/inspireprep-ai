import pdfkit

def export_lesson_as_pdf(lesson):
    html = f"<h1>{lesson['title']}</h1><p>{lesson['summary']}</p><ul>"
    for item in lesson["items"]:
        html += f"<li>{item}</li>"
    html += "</ul>"
    pdfkit.from_string(html, "lesson.pdf")

import pdfkit
pdfkit_config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

pdfkit.from_string(html_content, "output.pdf", configuration=pdfkit_config)
