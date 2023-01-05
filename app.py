# app.py
from flask import Flask, request, jsonify

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
