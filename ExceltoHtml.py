import pandas as pd

# Load Excel file
excel_data = pd.read_excel('Portfolio.xlsx')

# Convert to HTML with added CSS
html_table = excel_data.to_html(classes='styled-table')

# HTML code with added CSS style
html_with_style = f'''
<!DOCTYPE html>
<html>
<head>
    <title>Portfolio</title>
    <style>
        /* Define your CSS styles here */
        .styled-table {{
            width: 100%;
            border-collapse: collapse;
            border: 1px solid #ddd;
            font-family: Arial, sans-serif;
        }}
        
        .styled-table th, .styled-table td {{
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }}
        
        .styled-table th {{
            background-color: #f2f2f2;
        }}
    </style>
</head>
<body>
    <h1>Portfolio</h1>
    {html_table}
</body>
</html>
'''

# Save HTML to a file
with open('docs/index.html', 'w') as file:
    file.write(html_with_style)
