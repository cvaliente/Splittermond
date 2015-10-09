import requests
from pprint import pprint
import json

splitterwikijson = 'http://splitterwiki.de/w/index.php?title=Spezial:Ask&x=-5B-5BKategorie%3AZauber-5D-5D%2F-3F%3DZauber-23%2F-3FBeteiligte-20Werte%2F-3FHGS%2F-3FHatMagieschuleMitZaubergrad%2F-3FHauptkategorie%2F-3FMagieschule1%2F-3FMagieschule2%2F-3FMagieschule3%2F-3FMutterseite%2F-3FReichweite%2F-3FSeitentitel%2F-3FVaterseiten%2F-3FWirkungsbereich%2F-3FWirkungsdauer%2F-3FWirkungsdauerEinheit%2F-3FWirkungsdauerMitEinheit%2F-3FZauberHatMagieschule%2F-3FZauberart%2F-3FZauberdauer%2F-3FZauberdauerMitEinheit%2F-3FZaubergrad1%2F-3FZaubergrad2%2F-3FZaubergrad3%2F-3FZauberkosten%2F-3FZauberkostenMitVerst%C3%A4rken%2F-3FZauberkostenNurVerst%C3%A4rken%2F-3FZauberoption%2F-3FZauberoptionFlacheListe%2F-3FZauberreichweite%2F-3FZauberschwierigkeit%2F-3FZaubertypus%2F-3FZaubertypusFlacheListe%2F-3FZauberverst%C3%A4rkungWirkung%2F-3FZauberwirkung%2F-3FZuletzt-20ge%C3%A4ndert&format=json&limit=100&link=none&headers=plain&mainlabel=Zauber&searchlabel=Zauber%20-%20alle%20Zauber%20mit%20allen%20Attributen%20-%20JSON-Format&offset='
keys =['Zauberwirkung','HatMagieschuleMitZaubergrad', 'ZaubertypusFlacheListe', 'Zauberschwierigkeit', 'Zauberkosten','ZauberkostenMitVerstärken', 'ZauberdauerMitEinheit', 'Reichweite', 'ZauberoptionFlacheListe', 'WirkungsdauerMitEinheit', 'ZauberverstärkungWirkung']

SCZauber = ['Eiserne Aura', 'Haarfarbe']

zauberbuch = {}
for i in range(0,3):
    zauberbuch.update(json.loads(requests.get(splitterwikijson+str(i*100)).text)['results'])
    
for zauber in SCZauber:
    print(zauberbuch[zauber]['fulltext'])    
    for key in keys:
        if zauberbuch[zauber]['printouts'][key]:
            print(key, zauberbuch[zauber]['printouts'][key][0])
           
