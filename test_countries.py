import json

f = open('skyscanner_dallas.json', 'rt')

country_list = json.load(f)

countries = [
    {"index": 1, "name": "Thailand", "price": 500},
    {"index": 2, "name": "Australia", "price": 700},
    {"index": 3, "name": "Egypt", "price": 900},
]

def _find_next_id():
    return max(country["index"] for country in countries) + 1

for i in country_list:
    if i['price'] is not None:
        i['index']=_find_next_id()
        countries.append(i)

print(countries)
