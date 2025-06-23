import json

processed_data = dict()

with open("results/final.json", mode="r", encoding="utf-8") as f:
    data = json.load(f)

for obj in data:
    country = obj["country_name"]
    decade = int(obj["decade"])
    del obj["country_name"]
    del obj["decade"]
    if country not in processed_data:
        processed_data[country] = {decade: obj}
    else:
        processed_data[country][decade] = obj

with open("results/processed_final.json", mode="w", encoding="utf-8") as f:
    json.dump(processed_data, f)
