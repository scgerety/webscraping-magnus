import scrapy
import os
import sqlite3

current_directory = os.path.dirname(__file__)
url = os.path.join(current_directory, "magnus-download.html")

class ChesscomSpider(scrapy.Spider):
    name = "chesscom"
    allowed_domains = [""]
    start_urls = [f"file://{url}"]

    def parse(self, response):
        for child in response.xpath('//table'):
            if len(child.xpath('tr')) >=10:
                table = child
                break
        tablehead = response.xpath('//table')[0].xpath('thead')
        headers = [th.extract() for th in tablehead.xpath('tr').xpath('th/text()')]

