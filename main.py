import yaml
from pathlib import Path
import re
from html import escape
import os

errorMessage = []

# Mapping of ranks based on sex
rank_mapping = {
    'Imperatore': {
        'm': 'Imperator', 
        'f': 'Imperatrix', 
        'n': 'Imperatore'},
    'Venatorium': {
        'm': 'Venator', 
        'f': 'Venatrix', 
        'n': 'Venatorium'},
    'Ferratorium': {
        'm': 'Ferro', 
        'f': 'Ferroa', 
        'n': 'Ferratorium'},
    'Dominum': {
        'm': 'Dominus', 
        'f': 'Domina', 
        'n': 'Dominum'},
    'Luminorium': {
        'm': 'Luminor', 
        'f': 'Luminora', 
        'n': 'Luminorium'},
    'Exaltum': {
        'm': 'Exaltus', 
        'f': 'Exalta', 
        'n': 'Exaltum'},
    'Bellatorium': {
        'm': 'Bellator', 
        'f': 'Bellatrix', 
        'n': 'Bellatorium'}
}

def replace_rank_with_gender(data):
    for sin, details in data.items():
        sex = details.get("sex", "")
        rank = details.get("rank", "")
        
        if rank:
            # Determine the gendered or neutral rank
            if sex == 'm':
                details['rank'] = rank_mapping.get(rank, {}).get('m', rank)
            elif sex == 'f':
                details['rank'] = rank_mapping.get(rank, {}).get('f', rank)
            else:
                details['rank'] = rank_mapping.get(rank, {}).get('n', rank)
    
    return data

def yaml_to_html(yaml_file, html_file):
    with open(yaml_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        name = data.get("name", "")
        animal = data.get("animal", "")
        sin = data.get("sin", "")
        weapon = data.get("weapon", "")
        colour = data.get("colour", "")
        power = data.get("power", "")
        species = data.get("species", "")
        rank = data.get("rank", "")
    
    fullName = f"{name}, The {animal} Sin of {sin}, {rank} of The Seven Deadly Sins"
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
            Power: {escape(power)}
            <br>
            Species: {escape(species)}
        </p>
        <b><a href='../../home/home.html'>Home</a></b>
    </body>
</html>
    """
    html_content = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', html_content)
    html_content = re.sub(r'\*(.*?)\*', r'<i>\1</i>', html_content)
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

sinHTML = [item.name for item in Path("sins/sins").iterdir()]
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
for i in range(7):
    home_html += f"<li><a href='sins/{sinHTML[i]}'>{sinHTML[i][:-5].capitalize()}</a></li>"
home_html += """
</body>
</html>
"""
with open("home.html", "w", encoding="utf-8") as file:
    file.write(home_html)

def createfile(directory, name, type, content):
    name = f"{name}.{type}"
    with open(f"{directory}/{name}", "w") as file:
        file.write(content)

def yaml_to_md_table(data, yaml_file, html_file):
    table_rows = []
    # Remove the nested loop that causes repetition
    for sin, details in data.items():
        if sin == "ranks":  # Skip processing ranks if it's not part of the table
            continue
        # Extract the details
        name = details.get("name", "Unknown")
        animal = details.get("animal", "Unknown")
        sin_type = details.get("sin", "Unknown")
        weapon = details.get("weapon", "Unknown")
        colour = details.get("colour", "Unknown")
        power = details.get("power", "Unknown")
        species = details.get("species", "Unknown")
        sex = details.get("sex", "Unknown")
        rank = details.get("rank", "Unknown")
        # Only add the row once
        row = f"|{name}|{sin_type}|{animal}|{weapon}|{colour}|{power}|{species}|{rank}|"
        table_rows.append(row)

    # Prepare markdown content
    table_header = "|Name|Sin|Mark|Weapon|Colour|Power|Species|Rank|\n|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|\n"
    table_footer = "\n[Home](home.html)"
    md_content = f"There are __Seven Deadly Sins__. Here is a table:\n\n{table_header}{'\n'.join(table_rows)}\n\n{table_footer}"
    
    # Write the markdown file
    createfile("./", "README", "md", md_content)

# Read the YAML data, apply the rank update, and generate the HTML and MD files
for i in range(7):
    yaml_file = f"sins/sins.yaml"
    html_file = f"sins/sins/{sinHTML[i]}"
    with open(yaml_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        data = replace_rank_with_gender(data)  # Replace the rank with the gendered one

    yaml_to_html(yaml_file, html_file)
    yaml_to_md_table(data, "sins/sins.yaml", html_file)

with open("home.html", "w", encoding="utf-8") as file:
    file.write(home_html)
