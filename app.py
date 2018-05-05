from flask import Flask, render_template, jsonify, redirect
#from flask_pymongo import PyMongo
import pymongo
import scrape_mars

app = Flask(__name__)

# mongo = PyMongo(app)
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.missiontomars
collection = db.stuff


@app.route("/")
def index():
    scrape_dictionary = db.collection.find_one()
    return render_template("index.html", scrape_dictionary=scrape_dictionary)


@app.route("/scrape")
def scrape():
    #listings = mongo.db.listings
    scrape_dictionary = db.collection 
    scraping_data = scrape_mars.scrape()
    scrape_dictionary.update(
        {},
        scraping_data,
        upsert=True
    )
    return redirect("http://localhost:5000/", code=302)


if __name__ == "__main__":
    app.run(debug=True)

