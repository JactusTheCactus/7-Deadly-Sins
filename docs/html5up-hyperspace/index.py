import json
import os
from html import escape
import re
from pathlib import Path

def json_to_html(json_file, html_file):
    sin_data = json_data.get(sin_key, {})
    name = sin_data.get("name","")
    animal = sin_data.get("animal","")
    sin = sin_data.get("sin","")
    weapon = sin_data.get("weapon","")
    colour = sin_data.get("colour","")
    power = sin_data.get("power","")
    race = sin_data.get("race","")
    fullName = f"{name}, The {animal} Sin of {sin}"
    html_content = f"""<!DOCTYPE html>
<html>
	<head>
		<title>{escape(sin)}</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link rel="stylesheet" href="../assets/css/main.css" />
		<noscript><link rel="stylesheet" href="../assets/css/noscript.css" /></noscript>
	</head>
	<body class="is-preload">

		<!-- Header -->
			<header id="header">
				<a href="index.html" class="title">{escape(sin)}</a>
				<nav>
					<ul>
						<li><a href="../index.html">Home</a></li>
						<li><a href="../elements.html">Elements</a></li>
					</ul>
				</nav>
			</header>

		<!-- Wrapper -->
			<div id="wrapper">

				<!-- Main -->
					<section id="main" class="wrapper">
						<div class="inner">
							<h1 class="major">{escape(fullName)}</h1>
							<p>
                                Description
                            </p>
						</div>
					</section>

			</div>

		<!-- Scripts -->
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

sinHTML =  [
     "envy",
     "gluttony",
     "greed",
     "lust",
     "pride",
     "sloth",
     "wrath"
     ]
for i in range(7):
    json_file = f"sins/sins.json"
    html_file = f"docs/html5up-hyperspace/sin/{sinHTML[i]}.html"
    json_to_html(json_file, html_file)
    with open(json_file, 'r', encoding='utf-8') as f:
          data = json.load(f)