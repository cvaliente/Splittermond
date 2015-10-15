import json
from pprint import pprint

json_data=open('zauber.json').read()

data = json.loads(json_data)
print(data['Zunge des Diplomaten']['Dauer'])
keys =['name', 'schulen', 'Typus', 'Schwierigkeit', 'Zauberkosten', 'Dauer', 'Reichweite', 'Optionen', 'Wirkung', 'Wirkungsdauer', 'Verstärkt']


for zauber in data:
    for key in keys:
        print(key, data[zauber][key])
