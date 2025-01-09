import yaml
import os
from html import escape
import re
from pathlib import Path
# Function to ensure the value is not None before escaping
def safe_escape(value):
    if value is None:
        return ""  # or return a default value like "[Unknown]"
    return escape(str(value))
def get_gendered_rank(rank, sex):
    # Gender-specific rank replacements
    if sex == "F":
        if rank == "Imperatore":
            return "Imperatrix"
        elif rank == "Dominum":
            return "Domina"  # Female equivalent for 'Dominum'
        elif rank == "Venatorium":
            return "Venatoria"  # Female equivalent for 'Venatorium'
        elif rank == "Ferratorium":
            return "Ferratoria"  # Female equivalent for 'Ferratorium'
        elif rank == "Luminorium":
            return "Luminoria"  # Female equivalent for 'Luminorium'
        elif rank == "Exaltum":
            return "Exalta"  # Female equivalent for 'Exaltum'
        elif rank == "Bellatorium":
            return "Bellatoria"  # Female equivalent for 'Bellatorium'
        # Add any other specific rank changes for female here
    elif sex == "M":
        if rank == "Imperatore":
            return "Imperator"
        elif rank == "Dominum":
            return "Dominus"  # Male equivalent for 'Dominum'
        elif rank == "Venatorium":
            return "Venator"  # Male equivalent for 'Venatorium'
        elif rank == "Ferratorium":
            return "Ferrator"  # Male equivalent for 'Ferratorium'
        elif rank == "Luminorium":
            return "Luminor"  # Male equivalent for 'Luminorium'
        elif rank == "Exaltum":
            return "Exaltus"  # Male equivalent for 'Exaltum'
        elif rank == "Bellatorium":
            return "Bellator"  # Male equivalent for 'Bellatorium'
        # Add any other specific rank changes for male here
    else:
        # For neutral, just return rank as is
        return rank
def yaml_to_html(yaml_data, aspect_key, html_file):
    aspect_data = yaml_data.get(aspect_key, {})
    alignment = safe_escape(aspect_data.get("alignment",""))
    if alignment == "" or alignment is None: alignment = "[Alignment]"
    name = safe_escape(aspect_data.get("name",""))
    if name == "" or name is None: name = "[NAME]"
    animal = safe_escape(aspect_data.get("animal",""))
    if animal == "" or animal is None: animal = "[ANIMAL]"
    aspect = safe_escape(aspect_data.get("aspect",""))
    if aspect == "" or aspect is None: aspect = "[ASPECT]"
    weapon = safe_escape(aspect_data.get("weapon",""))
    if weapon == "" or weapon is None: weapon = "[WEAPON]"
    colour = safe_escape(aspect_data.get("colour",""))
    if colour == "" or colour is None: colour = "[COLOUR]"
    power = safe_escape(aspect_data.get("power",""))
    if power == "" or power is None: power = "[POWER]"
    species = safe_escape(aspect_data.get("species",""))
    if species == "" or species is None: species = "[SPECIES]"
    sex = safe_escape(aspect_data.get("sex",""))
    if sex == "f": pronouns = ["she", "her", "hers"]
    elif sex == "m": pronouns = ["he", "him", "his"]
    else: pronouns = ["they", "them", "theirs"]
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
        rank = f"{data[aspect_key]['rank']}"
        animal = f"{data[aspect_key]['animal']}"
        aspect = f"{data[aspect_key]['aspect']}"
        aspectTitle = title(aspect_key)
        alignment = data[aspect_key]['alignment']
        fullaspect = f"{animal} {alignment} of {aspect}"
        fullName = f"{aspectTitle}, {fullaspect}"
        return fullName
    html_content = f"""
<!DOCTYPE html>
<html>
	<head>
		<title>{escape(aspect)}</title>
		<meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link rel="stylesheet" href="main.css" />
		<noscript><link rel="stylesheet" href="noscript.css" /></noscript>
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
	</head>
	<body class="is-preload">
			<header id="header">
				<a href="index.html#{escape(data[aspect_key]['alignment'].lower())}" class="title" style="font-family: monospace;"><-Back</a>
			</header>
			<div id="wrapper">
					<section id="main" class="wrapper">
						<div class="inner">
							<h1 class="major">{escape(full(aspect.lower()))}</h1>
                                Species: {escape(str(data[aspect_key]['species']))}<br>
                                Superpower: {escape(str(data[aspect_key]['power']))}<br>
                                Gear-Colour: {escape(str(data[aspect_key]['colour']))}<br>
                                Weapon: {escape(str(data[aspect_key]['weapon']))}<br>
                            </p>
						</div>
					</section>
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
    html_content = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', html_content)
    html_content = re.sub(r'\*(.*?)\*', r'<i>\1</i>', html_content)
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
def createfile(directory,name,type,content):
	name = f"{name}.{type}"
	with open(f"{directory}/{name}", "w") as file:
		file.write(content)
yaml_file = "aspects.yaml"
with open(yaml_file, 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)
for aspect in data.keys():
    html_file = f"{aspect}.html"
    yaml_to_html(data, aspect, html_file)
def title(aspect):
    name = data[aspect]['name']
    if name is None:
        name = data[aspect]['aspect']
    rank = data[aspect]['rank']
    if rank is None:
        rank = ""
    sex = data[aspect]['sex']
    prefixTitles = ["Imperatore","Dominum"]
    if rank in prefixTitles:
        rank = get_gendered_rank(rank,sex)
        if name is None:
            title = rank
        else:
            title = f"{rank} {name}"
    else:
        rank = get_gendered_rank(rank,sex)
        if name is None:
            title = rank
        else:
            title = f"{name}, the {rank}"
    return title
# Define the HTML structure as a multi-line string
html_content = f"""
<!DOCTYPE HTML>
<html>
    <head>
        <title>The Capital Aspects</title>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
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
                            <h1>The Capital Aspects</h1>
                        </div>
                    </section>
"""
html_content += """
                    <section id="sin" class="wrapper style3 fade-up">
                        <div class="inner">
                            <h1>The Seven Deadly Sins</h1>
                            <div class="features">
                                <section>
                                    <h3><a href="envy.html" id="envy" class="button primary fit">{escape(title('envy'))}</a></h3>
                                    <h3><a href="gluttony.html" id="gluttony" class="button primary fit">{escape(title('gluttony'))}</a></h3>
                                    <h3><a href="greed.html" id="greed" class="button primary fit">{escape(title('greed'))}</a></h3>
                                    <h3><a href="lust.html" id="lust" class="button primary fit">{escape(title('lust'))}</a></h3>
                                    <h3><a href="pride.html" id="pride" class="button primary fit">{escape(title('pride'))}</a></h3>
                                    <h3><a href="sloth.html" id="sloth" class="button primary fit">{escape(title('sloth'))}</a></h3>
                                    <h3><a href="wrath.html" id="wrath" class="button primary fit">{escape(title('wrath'))}</a></h3>
                                </section>
                            </div>
                        </div>
                    </section>
"""
html_content += f"""
                    <section id="virtue" class="wrapper style3 fade-up">
                        <div class="inner">
                            <h1>The Seven Heavenly Virtues</h1>
                            <div class="features">
                                <section>
                                    <h3><a href="charity.html" id="charity" class="button primary fit">{escape(title('charity'))}</a></h3>
                                    <h3><a href="chastity.html" id="chastity" class="button primary fit">{escape(title('chastity'))}</a></h3>
                                    <h3><a href="diligence.html" id="diligence" class="button primary fit">{escape(title('diligence'))}</a></h3>
                                    <h3><a href="humility.html" id="humility" class="button primary fit">{escape(title('humility'))}</a></h3>
                                    <h3><a href="kindness.html" id="kindness" class="button primary fit">{escape(title('kindness'))}</a></h3>
                                    <h3><a href="patience.html" id="patience" class="button primary fit">{escape(title('patience'))}</a></h3>
                                    <h3><a href="temperance.html" id="temperance" class="button primary fit">{escape(title('temperance'))}</a></h3>
                                </section>
                            </div>
                        </div>
                    </section>
"""
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