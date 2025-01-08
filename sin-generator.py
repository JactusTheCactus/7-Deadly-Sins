import json
import re
from html import escape

def generate(combined_json_file, output_directory):
    # Open and parse the combined JSON file
    with open(combined_json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Iterate through each character in the JSON array
    for character in data:
        # Extract character details
        name = character["name"]
        sin = character["sin"]
        animal = character["animal"]
        weapon = character["weapon"]
        colour = character["colour"]
        power = character["power"]
        race = character["race"]
        
        # Construct the full name and HTML content
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
        # Replace markdown-style bold and italics with HTML tags
        html_content = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', html_content)
        html_content = re.sub(r'\*(.*?)\*', r'<i>\1</i>', html_content)

        # Define the output file name and path
        html_file = f"{output_directory}/{sin.lower().replace(' ', '_')}.html"
        
        # Write the HTML content to the file
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_content)

        print(f"HTML file generated for {sin}: {html_file}")

generate("sins/sins.json","sins/html")