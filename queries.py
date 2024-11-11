# Visualizzazione Homepage: visualizzazione della home page della web application
#in cui saranno presenti la lista di tutti i vini.

#Ricerca dei vini: ricercare uno vino specifico e visualizzazione dei dettagli.

#Ricerca ordinata: Paese

#Ricerca ordinata: Punti

#Ricerca ordinata: Prezzo

# Statistiche: Mostrare delle statistiche sui vini, come il prezzo medio per paese,
#varietà più popolari.





from mongo_connection import connect_to_collection
import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

import logging

logging.basicConfig(level=logging.DEBUG)  # Imposta il livello di log a DEBUG per vedere tutti i messaggi


#ricerca per nome
def search_title(query):
    collection = connect_to_collection()
    wine_data = collection.find({'winery': { '$regex': ".*"+query+".*"}})
    return wine_data

def allWine():
    collection = connect_to_collection()
    wines = collection.find()
    return wines

#cerca immagine vino
def search_wine_image(query):
    session = HTMLSession()
    search_url = f"https://www.bing.com/images/search?q={query}+wine"
    response = session.get(search_url)
    
    # Trova l'immagine nei risultati della ricerca
    image = response.html.find('img.mimg', first=True)
    if image:
        return image.attrs.get('src', "URL_dell_immagine_non_disponibile")
    return "URL_dell_immagine_non_disponibile"


# Consigliare: 10 vini con buon rapporto prezzo/Punti
def topValueWines():
    
    # Esegui la query per ottenere i vini con il miglior rapporto qualità/prezzo
    collection=connect_to_collection()
    logging.debug("Connected to MongoDB collection successfully.")
    
    listTop = collection.aggregate([
        {
            "$match": {
                "price": {"$ne": None},
                "points": {"$ne": None}
            }
        },
        {
            "$addFields": {
                "value_for_money": {"$divide": ["$points", "$price"]}
            }
        },
        {
            "$sort": {"value_for_money": -1}
        },
        {
            "$limit": 10
        }
    ])
    listTop=list(listTop)
    logging.debug(f"Found {len(listTop)} top value wines.")
     # Converti i risultati in una lista
    return listTop


# ordinato per prezzo
def find_wine_price():
    collection = connect_to_collection()
    queryPrice = collection.find().sort("price", -1)

    return list(queryPrice)

# range di prezzo
def find_wine_price_range(min, max):
    collection = connect_to_collection()
    query = collection.find({"price": {"$gt": min, "$lt": max}})

    return list(query)

# ordinato per punti
def find_wine_points():
    collection = connect_to_collection()
    queryPoints = collection.find().sort("points", -1)

    return list(queryPoints)

# range di punti
def find_wine_points_range(min, max):
    collection = connect_to_collection()
    query = collection.find({"points": {"$gt": min, "$lt": max}})

    return list(query)



# ordinato per paese
def find_wine_variety():
    collection = connect_to_collection()
    queryVariety = collection.find().sort("variety", 1)
    return list(queryVariety)   


def create_description_images():
    collection = connect_to_collection()
    # Leggi tutti i dati della collezione in un DataFrame pandas
    data = pd.DataFrame(list(collection.find()))


    # Grafico 2: Varietà più Popolari
    popular_varieties = data['variety'].value_counts().head(10).reset_index()
    popular_varieties.columns = ['variety', 'count']
    plt.figure(figsize=(14, 7))
    sns.barplot(x='count', y='variety', data=popular_varieties, palette='viridis')
    plt.title('Top 10 Varietà più Popolari')
    plt.xlabel('Numero di Vini')
    plt.ylabel('Varietà')
    plt.tight_layout()
    plt.savefig('popular_varieties.png')
    plt.show()

    # Grafico 3: Distribuzione dei Punti
    plt.figure(figsize=(14, 7))
    sns.histplot(data['points'], bins=20, kde=True, color='purple')
    plt.title('Distribuzione dei Punti')
    plt.xlabel('Punti')
    plt.ylabel('Frequenza')
    plt.tight_layout()
    plt.savefig('points_distribution.png')
    plt.show()

    # Grafico 4: Prezzo vs. Punti
    plt.figure(figsize=(14, 7))
    sns.scatterplot(x='price', y='points', data=data, hue='country', palette='viridis')
    plt.title('Prezzo vs. Punti')
    plt.xlabel('Prezzo')
    plt.ylabel('Punti')
    plt.legend(title='Paese', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig('price_vs_points.png')
    plt.show()
