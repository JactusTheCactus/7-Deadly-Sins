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

def full(sin):
    if data[sin]['name'] is not None:
        name = f"{data[sin]['name']}"
    else:
        name = f"{sin.capitalize()}"
    name = f"{name}"
    rank = f"{data[sin]['rank']}"
    prefixTitles = ["Imperatore","Dominum"]
    if rank in prefixTitles:
        title = f"{rank} {name}"
    else: title = f"{name}, the {rank}"
    rank = f"{get_gendered_rank(data[sin]['rank'],data[sin]['sex'])}"
    animal = f"{data[sin]['animal']}"
    sin = f"{data[sin]['sin']}"
    fullName = f"{title}, {animal} sin of {sin}"
    return fullName

def yaml_to_html(yaml_data, sin_key, html_file):
    sin_data = yaml_data.get(sin_key, {})
    name = sin_data.get("name","")
    if name == "" or name is None: name = "[NAME]"
    animal = sin_data.get("animal","")
    if animal == "" or animal is None: animal = "[ANIMAL]"
    sin = sin_data.get("sin","")
    if sin == "" or sin is None: sin = "[SIN]"
    weapon = sin_data.get("weapon","")
    if weapon == "" or weapon is None: weapon = "[WEAPON]"
    colour = sin_data.get("colour","")
    if colour == "" or colour is None: colour = "[COLOUR]"
    power = sin_data.get("power","")
    if power == "" or power is None: power = "[POWER]"
    species = sin_data.get("species","")
    if species == "" or species is None: species = "[SPECIES]"
    sex = sin_data.get("sex","")
    if sex == "f": pronouns = ["she", "her", "hers"]
    elif sex == "m": pronouns = ["he", "him", "his"]
    else: pronouns = ["they", "them", "theirs"]
    rank = sin_data.get("rank","")
    if rank == "" or rank is None: rank = "[RANK]"

    html_content = f"""
<!DOCTYPE html>
<html>
	<head>
		<title>{escape(sin)}</title>
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
				<a href="index.html#sins" class="title" style="font-family: monospace;"><-Back</a>
			</header>
			<div id="wrapper">
					<section id="main" class="wrapper">
						<div class="inner">
							<h1 class="major">{escape(full(sin.lower()))}</h1>
							<p class="mono">
                                Species:        {escape(species)}
                                Superpower:     {escape(power)}
                                Gear-Colour:    {escape(colour)}
                                Weapon:         {escape(weapon)}
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

yaml_file = "sins.yaml"
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
    html_file = f"{sin}.html"
    yaml_to_html(data, sin, html_file)

# Define the HTML structure as a multi-line string
html_content = f"""
<!DOCTYPE HTML>
<!--
    Hyperspace by HTML5 UP
    html5up.net | @ajlkn
    Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
-->
<html>
    <head>
        <title>The Seven Deadly Sins</title>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
        <link rel="stylesheet" href="main.css" />
        <noscript><link rel="stylesheet" href="noscript.css" /></noscript>
    </head>
    <body class="is-preload">

        <!-- Header -->
        <header id="header">
            <nav>
                <ul>
                </ul>
            </nav>
        </header>

        <!-- Sidebar -->
            <section id="sidebar">
                <div class="inner">
                    <nav>
                        <ul>
                            <li><a href="#home">Home</a></li>
                            <li><a href="#sins">The Sins</a></li>
                        </ul>
                    </nav>
                </div>
            </section>

        <!-- Wrapper -->
            <div id="wrapper">

                <!-- Intro -->
                    <section id="home" class="wrapper style1 fullscreen fade-up">
                        <div class="inner">
                            <h1>The Seven Deadly Sins</h1>
                            <p><!--Description--></p>
                        </div>
                    </section>

                <!-- The Sins -->
                    <section id="sins" class="wrapper style3 fade-up">
                        <div class="inner">
                            <p><!--Description--></p>
                            <div class="features">
                                <!-- Icons
                                 <span class="icon solid major fa-code"></span>
                                 <span class="icon solid major fa-lock"></span>
                                 <span class="icon solid major fa-cog"></span>
                                 <span class="icon solid major fa-desktop"></span>
                                 <span class="icon solid major fa-link"></span>
                                 <span class="icon major fa-gem"></span>
                                 -->
                                <section>
                                    <h3><a href="envy.html" id="envy" class="button primary fit">{escape(full('envy'))}</a></h3>
                                    <h3><a href="gluttony.html" id="gluttony" class="button primary fit">{escape(full('gluttony'))}</a></h3>
                                    <h3><a href="greed.html" id="greed" class="button primary fit">{escape(full('greed'))}</a></h3>
                                    <h3><a href="lust.html" id="lust" class="button primary fit">{escape(full('lust'))}</a></h3>
                                    <h3><a href="pride.html" id="pride" class="button primary fit">{escape(full('pride'))}</a></h3>
                                    <h3><a href="sloth.html" id="sloth" class="button primary fit">{escape(full('sloth'))}</a></h3>
                                    <h3><a href="wrath.html" id="wrath" class="button primary fit">{escape(full('wrath'))}</a></h3>
                                </section>
                            </div>
                        </div>
                    </section>

            </div>

        <!-- Scripts -->
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
