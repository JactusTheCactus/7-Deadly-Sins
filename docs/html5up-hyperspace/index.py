import yaml
import os
from html import escape
import re
from pathlib import Path

def yaml_to_html(yaml_data, sin_key, html_file):
    sin_data = yaml_data.get(sin_key, {})
    name = sin_data.get("name","")
    if name == "" or name is None: name = "[NAME]"
    animal = sin_data.get("animal","")
    if animal == "" or animal is None: animal = "[ANIMAL]"
    sin = sin_data.get("sin","")
    if sin == "" or sin is None: sin = "[[SIN]]"
    weapon = sin_data.get("weapon","")
    if weapon == "" or weapon is None: weapon = "[WEAPON]"
    colour = sin_data.get("colour","")
    if colour == "" or colour is None: colour = "[COLOUR]"
    power = sin_data.get("power","")
    if power == "" or power is None: power = "[POWER]"
    species = sin_data.get("species","")
    if species == "" or species is None: species = "[species]"
    sex = sin_data.get("sex","")
    if sex == "f": pronouns = ["she", "her", "hers"]
    elif sex == "m": pronouns = ["he", "him", "his"]
    else: pronouns = ["they", "them", "theirs"]
    rank = sin_data.get("rank","")
    if rank == "" or rank is None: rank = "[RANK]"
    html_content = f"""<!DOCTYPE html>
<html>
	<head>
		<title>{escape(sin)}</title>
		<meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link rel="stylesheet" href="../assets/css/main.css" />
		<noscript><link rel="stylesheet" href="../assets/css/noscript.css" /></noscript>

		<style>
			.sin {{
				font-size: 1.5em;
				font-weight: bold;
			}}
		</style>
	</head>
	<body class="is-preload">
			<header id="header">
				<a href="../index.html" class="title">Home</a>
			</header>
			<div id="wrapper">
					<section id="main" class="wrapper">
						<div class="inner">
							<h1 class="major">{escape(name)}</h1>
							<p class="sin">
								{escape(name)}, The {escape(animal)} Sin of {escape(sin)}, {escape(rank)} of the Seven Deadly Sins.<br>
                                
                                Weapon: {escape(weapon)}<br>
                                Gear Colour: {escape(colour)}<br>
                                Superpower: {escape(power)}<br>
                                Species: {escape(species)}<br>
                            </p>
						</div>
					</section>
			</div>
			<script src="../assets/js/jquery.min.js"></script>
			<script src="../assets/js/jquery.scrollex.min.js"></script>
			<script src="../assets/js/jquery.scrolly.min.js"></script>
			<script src="../assets/js/browser.min.js"></script>
			<script src="../assets/js/breakpoints.min.js"></script>
			<script src="../assets/js/util.js"></script>
			<script src="../assets/js/main.js"></script>
	</body>
</html>
    """
    html_content = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', html_content)
    html_content = re.sub(r'\*(.*?)\*', r'<i>\1</i>', html_content)
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

def createfile(directory,name,type,content):
	name = f"{name}.{type}"
	with open(f"{directory}/{name}", "w") as file:
		file.write(content)

yaml_file = "sins/sins.yaml"
with open(yaml_file, 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

sinHTML =  [
     "envy",
     "gluttony",
     "greed",
     "lust",
     "pride",
     "sloth",
     "wrath"
     ]
for sin in sinHTML:
    html_file = f"docs/html5up-hyperspace/sin/{sin}.html"
    yaml_to_html(data, sin, html_file)

