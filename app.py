from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# MongoDB connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mission_to_mars"
mongo = PyMongo(app)

@app.route("/")
def index():

    mars_dict = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", mars_dict=mars_dict)

@app.route("/scrape")
def scrape():
    mars_dict = scrape_mars.scrape()

    mongo.db.collection.update({}, mars_dict, upsert=True)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)