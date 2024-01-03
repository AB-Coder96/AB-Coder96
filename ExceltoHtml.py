import pandas as pd

# Load Excel file
excel_data = pd.read_excel('Portfolio.xlsx')

# Convert to HTML
html_table = excel_data.to_html()

# Save HTML to a file
with open('docs/portfolio.html', 'w') as file:
    file.write(html_table)
