from fonctions import book_scraper
from fonctions import category_scraper
from fonctions import all_category_scraper

categories = all_category_scraper()
books = category_scraper(categories)
book_scraper(books)