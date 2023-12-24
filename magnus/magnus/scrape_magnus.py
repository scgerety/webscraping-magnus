"""
scrape_magnus.py fetches html from chess.com on Magnus Carlsen's games and persists that into a local 
document for later use.
"""

import requests
import os

current_directory = os.path.dirname(__file__)
file = os.path.join(current_directory, "spiders/magnus-download.html")

html = requests.get("https://www.chess.com/games/magnus-carlsen")
with open(file, "w") as _f:
    _f.write(html.text)
