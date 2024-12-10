import csv
import requests
lst1 = []
def results():
    i = 1
    while i < 42:
        res = requests.get(f'https://rickandmortyapi.com/api/character?page={i}')
        lst = res.json()['results']
        for character in lst:
            res1 = {k: character[k] for k in ['origin', 'name', 'status', 'species', 'location', 'image'] if k in character}
            if res1.get("species") == "Human" and res1.get("status") == "Alive":
                if isinstance(res1.get("origin"), dict) and "Earth" in res1["origin"].get("name", ""):
                    lst1.append([res1["name"], res1["location"].get("name", ""), res1["image"]])
        i += 1
    return(lst1)