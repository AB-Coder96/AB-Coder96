def generate_html_css_from_docx(docx_file, output_html_file):
    paragraphs, tables = extract_paragraphs_and_tables(docx_file)

    print("Paragraphs:")
    for i, paragraph in enumerate(paragraphs):
        print(f"Paragraph {i + 1}: {paragraph}")

    print("\nTables:")
    for i, table in enumerate(tables):
        print(f"Table {i + 1}:\n{table}")

    html_content = "<!DOCTYPE html>\n<html>\n<head>\n<title>Portfolio</title>\n"
    html_content += "<link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.2/css/all.min.css' integrity='sha384-rGp68ppUyMMd6JAiyr5K1SfSvYY4GYvRnfT2XrSP7z2S+YYZxM3R8yf+BxyiXagD' "
    html_content += "crossorigin='anonymous'>\n"
    html_content += "<style>\nbody {\nfont-family: Arial, sans-serif;\nmargin: 20px;\n}\n"
    html_content += "table {\nborder-collapse: collapse;\nmargin: 0 auto;\n}\ntable, th, td {\nborder: 1px solid black;\npadding: 5px;\n}\n"
    html_content += "h1, p {\ntext-align: center;\n}\n"
    html_content += "footer {\nposition: fixed;\nbottom: 0;\nwidth: 100%;\nbackground-color: #333;\ntext-align: center;\npadding: 10px;\n"
    html_content += "color: white;\n}\n"
    html_content += "footer a {\ncolor: white;\n}\n"
    html_content += ".table-container {\n display: flex;\n }\n"
    html_content += ".table-container table {\n flex: 1;\n margin-right: 20px;\n}\n" 
    html_content += ".counter {\nfont-size: 24px;\nfont-weight: bold;\n}\n"
    html_content += "</style>\n</head>\n<body>\n"

    # Add the portion showing experience and projects completed
    html_content += "<div style='text-align: center;'>\n"
    html_content += "<p>Years of Experience:</p>\n"
    html_content += "<div class='counter' id='years-counter'>0</div>\n"
    html_content += "<p>Projects Completed:</p>\n"
    html_content += "<div class='counter' id='projects-counter'>0</div>\n"
    html_content += "</div>\n"

    html_content += "<script>\n"
    html_content += "const yearsCounter = document.getElementById('years-counter');\n"
    html_content += "const projectsCounter = document.getElementById('projects-counter');\n"
    html_content += "let years = 0;\n"
    html_content += "let projects = 0;\n"
    html_content += "const yearsIncrement = 4 / 100; // Increment for animation\n"
    html_content += "const projectsIncrement = 40 / 100; // Increment for animation\n"
    html_content += "function animateCounters() {\n"
    html_content += "if (years < 4) {\n"
    html_content += "years += yearsIncrement;\n"
    html_content += "yearsCounter.innerText = Math.round(years);\n"
    html_content += "}\n"
    html_content += "if (projects < 40) {\n"
    html_content += "projects += projectsIncrement;\n"
    html_content += "projectsCounter.innerText = Math.round(projects);\n"
    html_content += "}\n"
    html_content += "requestAnimationFrame(animateCounters);\n"
    html_content += "}\n"
    html_content += "animateCounters();\n"
    html_content += "</script>\n"

    # Add the remaining content
    html_content += "<h1>{paragraphs[0]}</h1>\n"
    html_content += f"<p>{paragraphs[1]}</p>\n"
    html_content += "<div class='table-container'>\n"
    html_content += tables[0] + "\n"
    html_content += tables[1] + "\n"
    html_content += "</div>\n"
    # Check if the current paragraph is at index 4
    html_content += f"<p>{paragraphs[4]}</p>\n"
    # Display the table
    html_content += "<div class='table-container'>\n"
    html_content += tables[2] + "\n"
    html_content += tables[3] + "\n"
    html_content += "</div>\n"
    html_content += f"<p>{paragraphs[6]}</p>\n"
    # Display the table
    html_content += "<div class='table-container'>\n"
    html_content += tables[4] + "\n"
    html_content += tables[5] + "\n"
    html_content += "</div>\n"
    html_content += f"<h1>{paragraphs[9]}</h1>\n"
    html_content += tables[6] + "\n"
    # Add code to embed PDF using PDF.js
    html_content += "<canvas id='pdf-render'></canvas>\n"
    html_content += "<script src='https://mozilla.github.io/pdf.js/build/pdf.js'></script>\n"
    html_content += "<script>\n"
    html_content += "const pdfUrl = 'Imbalance_paper.pdf';\n"  # Update this line with the correct PDF file name
    html_content += "pdfjsLib.getDocument(pdfUrl).then(pdf => {\n"
    html_content += "pdf.getPage(1).then(page => {\n"
    html_content += "const canvas = document.getElementById('pdf-render');\n"
    html_content += "const context = canvas.getContext('2d');\n"
    html_content += "const viewport = page.getViewport({ scale: 1.5 });\n"
    html_content += "canvas.width = viewport.width;\n"
    html_content += "canvas.height = viewport.height;\n"
    html_content += "page.render({ canvasContext: context, viewport: viewport });\n"
    html_content += "});\n"
    html_content += "});\n"
    html_content += "</script>\n"


    # Add HTML footer with date modified, links, and email
    date_modified = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    github_link = "https://github.com/AB-Coder96"
    linkedin_link = "https://www.linkedin.com/in/araz-karimi-0b2600290/"
    email_address = "arazbagherzadeh@gmail.com"
    
    html_content += f"<footer>\n
