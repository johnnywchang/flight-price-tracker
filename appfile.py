# app.py
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import json
import os

app = Flask(__name__)

countries = [
    {"index": 1, "name": "Thailand", "price": 500},
    {"index": 2, "name": "Australia", "price": 700},
    {"index": 3, "name": "Egypt", "price": 900},
]

def _find_next_id():
    return max(country["index"] for country in countries) + 1

@app.get("/countries")
def get_countries():
    return jsonify(countries)

@app.post("/countries")
def add_countries():
    if request.is_json:
        country_list = request.get_json()
        for c in country_list:
            if c['price'] is not None:
                c['index']=_find_next_id()
                countries.append(c)
        return countries, 201
    return {"error": "Request must be JSON"}, 415


#@app.get("/data")
#def get_files():
#    return jsonify(countries)

#@app.route("/data", methods=['GET', 'POST'])
#def add_files():
#    with open("all_countries.json", 'w') as file:
#        json.dump(countries, file)
#    return "all_countries.json"

@app.route("/data")
def create_files():
    with open( "allcountries.json" , "w") as write:
        json.dump( countries, write )
    return os.listdir()

@app.post("/data")
def update_files():
    with open("allcountries.json") as f:
        datafile = json.load(f)
        if request.is_json:
            country_list = request.get_json()
            newindex=max(i["index"] for i in datafile)+1
            for c in country_list:
                if c['price'] is not None:
                    c['index']=newindex
                    newindex += 1
                    datafile.append(c)
    with open("allcountries.json", "w") as f:
        json.dump(datafile, f, indent=4)
    f.close()
    return f