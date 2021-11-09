{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, jsonify, render_template\n",
    "from flask_pymongo import PyMongo\n",
    "\n",
    "import scrape_mars\n",
    "\n",
    "#make an app instance\n",
    "app = Flask(__name__)\n",
    "\n",
    "mongo = PyMongo(app)\n",
    "\n",
    "'''Define the Routes'''\n",
    "\n",
    "#index\n",
    "@app.route('/')\n",
    "def index():\n",
    "    mars = mongo.db.mars.find_one()\n",
    "    return render_template('index.html', mars=mars)\n",
    "\n",
    "@app.route('/scrape')\n",
    "def scraper():\n",
    "    mars = mongo.db.mars\n",
    "    mars_data = scrape_mars.scrape()\n",
    "    #update the mars db w/ mars_data\n",
    "    mars.update({}, mars_data, upsert=True)\n",
    "    return index()\n",
    "\n",
    "#run the app\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:PythonData] *",
   "language": "python",
   "name": "conda-env-PythonData-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
