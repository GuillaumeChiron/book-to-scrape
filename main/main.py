import csv
import requests
from bs4 import BeautifulSoup
from fonctions import *


category_scraper()
book_scraper(category_scraper())