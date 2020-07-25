from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrape_mars
from pymongo import MongoClient


app = Flask(__name__)


app.config["MONGO_URI"] = "mongodb+srv://pharmon9847:ljcx7R9iOsO8oH0b@cluster1.xhk0t.mongodb.net/mars_app?retryWrites=true&w=majority"

mongo = PyMongo(app)
print(mongo)
#client = MongoClient("mongodb+srv://pharmon9847:ljcx7R9iOsO8oH0b@cluster1.xhk0t.mongodb.net/test?retryWrites=true&w=majority")
#db = client.mars_app

#db.mars_app.drop()

# Use flask_pymongo to set up mongo connection
#app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
#mongo = PyMongo(app)
#print(mongo)
# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)


@app.route("/scrape")
def scrape():
    #mars = mongo.db.mars
    #mars_data = scrape_mars.scrape_all()
    #mars.replace_one({}, mars_data, upsert=True)
    #return "Scraping Successful!"
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8070, debug=True)
    #app.run(debug=True)
