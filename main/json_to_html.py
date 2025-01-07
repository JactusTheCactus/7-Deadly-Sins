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

    if data["name"] != "":
        name = f"{data["name"]}, "
    else:
        name = ""
    if data["animal"] != "":
        animal = f"{data["animal"]} "
    else:
        animal = ""
    sin = data["sin"]
    description = data["description"]
    weapon = data["weapon"]
    colour = data["colour"]
    power = data["power"]
    race = data["race"]
    fullName = f"{name}The {animal}Sin of {sin}"

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
    body {{
        font-family: Arial, sans-serif;
        margin: 0rem 5rem 0rem;
        font-size: 1.5rem;
        word-wrap: break-word;
        font-weight: bold;
    }}
    .title {{
        font-size: 5rem;
        text-decoration: underline;
    }}
    </style>
    <title>{escape(sin)}</title>
    <meta charset='UTF-8'>
    </head>
    <body>
        <p class="title">
            {escape(fullName)}
        </p>
        <p>
            Weapon: <u>{escape(weapon)}</u>
            <br>
            Gear Colour: <u>{escape(colour)}</u>
            <br>
            Power: <u>{escape(power)}</u>
            <br>
            Race: <u>{escape(race)}</u>
            <br>
            {escape(description)}
        </p>
        <b><a href='../../home/home.html'>Home</a></b>
    </body>
</html>
    """

    html_content = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', html_content)
    html_content = re.sub(r'\*(.*?)\*', r'<i>\1</i>', html_content)

    # Write the HTML content to a file
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

sins = Path("main/sins/json")
sinJSON = [item.name for item in sins.iterdir()]
sinHTML =  [item[:-4] + "html" for item in sinJSON]

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
    <title>Home</title>
</head>
<body>
    <h1>Home</h1>
"""

for i in range(len(sinHTML)):
    home_html += f"<li><a href='../sins/html/{sinHTML[i]}'>{sinHTML[i][:-5].capitalize()}</a></li>"

home_html += """
</body>
</html>
"""

with open("main/home/home.html", "w", encoding="utf-8") as file:
    file.write(home_html)

def runloop():
    for i in range(len(sinJSON)):
        json_file = f"main/sins/json/{sinJSON[i]}"
        html_file = f"main/sins/html/{sinHTML[i]}"
        json_to_html(json_file, html_file)
    
    # Write the home page separately after generating the sin pages
    with open("main/home/home.html", "w", encoding="utf-8") as file:
        file.write(home_html)

runloop()