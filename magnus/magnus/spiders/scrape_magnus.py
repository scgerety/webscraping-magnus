"""
scrape_magnus.py fetches html from chess.com on Magnus Carlsen's games and persists that into a local 
document for later use.
"""

import requests

html = requests.get("https://www.chess.com/games/magnus-carlsen")
with open("magnus-download", "w") as _f:
    _f.write(html.text)
