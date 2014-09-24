import random
import haartracht
import bart
import gesichtsmerkmal
import stand
import beruf
import besonderheiten
import darstellung


def weighted_choice(choices):
   total = sum(w for c, w in choices)
   r = random.uniform(0, total)
   upto = 0
   for c, w in choices:
      if upto + w > r:
         return c
      upto += w
   assert False, "Shouldn't get here"

Haarfarbe = [['schwarz',6],['dunkelbraun',6],['braun',6],['hellbraun',6],['dunkelblond',4],['mittelblond',4],['hellblond',4],['rotbraun',1],['rotblond',1],['rot',2]]

Augenfarbe = {
              'schwarz':[['schwarz',5],['braun',11],['grün',3],['blau',1]],
              'dunkelbraun':[['schwarz',2],['braun',11],['grün',5],['blau',2]],
              'braun':[['schwarz',2],['braun',11],['grün',4],['blau',3]],
              'hellbraun':[['schwarz',2],['braun',8],['grün',5],['blau',4],['grau',1]],
              'dunkelblond':[['braun',7],['grün',6],['blau',5],['grau',2]],
              'mittelblond':[['braun',6],['grün',6],['blau',6],['grau',2]],
              'hellblond':[['braun',3],['grün',5],['blau',7],['grau',5]],
              'rotbraun':[['braun',6],['grün',10],['blau',3],['grau',1]],
              'rotblond':[['braun',6],['grün',10],['blau',3],['grau',1]],
              'rot':[['braun',5],['grün',11],['blau',3],['grau',1]]
              }


def parseAuswahl(Liste):
    templist = []
    for value, key in Liste.items():
        if '-' in key:
            templist.append([value, 1+int(key.split('-')[0])-int(key.split('-')[1])])
        else:
            templist.append([value, 1])
    return templist
  
Haartracht_m = parseAuswahl(haartracht.Haartracht_m_temp)
Haartracht_w = parseAuswahl(haartracht.Haartracht_w_temp)
  
Barttracht_m = parseAuswahl(bart.Barttracht_m_temp)
Barttracht_w = parseAuswahl(bart.Barttracht_w_temp)

Gesichtsmerkmale = parseAuswahl(gesichtsmerkmal.gesichtsmerkmal_temp)
Stand = parseAuswahl(stand.stand_temp)
Besonderheiten = parseAuswahl(besonderheiten.besonderheiten_temp)
Darstellungen = parseAuswahl(darstellung.darstellung_temp)

Beruf = {}
for key, value in beruf.berufe_temp.items():
    Beruf[key] = parseAuswahl(value)
        
class NSC():
    def __init__(self):
        self.Geschlecht = random.choice(['männlich', 'weiblich'])
        self.Altersklasse = weighted_choice([['Kind',2],['Jugendlich', 4],['Erwachsen',12],['Senior',2]])
        if self.Altersklasse == 'Kind':
            self.Alter = random.randint(1,10)
        if self.Altersklasse == 'Jugendlich':
            self.Alter = random.randint(1,10) + 10
        if self.Altersklasse == 'Erwachsen':
            self.Alter = random.randint(1,10) + random.choice([2,2,3,3,4,5])*10
        if self.Altersklasse == 'Senior':
            self.Alter = random.randint(1,10) + random.choice([6,6,6,6,6,7,7,7,8,9])*10
        self.Körpergröße = weighted_choice([['klein',2],['unterdurchschnittlich groß',3],['normal',10],['überdurchschnittlich groß',3],['riesig',2]])  
        self.Körperbau = weighted_choice([['dürr',2],['schlank',3],['normal gebaut',7],['dicklich',3],['fett',1],['athletisch gebaut', 3],['deutlich muskulös',1]])
        self.Haarfarbe = weighted_choice(Haarfarbe)
        self.Augenfarbe = weighted_choice(Augenfarbe[self.Haarfarbe])
        if self.Geschlecht == 'weiblich':
            self.Haartracht = weighted_choice(Haartracht_w)
        else:            
            self.Haartracht = weighted_choice(Haartracht_m)          
        if self.Geschlecht == 'weiblich' and self.Alter > 15:
            self.Barttracht = weighted_choice(Barttracht_w)
        elif self.Alter > 15:
            self.Barttracht = weighted_choice(Barttracht_m)
        else:
            self.Barttracht = 'kein Bart'
        self.Gesichtsmerkmal = ''
        x = random.randint(1,20)
        if x > 4:
            self.Gesichtsmerkmal = weighted_choice(Gesichtsmerkmale)      
        if x == 20:
            self.Gesichtsmerkmal += ', ' + weighted_choice(Gesichtsmerkmale)
        self.Stand = weighted_choice(Stand)
        self.Beruf = weighted_choice(Beruf[self.Stand])
        
        if 'Mittelschichtberuf' in self.Beruf:
            self.Beruf += ': ' + weighted_choice(Beruf['Mittelschicht'])
        if 'Oberschichtberuf' in self.Beruf:
            self.Beruf += ': ' + weighted_choice(Beruf['Oberschicht'])        
        x = random.randint(1,20)
        self.Besonderheit = ''
        if x > 4:
            self.Besonderheit = weighted_choice(Besonderheiten)      
        if x == 20:
            self.Besonderheit += ', ' + weighted_choice(Besonderheiten)
            
        self.Darstellung = weighted_choice(Darstellungen)
            
alrik = NSC()
print(alrik.Geschlecht, alrik.Altersklasse, alrik.Alter, alrik.Körpergröße)
print(alrik.Haarfarbe, alrik.Augenfarbe,  alrik.Körperbau, alrik.Haartracht, alrik.Barttracht)
print(alrik.Gesichtsmerkmal, alrik.Stand, alrik.Beruf, alrik. Besonderheit, alrik.Darstellung)
        
        
