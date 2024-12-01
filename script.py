import requests
res = requests.get('https://rickandmortyapi.com/api/character')
lst = res.json()['results']
lst1 = []
for i in lst:
    res1 = dict((k, i[k]) for k in ['origin','name', 'status', 'species','location', 'image'] if k in i)
    if res1["species"] == "Human" and res1["status"] == "Alive":
        if "Earth" in res1["origin"]["name"]:
            print(res1["name"],res1["location"]["name"],res1["image"])