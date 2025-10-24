# book-to-scrape

Ce projet est un **scraper Python** permettant d’extraire automatiquement toutes les données du site [Books to Scrape](https://books.toscrape.com), y compris les catégories, les informations détaillées des livres et leurs images.  

Les données sont enregistrées sous forme de fichiers **CSV** par categories et les **images** téléchargées.

---

## Fonctionnalités

- Récupération automatique de **toutes les catégories** de livres  
- Extraction de **tous les livres** de chaque catégorie  
- Enregistrement des données (titre, prix, description, etc.) au format **CSV**  
- Téléchargement des **images** associées  
- Organisation automatique des fichiers dans un dossier `data/`

---

## Technologies utilisées

- Python 3.11+
- [Requests](https://docs.python-requests.org/)
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)
- [CSV](https://docs.python.org/3/library/csv.html)
- [OS](https://docs.python.org/3/library/os.html)
- [re](https://docs.python.org/3/library/re.html)

---

## Installation

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/GuillaumeChiron/book-to-scrape.git
   cd book_to_scrape

## Utilisation

1. Exécute le script principal :
   ```bash
   python main.py

2.  Retour attendu : 
    
    Résultat : Scraping terminé