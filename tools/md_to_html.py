import sys
import os
import markdown

# HTML Template with Print-Optimized CSS
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: "Times New Roman", Times, serif;
            line-height: 1.4;
            max-width: 100%;
            margin: 20px;
            color: #000;
        }}
        h1, h2 {{
            text-align: center;
            text-transform: uppercase;
        }}
        .header-box {{
            border: 2px solid #000;
            padding: 15px;
            margin-bottom: 20px;
            background-color: #f9f9f9;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }}
        th, td {{
            border: 1px solid #000;
            padding: 10px;
            vertical-align: top;
            text-align: left;
        }}
        th {{
            background-color: #eee;
            font-weight: bold;
        }}
        
        /* Column Widths (Approximate) */
        th:nth-child(1), td:nth-child(1) {{ width: 10%; }} /* Segment */
        th:nth-child(2), td:nth-child(2) {{ width: 10%; }} /* Time */
        th:nth-child(3), td:nth-child(3) {{ width: 35%; }} /* Visual */
        th:nth-child(4), td:nth-child(4) {{ width: 30%; }} /* Audio */
        th:nth-child(5), td:nth-child(5) {{ width: 15%; }} /* Note */

        /* Print Styles */
        @media print {{
            body {{ margin: 0; }}
            .header-box {{ background-color: white !important; }}
            th {{ background-color: white !important; font-weight: bold; border-bottom: 2px solid black; }}
            a {{ text-decoration: none; color: black; }}
            h1, h2 {{ page-break-after: avoid; }}
            table {{ page-break-inside: auto; }}
            tr {{ page-break-inside: avoid; page-break-after: auto; }}
        }}
        
        .gesture-box {{
            border: 1px dashed #666;
            padding: 10px;
            margin-bottom: 20px;
        }}
    </style>
</head>
<body>
    {content}
</body>
</html>
"""

def convert_md_to_html(md_path):
    if not os.path.exists(md_path):
        print(f"Error: File '{md_path}' not found.")
        sys.exit(1)

    # Read Markdown content
    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    # Convert to HTML (using extensions for tables)
    html_content = markdown.markdown(md_text, extensions=['tables', 'fenced_code'])

    # Prepare Title and Filename
    filename = os.path.basename(md_path)
    title = filename.replace('.md', '').replace('_', ' ').title() + " - Printable"
    output_filename = md_path.replace('.md', '_printable.html')

    # Inject Content into Template
    final_html = HTML_TEMPLATE.format(title=title, content=html_content)

    # Write HTML file
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(final_html)

    print(f"Success! Created printable HTML: {output_filename}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python tools/md_to_html.py <markdown_file_path>")
        sys.exit(1)
    
    convert_md_to_html(sys.argv[1])
