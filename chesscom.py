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
        table = "CREATE TABLE magnus ([Player1] TEXT, [Rating1] TEXT, [Player2] TEXT, [Rating2] TEXT, [OpeningMoves] TEXT, [OpeningName] TEXT, [Result] TEXT, [NumMoves] TEXT, [Year] TEXT)"
        connection = sqlite3.connect("chesscom.db")

        tbody = response.xpath('//table')[0].xpath('//tbody')[0]
        for row in tbody.xpath('//tr'):
            player1, rating1, player2, rating2 = [cell.xpath('a/div/span/text()').extract() for cell in row.xpath('td')]
            opening_moves = row.xpath(td/a)[1].xpath('span/text()')[0].extract()
            opening_name = row.xpath(td/a)[1].xpath('span/text()')[1].extract()
            result = tbody.xpath('//tr').xpath('td')[1].xpath('a/text()')[0].extract()
            moves = tbody.xpath('//tr').xpath('td')[2].xpath('a/text()')[0].extract()
            year = tbody.xpath('//tr').xpath('td')[3].xpath('a/text()')[0].extract()
            

