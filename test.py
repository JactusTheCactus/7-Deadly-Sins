import json
from pathlib import Path
import re
import time
from html import escape

errorMessage = []

# Function to convert JSON to HTML
def json_to_html(json_file, html_file):
    # Open and load the JSON data
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Extract 'data' from the JSON
    # main = main['main']

    # Extract {data} from the main: data = main.get("data", "no data")
    name = data["name"]
    description = data["description"]
    formatting = f"<style>body {{font-family: Arial, sans-serif;margin: -1em 5em 4em;font-size: 1.5rem;}}</style>"
    style = f"style='font-size: 5em;text-decoration: underline;'"

    # Build the HTML file
    html_content = f"<html><head><title>{name}</title>{formatting}<meta charset='UTF-8'></head><body>\n<h1 {style}>{name}</h1><p>{description}</p><b><a href='../../home.html'>Home</a></b></body></html>"

    html_content = html_content.replace("\n", "<br>")
    html_content = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', html_content)
    html_content = re.sub(r'\*(.*?)\*', r'<i>\1</i>', html_content)

    # Write the HTML content to a file
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

filePath = "sins/"
sins = Path(f"{filePath}json")
sinJSON = [item.name for item in sins.iterdir()]
sinHTML =  [item[:-4] + "html" for item in sinJSON]

def runloop():
    for i in range(len(sinJSON)):
        json_file = f"{filePath}json/{sinJSON[i]}"
        html_file = f"{filePath}html/{sinHTML[i]}"
        json_to_html(json_file, html_file)

# Define your variables
title = "Home"
heading1 = "Home"
paragraph = "Test!"

# Use Python string formatting to insert variables into the HTML template
home_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 1rem 5rem 0rem;
            font-size: 1.5rem;
        }}
        h1 {{
            font-size: 5rem;
        }}
    </style>
    <title>{escape(title)}</title>
</head>
<body>
    <h1>{escape(heading1)}</h1>
"""

for i in range(len(sinHTML)):
    home_html += f"<li><a href='{filePath}html/{sinHTML[i]}'>{sinHTML[i][:-5]}</a></li>"

home_html += """
</body>
</html>
"""

with open("home.html", "w", encoding="utf-8") as file:
    file.write(home_html)

runloop()