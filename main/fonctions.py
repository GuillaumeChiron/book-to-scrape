import csv
import requests
from bs4 import BeautifulSoup


#retourne toutes les category des livres et les stocks dans la liste "all_liste_category"
def all_category_scraper():

    url = 'https://books.toscrape.com/index.html'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")


    #recupere toutes les category de la page principale
    all_liste_category = []

    ul = soup.find_all("ul", class_="nav nav-list")
    for li in ul:
        links = li.find_all("li")
        for a in links[1:]:
            dict_category = {}
            link = a.find("a")
            link = link["href"]
            newlink = link.replace("index.html", "")
            dict_category["Lien"] = "https://books.toscrape.com/" + newlink
            all_liste_category.append(dict_category)

    return all_liste_category


#retoune la liste des liens de tous les livres du site
def category_scraper(all_liste_category):

    #recupere tous les url des livres de la page et les stock dans la liste "list_link"
    list_link = []

    for row in all_liste_category:
        base_url = row["Lien"]
        print(f"Categorie scrapé : {base_url}")
        page = 1

        #créer une boucle qui permet d'iterer de pages en pages
        while True:
            #si il y a une seule page prend "index.html" sinon prends "page-n°.html"
            if page > 1:
                url = base_url + "page-" + str(page) + ".html"
            else:
                url = base_url + "index.html"

            response = requests.get(url)

            #si la page ne repond pas stop la boucle while
            if not response.ok : 
                break

            page += 1
            soup = BeautifulSoup(response.text, "html.parser")          
            li = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

            for i in li:
                h3 = i.find_all("h3")
                for a in h3:
                    dict_link = {}
                    links = a.find("a")
                    link = links["href"]
                    link = link.replace("../../../", "")
                    dict_link["Lien"] = "https://books.toscrape.com/catalogue/" + link
                    list_link.append(dict_link)
              
    return list_link 

print(category_scraper(all_category_scraper()))


#Fonction qui permet de recupérer les données d'un seul livre et le renvoie sous forme d'un dictionnaire
def book_scraper(list_link):

    #initialise une liste vide pour y intégrer les données de chaques livres
    all_infos_products = []
    count = 1

    for row in list_link:
        url = row["Lien"]
        print(f"Données livre {count} enregistrées")
        count += 1

        response = requests.get(url)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, "html.parser")

        #initialise un dictionnaire vide
        infos_products = {}

        #recupere le titre du livre et le stock dans le dictionnaire "infos_products"
        title = soup.find("h1").string
        infos_products["Titre"] = title

        #recupere la category du livre et la stock dans le dictionnaire "infos_products"
        liste_category = []
        li = soup.find_all("li")
        for info in li:
                
            a = info.find("a")
            liste_category.append(a)

        category = (liste_category[2]).text
        infos_products["Category"] = category

        #recupere les infos du livres et de les stock dans le dictionnaire "infos_products"
        trs = soup.find_all("tr")
        for info in trs:
            if info == trs[1] or info == trs[4] or info == trs[6]:
                continue
            else:
                th = info.find("th").string
                td = info.find("td").string
                infos_products[th] = td

        #recupere le nombre l'évaluation du livre (nombre d'étoiles)
        stars = soup.find_all("p")[2]
        stars = stars["class"]
        star = stars[1]
        infos_products["Reveiw rating"] = star
        
        #recupere la description du produit et la stock dans la dictionnaire "infos_products"
        description = soup.find_all("p")[3].string
        infos_products["Description"] = description

        #ajoute l'url du livre dans le dictionnaire "infos_products"
        infos_products["URL"] = url

        #recupere l'url de l'image et la stock dans le dictionnaire "infos_products"
        image = soup.find("img")
        image = image["src"]
        image = image.replace("../../", "")
        infos_products["Image"] = "https://books.toscrape.com/" + image

        #ajoute les données d'un livre dans la liste "all_infos_products"
        all_infos_products.append(infos_products)

        with open("data.csv", "w+") as file:
            writer = csv.DictWriter(file, fieldnames=all_infos_products[0].keys())
            writer.writeheader()
            for data in all_infos_products:
                writer.writerow(data)





