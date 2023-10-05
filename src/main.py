from modules.scraper import WebScraper
from modules.spreadsheet import Spreadsheet

web_scraper = WebScraper((406, 455))
web_scraper.start()

spreadsheet = Spreadsheet(web_scraper.reports)
spreadsheet.populate()