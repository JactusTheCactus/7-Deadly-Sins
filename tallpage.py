import yaml
import os
from html import escape
import re
from pathlib import Path

def test(x):
    print(f"|{x}|")
# Function to ensure the value is not None before escaping
def safe_escape(value):
    if value is None:
        return ""  # or return a default value like "[Unknown]"
    return escape(str(value))
def get_gendered_rank(rank, sex):
    # Dictionary mapping rank to its male and female versions
    rank_map = {
        "Imperatore": {"F": "Imperatrix", "M": "Imperator"},
        "Dominum": {"F": "Domina", "M": "Dominus"},
        "Venatorium": {"F": "Venatoria", "M": "Venator"},
        "Ferratorium": {"F": "Ferratoria", "M": "Ferrator"},
        "Luminorium": {"F": "Luminoria", "M": "Luminor"},
        "Exaltum": {"F": "Exalta", "M": "Exaltus"},
        "Bellatorium": {"F": "Bellatoria", "M": "Bellator"},
    }
    
    # Return the appropriate rank based on sex or return the original if not in the map
    return rank_map.get(rank, {}).get(sex, rank)

def yaml_to_html(yaml_data, aspect_key):
    aspect_data = yaml_data.get(aspect_key, {})
    rank = safe_escape(aspect_data.get("rank",""))
    if rank == "" or rank is None: rank = "[RANK]"
    def title(aspect_key):
        name = data[aspect_key]['name']
        prefixTitles = [
            "Imperatore",
            "Dominum"
            ]
        if data[aspect_key]['rank'] in prefixTitles:
            if name is None:
                title = f"{get_gendered_rank(data[aspect_key]['rank'],data[aspect_key]['sex'])}"
            else:
                title = f"{rank} {name}"
        else:
            if name is None:
                title = f"{get_gendered_rank(data[aspect_key]['rank'],data[aspect_key]['sex'])}"
            else:
                title = f"{name}, the {get_gendered_rank(data[aspect_key]['rank'],data[aspect_key]['sex'])}"
        return(title)
    def full(aspect_key):
        if data[aspect_key]['name'] is None:
            name = f"{data[aspect_key]['aspect']}"
        else:
            name = data[aspect_key]['name']
        name = f"{name}"
        animal = f"{data[aspect_key]['animal']}"
        aspect = f"{data[aspect_key]['aspect']}"
        aspectTitle = title(aspect_key)
        alignment = data[aspect_key]['alignment']
        fullaspect = f"{animal} {alignment} of {aspect}"
        fullName = f"{aspectTitle}, {fullaspect}"
        return fullName
yaml_file = "aspects.yaml"
with open(yaml_file, 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)
for aspect in data.keys():
    html_file = f"{aspect}.html"
    yaml_to_html(data, aspect)
def title(aspect):
    name = data[aspect]['name']
    rank = data[aspect]['rank']
    sex = data[aspect]['sex']
    if sex is None: pass
    else: rank = get_gendered_rank(rank,sex)
    if rank is None: rank = ""
    else: rank = f" {rank}"
    title = f"{name}{rank}"
    # test(title)
    return title
def full(aspect_key):
    animal = f"{data[aspect_key]['animal']}"
    aspect = f" {data[aspect_key]['aspect']}"
    aspectTitle = title(aspect_key)
    alignment = data[aspect_key]['alignment']
    epithet = data[aspect_key]['epithet']
    if animal == "None":
        fullaspect = f"{alignment} of{aspect}"
    else:
        fullaspect = f"{animal} {alignment} of {aspect}"
    fullName = f"{aspectTitle}, {fullaspect}"
    return fullName

sinList = [
    "envy",
    "gluttony",
    "greed",
    "lust",
    "pride",
    "sloth",
    "wrath"
]
virtueList = [
    "charity",
    "chastity",
    "diligence",
    "kindness",
    "humility",
    "patience",
    "temperance"
]
html_content = f"""
<!DOCTYPE HTML>
<html>
    <head>
        <title>The Capital Aspects</title>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
        <style>
			.mono {{
				font-size: 1.5em;
				font-weight: bold;
                white-space: pre;
                font-family: monospace;
                margin-top: -3em;
                margin-left: -15em;
			}}
		</style>
        <link rel="stylesheet" href="main.css" />
        <noscript><link rel="stylesheet" href="noscript.css" /></noscript>
    </head>
    <body class="is-preload">
            <section id="sidebar">
                <div class="inner">
                    <nav>
                        <ul>
                            <li><a href="#aspect">The Capital Aspects</a></li>
                            <li><a href="#sin">The Seven Deadly Sins</a></li>
                            <li><a href="#virtue">The Seven Heavenly Virtues</a></li>
                        </ul>
                    </nav>
                </div>
            </section>
            <div id="wrapper">
"""
html_content += f"""
            <section id="aspect" class="wrapper style1 fullscreen fade-up">
                <div class="inner">
                    <h1 style="font-size: 5em;">
                        The Capital Aspects
                    </h1>
                </div>
            </section>
"""
def genAspect(aspectAlignment):
    global html_content
    if aspectAlignment == "sin":
        group = "The Seven Deadly Sins"
        list = sinList
    else:
        group = "The Seven Heavenly Virtues"
        list = virtueList
    html_content += f"""
            <section id="{aspectAlignment}" class="wrapper style3 fade-up">
                <div class="inner">
                    <h1>{escape(group)}</h1>
                    <div class="features">
                        <section>
"""
    for i in range(len(list)):
        aspect_key = list[i]
        html_content += f"""
                            <h3><a href="#{escape(aspect_key)}" class="button primary fit scrolly">{escape(title(aspect_key))}</a></h3>
"""
    html_content += f"""
                        </section>
                    </div>
                </div>
            </section>
"""
    for i in range(len(list)):
        aspect_key = list[i]
        def setData(x):
            x = str(data[aspect_key][x])
            if x == "None": x = "[N/A]"
            return x
        species = setData('species')
        power = setData('power')
        colour = setData('colour')
        weapon = setData('weapon')
        epithet = setData('epithet')
        inverse = setData('inverse')
        if aspectAlignment == "sin": inverseAspect = "virtue"
        else: inverseAspect = "sin"
        if epithet != "[N/A]": epithet = f"\"{epithet}\""
        else: epithet = ""
        fullName = full(aspect_key)
        html_content += f"""
            <section id="{escape(aspect_key)}" class="wrapper">
                <div class="inner">
                    <h1 class="major">
                        {escape(fullName)}<br>
                        {escape(epithet)}
                    </h1>
                        Species: {escape(species)}<br>
                        Superpower: {escape(power)}<br>
                        Gear Colour: {escape(colour)}<br>
                        Weapon: {escape(weapon)}<br>
                        Inverse {escape(inverseAspect.capitalize())}: <a href="#{escape(inverse)}" class="scrolly">{escape(full(inverse))}</a>
                    </p>
                </div>
            </section>
"""
genAspect("sin")
genAspect("virtue")
html_content += f"""
            </div>
            <script src="jquery.min.js"></script>
            <script src="jquery.scrollex.min.js"></script>
            <script src="jquery.scrolly.min.js"></script>
            <script src="browser.min.js"></script>
            <script src="breakpoints.min.js"></script>
            <script src="util.js"></script>
            <script src="main.js"></script>
    </body>
</html>
"""
# Define the output file name
file_name = "index.html"
# Write the HTML content to the file
with open(file_name, "w") as file:
    file.write(html_content)