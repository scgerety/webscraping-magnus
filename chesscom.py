import scrapy
import os
import sqlite3

current_directory = os.path.dirname(__file__)
url = os.path.join(current_directory, "magnus-download")

class ChesscomSpider(scrapy.Spider):
    name = "chesscom"
    allowed_domains = [""]
    start_urls = [f"file://{url}"]

    def parse(self, response):
        pass
