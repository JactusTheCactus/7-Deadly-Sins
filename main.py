import json
from pathlib import Path
import re
import time
from html import escape
import os
errorMessage = []
def json_to_html(json_file, html_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)    
        name = data.get("name")
        if name is None:
             name = ""
        animal = data.get("animal")
        if animal is None:
             animal = ""
        sin = data.get("sin")
        if sin is None:
             sin = ""
        weapon = data.get("weapon")
        if weapon is None:
             weapon = ""
        colour = data.get("colour")
        if colour is None:
             colour = ""
        power = data.get("power")
        if power is None:
             power = ""
        race = data.get("race")
        if race is None:
             race = ""
    fullName = f"{name}, The {animal} Sin of {sin}"
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
            Colour: <u>{escape(colour)}</u>
            <br>
            Power: {escape(power)}</u>
            <br>
            Race: {escape(race)}</u>
        </p>
        <b><a href='../../home/home.html'>Home</a></b>
    </body>
</html>
    """
    html_content = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', html_content)
    html_content = re.sub(r'\*(.*?)\*', r'<i>\1</i>', html_content)
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
sinHTML =  [item.name for item in Path("sins/sins").iterdir()]
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
    home_html += f"<li><a href='sins/{sinHTML[i]}'>{sinHTML[i][:-5].capitalize()}</a></li>"
home_html += """
</body>
</html>
"""
with open("home.html", "w", encoding="utf-8") as file:
    file.write(home_html)
def createfile(directory,name,type,content):
	name = f"{name}.{type}"
	with open(f"{directory}/{name}", "w") as file:
		file.write(content)
def json_to_md_table(directory):
    with open(directory, "r") as file:
        data_dict = json.load(file)
    
    table_rows = []
    for key, data in data_dict.items():
        name = data.get("name", "")
        animal = data["animal"]
        sin = data["sin"]
        weapon = data["weapon"]
        colour = data["colour"]
        power = data["power"]
        race = data["race"]
        row = f"|{name}|{sin}|{animal}|{weapon}|{colour}|{power}|{race}|"
        table_rows.append(row)
        
    table_header = "|Name|Sin|Mark|Weapon|Colour|Power|Race|\n"
    table_header += "|:-:|:-:|:-:|:-:|:-:|:-:|:-:|\n"
    table_footer = "\n[Home](home/home.html)"
    md_content = f"There are __Seven Deadly Sins__. Here is a table:\n\n{table_header}{'\n'.join(table_rows)}\n\n{table_footer}"
    createfile("./", "README", "md", md_content)
json_to_md_table("sins/sins.json")
for i in range(7):
    json_file = f"sins/sins.json"
    html_file = f"sins/sins/{sinHTML[i]}"
    json_to_html(json_file, html_file)
with open("sins/home.html", "w", encoding="utf-8") as file:
    file.write(home_html)