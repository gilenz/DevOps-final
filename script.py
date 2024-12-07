#import csv
import requests
import json
res = requests.get('https://rickandmortyapi.com/api/character')
lst = res.json()['results']
lst1 = []
def results():
    for i in lst:
        res1 = dict((k, i[k]) for k in ['origin','name', 'status', 'species','location', 'image'] if k in i)
        if res1["species"] == "Human" and res1["status"] == "Alive":
            if "Earth" in res1["origin"]["name"]:
                lst1.append([res1["name"],res1["location"]["name"],res1["image"]])
    json_str = json.dumps(lst1)
    return(json_str)
#with open('results.csv', 'w', newline='') as csvfile:
 #   writer = csv.writer(csvfile)
 #   writer.writerows(lst1)