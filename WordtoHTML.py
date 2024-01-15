from docx import Document
from datetime import datetime

def extract_paragraphs_and_tables(docx_file):
    doc = Document(docx_file)
    paragraphs = [p.text for p in doc.paragraphs]
    tables_html = []

    for table in doc.tables:
        table_html = "<table border='1'>"
        for row in table.rows:
            table_html += "<tr>"
            for cell in row.cells:
                table_html += f"<td>{cell.text}</td>"
            table_html += "</tr>"
        table_html += "</table>"
        tables_html.append(table_html)

    return paragraphs, tables_html

def generate_html_css_from_docx(docx_file, output_html_file):
    paragraphs, tables = extract_paragraphs_and_tables(docx_file)

    html_content = "<!DOCTYPE html>\n<html>\n<head>\n<title>Portfolio</title>\n"
    html_content += "<style>\nbody {\nfont-family: Arial, sans-serif;\nmargin: 20px;\n}\n"
    html_content += "table {\nborder-collapse: collapse;\n}\ntable, th, td {\nborder: 1px solid black;\npadding: 5px;\n}\n"
    html_content += "</style>\n</head>\n<body>\n"

    for paragraph in paragraphs:
        html_content += f"<p>{paragraph}</p>\n"

    for table in tables:
        html_content += table + "\n"

    # Add HTML footer with date modified, links, and email
    date_modified = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    github_link = "https://github.com/AB-Coder96"
    linkedin_link = "https://www.linkedin.com/in/araz-karimi-0b2600290/"
    email_address = "arazbagherzadeh@gmail.com"
    
    html_content += f"<footer>\n"
    html_content += f"Date Modified: {date_modified}<br>\n"
    html_content += f"GitHub: <a href='{github_link}'>{github_link}</a><br>\n"
    html_content += f"LinkedIn: <a href='{linkedin_link}'>{linkedin_link}</a><br>\n"
    html_content += f"Email: <a href='mailto:{email_address}'>{email_address}</a>\n"
    html_content += "</footer>\n"

    html_content += "</body>\n</html>"

    with open(output_html_file, "w", encoding="utf-8") as html_file:
        html_file.write(html_content)

# Replace 'input_word.docx' with the path to your Word file
input_word_file = 'portfolio Araz Karimi.docx'
output_html_file = 'docs/index.html'

generate_html_css_from_docx(input_word_file, output_html_file)
