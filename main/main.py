from fonctions import (
    book_scraper,
    category_scraper,
    all_category_scraper,
)


categories = all_category_scraper()
for row in categories[:3]:
    books = category_scraper(row["Category"], row["Lien"])
    book_scraper(books)

print("Scraping terminé.")
