import csv
import requests
from bs4 import BeautifulSoup



#Fonction qui permet de recupérer les données d'un seul livre et le renvoie sous forme d'un dictionnaire
def book_scraper(list_link):

    #initialise une liste vide pour y intégrer les données de chaques livres
    all_infos_products = []

    for row in list_link:
        url = row["Lien"]

        response = requests.get(url)
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
            th = info.find("th").string
            td = info.find("td").string
            infos_products[th] = td

        #recupere l'url de l'image et la stock dans le dictionnaire "infos_products"
        image = soup.find("img")
        image = image["src"]
        image = image.replace("../../", "")
        infos_products["Image"] = "https://books.toscrape.com/" + image


        #recupere la description du produit et la stock dans la dictionnaire "infos_products"
        description = soup.find_all("p")[3].string
        infos_products["Description"] = description

        #ajoute les données d'un livre dans la liste "all_infos_products"
        all_infos_products.append(infos_products)

    with open("data.csv", "w+") as file:
        writer = csv.DictWriter(file, fieldnames=all_infos_products[0].keys())
        writer.writeheader()
        writer.writerows(all_infos_products)

    print("Données enregistrées !!!")


def category_scraper():

    url = 'https://books.toscrape.com/catalogue/category/books/classics_6/index.html'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    #recupere tous les url des livres de la page et les stock dans la liste "list_link"
    list_link = []

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


    





