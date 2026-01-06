import json

def save_to_json(data, filename="news.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def load_from_json(filename="news.json"):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
