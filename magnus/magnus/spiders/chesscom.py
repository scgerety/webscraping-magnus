"""
chesscom.py parses a local html file, magnus-download.html, which is scraped using a different module.
This program persists the data in a sqlite database.
"""

# Import necessary libraries
import scrapy
import os
import sqlite3

# Point toward the correct html file
current_directory = os.path.dirname(__file__)
url = os.path.join(current_directory, "magnus-download.html")

# Create a Spider for parsing
class ChesscomSpider(scrapy.Spider):
    name = "chesscom"
    allowed_domains = [""]
    start_urls = [f"file://{url}"] # points to file on line in "url" variable

    def parse(self, response):
        # # Find a reasonably-sized table
        # for child in response.xpath('//table'):
        #     if len(child.xpath('tr')) >=10:
        #         table = child
        #         break
        
        # # Find table heads (commented out)
        # tablehead = response.xpath('//table')[0].xpath('thead')
        # headers = [th.extract() for th in tablehead.xpath('tr').xpath('th/text()')]
        
        # Set up table creation and query
        magnus_db = "CREATE TABLE magnus ([Player1] TEXT, [Rating1] TEXT, [Player2] TEXT, [Rating2] TEXT, [OpeningMoves] TEXT, [OpeningName] TEXT, [Result] TEXT, [NumMoves] TEXT, [Year] TEXT)"
        query = "INSERT INTO magnus ([Player1], [Rating1], [Player2], [Rating2], [OpeningMoves], [OpeningName], [Result]) VALUES (?, ?, ?, ?, ?, ?, ?)"
        connection = sqlite3.connect("chesscom.db")
        cursor = connection.cursor()

        # Create table
        cursor.execute(magnus_db)
        connection.commit()

        tbody = response.xpath('//table')[0].xpath('//tbody')[0] # 
        for row in tbody.xpath('//tr'):
            player1, rating1, player2, rating2 = [cell.xpath('a/div/span/text()').extract() for cell in row.xpath('td')]
            opening_moves = row.xpath(td/a)[1].xpath('span/text()')[0].extract()
            opening_name = row.xpath(td/a)[1].xpath('span/text()')[1].extract()
            result = tbody.xpath('//tr').xpath('td')[1].xpath('a/text()')[0].extract()
            moves = tbody.xpath('//tr').xpath('td')[2].xpath('a/text()')[0].extract()
            year = tbody.xpath('//tr').xpath('td')[3].xpath('a/text()')[0].extract()
            cursor.execute(query, (player1, rating1, player2, rating2, opening_moves, opening_name, result, moves, year))
            connection.commit()

