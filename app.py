from flask import Flask, render_template, request
import queries  

app = Flask(__name__)

@app.route('/')
def index():

    #top 10 vini
    listaTops = queries.topValueWines()
    if listaTops:
            # Ottieni l'URL dell'immagine per i vini trovato
            img_results = []
            for result in listaTops:
                result["img_url"] = queries.search_wine_image(result['title'])
                img_results.append(result)
            #wine['img_url'] = "" #img_url  # Aggiungi l'URL dell'immagine al vino trovato
            return render_template('index.html', listaTops=img_results)
    #return render_template('index.html', listaTops=listaTops)
   # return render_template('index.html')


@app.route('/search_title')
def search():
    query = request.args.get('query')
    if query:
        results = queries.search_title(query)
        if results:
            # Ottieni l'URL dell'immagine per i vini trovato
            img_results = []
            for result in results:
                result["img_url"] = queries.search_wine_image(result['title'])
                img_results.append(result)
            #wine['img_url'] = "" #img_url  # Aggiungi l'URL dell'immagine al vino trovato
            return render_template('search_result.html', results=img_results)
        else:
            return "Nessun risultato trovato"
    else:
        return  render_template('wine_list.html', results=result) #controllare
    
@app.route('/wine_list')
def allWine():
    #query = request.args.get('query')
    listawine= queries.allWine()
    return render_template('wine_list.html', listawine=listawine)

@app.route('/search_price')
def search_price():
    wines = queries.find_wine_price()
    return render_template('wine_list.html', listawine=wines)

@app.route('/search_points')
def search_points():
    wines = queries.find_wine_points()
    return render_template('wine_list.html', listawine=wines)

@app.route('/search_variety')
def search_variety():
    wines = queries.find_wine_variety()
    return render_template('wine_list.html', listawine=wines)

@app.route('/statistiche')
def statistiche():
    return render_template('statistiche.html')

if __name__ == '__main__':
    app.run(port=5000)


