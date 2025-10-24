# book-to-scrape

Ce projet est un **scraper Python** permettant d’extraire automatiquement toutes les données du site [Books to Scrape](https://books.toscrape.com), y compris les catégories, les informations détaillées des livres et leurs images.  

Les données sont enregistrées sous forme de fichiers **CSV** par categories et les **images** téléchargées.

---

## Fonctionnalités

- Récupération de **toutes les catégories** de livres  
- Extraction de **tous les livres** de chaque catégorie  
- Enregistrement des données (titre, prix, description, etc.) au format **CSV**  
- Téléchargement des **images** associées  
- Enregistrement des fichiers dans un dossier `data/`

---

## Packages utilisées

- Python 3.11+
- [Requests](https://docs.python-requests.org/)
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)
- [CSV](https://docs.python.org/3/library/csv.html)
- [OS](https://docs.python.org/3/library/os.html)
- [re](https://docs.python.org/3/library/re.html)

---

## Fonctionnement global

Le script `main.py` execute ces fonctions dans l’ordre suivant :

1. `all_category_scraper()` : récupère toutes les catégories  
2. `category_scraper()` : récupère les livres de chaque catégorie  
3. `book_scraper()` : extrait et enregistre les informations de chaque livre  

À la fin, toutes les données sont sauvegardées dans le dossier `data/`.

---

## Installation

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/GuillaumeChiron/book-to-scrape.git
   cd book_to_scrape

---

## Utilisation

1. Exécute le script principal :
   ```bash
   python main.py

2.  Retour attendu : 
    
    Résultat : 

    Catégorie scrapé : "nom de la categorie"
    Données livre "n°" enregistrées
    ...
    Scraping terminé