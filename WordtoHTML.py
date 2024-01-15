from docx import Document

def extract_paragraphs_and_tables(docx_file):
    doc = Document(docx_file)
    combined_list = []

    for element in doc.element.body:
        if element.tag.endswith('p') and element.text:  # Paragraph with text
            combined_list.append({'type': 'paragraph', 'content': element.text.strip()})
        elif element.tag.endswith('tbl'):  # Table
            table_data = []
            for row in element:
                row_data = [cell.text.strip() for cell in row]
                table_data.append(row_data)
            combined_list.append({'type': 'table', 'content': table_data})

    return combined_list

def generate_html_from_elements(elements):
    html_content = ""

    for element in elements:
        if element['type'] == 'paragraph':
            html_content += f"<p>{element['content']}</p>\n"
        elif element['type'] == 'table':
            html_content += "<table border='1'>\n"
            for row_data in element['content']:
                html_content += "<tr>"
                for cell_data in row_data:
                    html_content += f"<td>{cell_data}</td>"
                html_content += "</tr>\n"
            html_content += "</table>\n"
    print(html_content)
    return html_content

def generate_html_css_from_docx(docx_file, output_html_file):
    elements = extract_paragraphs_and_tables(docx_file)

    html_content = "<!DOCTYPE html>\n<html>\n<head>\n<title>Word to HTML</title>\n"
    html_content += "<style>\nbody {\nfont-family: Arial, sans-serif;\nmargin: 20px;\n}\n"
    html_content += "table {\nborder-collapse: collapse;\n}\ntable, th, td {\nborder: 1px solid black;\npadding: 5px;\n}\n"
    html_content += "</style>\n</head>\n<body>\n"

    html_content += generate_html_from_elements(elements)

    html_content += "</body>\n</html>"

    with open(output_html_file, "w", encoding="utf-8") as html_file:
        html_file.write(html_content)

#
