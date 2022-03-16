from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import datetime as dt

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
#pass 
mongo = PyMongo(app)


# make routes
# main page; call html here to display
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    #mars = mongo.db.mars.find_all()
    #mars = scrape_mars.scrape()
    return render_template("index.html", dict=mars)

# scrape to call the get all function in py
@app.route("/scrape")
def scrapper():
    #conn = "mongodb://localhost:27017"
    #client = pymongo.MongoClient(conn)
    #db = client.mars_db
    #allows for repetition
    #db.mars.drop()
    #db.mars.insert_one(mars_info)
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape()
    mars.update_one({}, {"$set": mars_data}, upsert=True)
    return redirect("/",code=302)

# Define Main Behavior
if __name__ == "__main__":
    app.run()