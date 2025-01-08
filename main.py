import yaml
from pathlib import Path
import re
import time
from html import escape
import os
errorMessage = []
def yaml_to_html(yaml_file, html_file):
    with open(yaml_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
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
        species = data.get("species")
        if species is None:
             species = ""
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
            species: {escape(species)}</u>
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
def yaml_to_md_table(yaml_data,directory,sin_key):
    with open(directory, "r") as file:
        data_dict = yaml.safe_load(file)
    
    table_rows = []
    for key, data in data_dict.items():
        sin_data = yaml_data.get(sin_key, {})
        name = sin_data.get("name", "")
        animal = sin_data.get("animal", "")
        sin = sin_data.get("sin", "")
        weapon = sin_data.get("weapon", "")
        colour = sin_data.get("colour", "")
        power = sin_data.get("power", "")
        species = sin_data.get("species", "")
        row = f"|{name}|{sin}|{animal}|{weapon}|{colour}|{power}|{species}|"
        table_rows.append(row)
        
    table_header = "|Name|Sin|Mark|Weapon|Colour|Power|species|\n"
    table_header += "|:-:|:-:|:-:|:-:|:-:|:-:|:-:|\n"
    table_footer = "\n[Home](home.html)"
    md_content = f"There are __Seven Deadly Sins__. Here is a table:\n\n{table_header}{'\n'.join(table_rows)}\n\n{table_footer}"
    createfile("./", "README", "md", md_content)
for i in range(7):
    yaml_file = f"sins/sins.yaml"
    html_file = f"sins/sins/{sinHTML[i]}"
    yaml_to_html(yaml_file, html_file)
with open(yaml_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
yaml_to_md_table(data,"sins/sins.yaml",html_file)
with open("home.html", "w", encoding="utf-8") as file:
    file.write(home_html)