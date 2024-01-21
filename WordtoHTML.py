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
    html_content += "<link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.2/css/all.min.css' integrity='sha384-rGp68ppUyMMd6JAiyr5K1SfSvYY4GYvRnfT2XrSP7z2S+YYZxM3R8yf+BxyiXagD' "
    html_content += "crossorigin='anonymous'>\n"
    html_content += "<style>\nbody {\nfont-family: Arial, sans-serif;\nmargin: 20px;\n}\n"
    html_content += "table {\nborder-collapse: collapse;\nmargin: 0 auto;\n}\ntable, th, td {\nborder: 1px solid black;\npadding: 5px;\n}\n"
    html_content += "h1, p {\ntext-align: center;\n}\n"
    html_content += "footer {\nposition: fixed;\nbottom: 0;\nwidth: 100%;\nbackground-color: #333;\ntext-align: center;\npadding: 10px;\n"
    html_content += "color: white;\n}\n"
    html_content += "footer a {\ncolor: white;\n}\n"
    html_content += "</style>\n</head>\n<body>\n"

    # Add the first paragraph as an <h1> header
    if paragraphs:
        html_content += f"<h1>{paragraphs[0]}</h1>\n"

    # Iterate through paragraphs and tables, excluding the first paragraph
    i = 1
    while i < len(paragraphs):
        # Check if the current paragraph is at index 4
        if i == 4:
            html_content += f"<h1>{paragraphs[i]}</h1>\n"
            # Check if there is a corresponding table for this paragraph
            if i - 1 < len(tables):
                # Display the table
                html_content += tables[i - 1] + "\n"
            i += 1  # Skip the next iteration as the table is already handled
        else:
            # Display paragraph
            html_content += f"<p>{paragraphs[i]}</p>\n"
            
            # Check if there is a corresponding table for this paragraph
            if i - 1 < len(tables):
                # Display the table
                html_content += tables[i - 1] + "\n"

        i += 1

    # Add HTML footer with date modified, links, and email
    date_modified = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    github_link = "https://github.com/AB-Coder96"
    linkedin_link = "https://www.linkedin.com/in/araz-karimi-0b2600290/"
    email_address = "arazbagherzadeh@gmail.com"
    
    html_content += f"<footer>\n"
    html_content += f"Made by Araz Karimi<br>\n"  # Line added before "Date Modified"
    html_content += f"<a href='{github_link}' target='_blank'><i class='fab fa-github'></i> GitHub</a> | "
    html_content += f"<a href='{linkedin_link}' target='_blank'><i class='fab fa-linkedin'></i> LinkedIn</a> | "
    html_content += f"<a href='mailto:{email_address}'><i class='far fa-envelope'></i> {email_address}</a><br>\n"
    html_content += f"Date Modified: {date_modified}\n"
    html_content += "</footer>\n"

    html_content += "</body>\n</html>"

    with open(output_html_file, "w", encoding="utf-8") as html_file:
        html_file.write(html_content)

# Replace 'input_word.docx' with the path to your Word file
input_word_file = 'portfolio Araz Karimi.docx'
output_html_file = 'docs/index.html'

generate_html_css_from_docx(input_word_file, output_html_file)
