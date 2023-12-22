import scrapy


class ChesscomSpider(scrapy.Spider):
    name = "chesscom"
    allowed_domains = [""]
    start_urls = ["https://www.chess.com/games/magnus-carlsen"]

    def parse(self, response):
        pass
