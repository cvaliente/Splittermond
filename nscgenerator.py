import random

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

Haartracht_w_temp = {'2-1':'Igelfrisur',
'6-3':'Seitenscheitel, kurz',
'8-7':'Seitenscheitel, schlecht geschnitten',
'10-9':'Mittelscheitel, kurz',
'2-1':'Mittelscheitel, kurz',
'4-3':'Mittelscheitel, schlecht geschnitten',
'5':'Seitenscheitel, schlecht geschnitten',
'6':'Mittelscheitel, schlecht geschnitten (Fransen)',
'8-7':'Seitenscheitel, an den Schläfen kurz rasiert',
'10-9':'Mittelscheitel, an den Schläfen kurz rasiert',
'1':'Seitenscheitel, schlecht geschnitten, an den Schläfen kurz rasiert',
'2':'Mittelscheitel, schlecht geschnitten, an den Schläfen kurz rasiert',
'5-3':'Prinz-Eisenherz-Frisur',
'7-6':'gezähmte Lockenpracht, lang',
'10-8':'Lockenpracht, lang',
'1':'Lockenpracht, lang',
'3-2':'ungezähmte Lockenpracht, lang',
'5-4':'ungezähmter Lockenkopf, mittellang',
'10-5':'Lockenkopf, mittellang',
'1':'Lockenpracht, unter Kopftuch',
'2':'ungezähmter Lockenkopf, kurz',
'6-3':'Lockenkopf, kurz',
'9-7':'Mittellange Haare (bis Kinn), ins Gesicht fallend',
'10':'Mittellange Haare (bis Kinn), Pony',
'2-1':'Mittellange Haare (bis Kinn), Pony',
'5-3':'Mittellange Haare (bis Kinn), gescheitelt',
'8-6':'Mittellange Haare (bis Kinn), Mittelscheitel',
'10-9':'Mittellange Haare (bis Kinn), Haarreif',
'1':'Mittellange Haare (bis Kinn), Haarreif',
'4-2':'Mittellange Haare (bis Kinn), nach hinten gekämmt',
'7-5':'Mittellange Haare (bis Kinn), unter Kopftuch',
'10-8':'Mittellange Haare (bis Kinn), mit Haarspange',
'3-1':'Mittellange Haare (bis Kinn), mit Haarband',
'6-4':'Mittellange Haare (bis Kinn), mit Haarbändern',
'9-7':'Mittellange Haare (bis Kinn), dicker Zopf',
'10':'Mittellange Haare (bis Kinn), zwei Zöpfe',
'2-1':'Mittellange Haare (bis Kinn), zwei Zöpfe',
'5-3':'Mittellange Haare (bis Kinn), viele Zöpfe',
'8-6':'Zöpfe mit Haarnadeln am Kopf befestigt',
'10-9':'Mittellange Haare (bis Kinn), unter Kopftuch',
'1':'Mittellange Haare (bis Kinn), unter Kopftuch',
'4-2':'Mittellange Haare (bis Kinn), unter Haube',
'7-5':'Mittellange gewellte Haare (bis Kinn), ins Gesicht fallend',
'10-8':'Mittellange gewellte Haare (bis Kinn), gescheitelt',
'3-1':'Mittellange gewellte Haare (bis Kinn), Pony',
'6-4':'Mittellange gewellte Haare (bis Kinn), Mittelscheitel',
'9-7':'Mittellange gewellte Haare (bis Kinn), Haarreif',
'10':'Mittellange gewellte Haare (bis Kinn), Haarspange',
'2-1':'Mittellange gewellte Haare (bis Kinn), Haarspange',
'5-3':'Mittellange gewellte Haare (bis Kinn), Haarband',
'8-6':'Mittellange gewellte Haare (bis Kinn), Haarbänder',
'10-9':'Lange Haare (Schulterlang), ins Gesicht fallend',
'1':'Lange Haare (Schulterlang), ins Gesicht fallend',
'4-2':'Lange Haare (Schulterlang), gescheitelt',
'7-5':'Lange Haare (Schulterlang), nach hinten gekämmt',
'10-8':'Lange Haare (Schulterlang), mit Haarband zusammengehalten',
'3-1':'Lange Haare (Schulterlang), mit zwei Haarbändern links und rechts',
'6-4':'Lange Haare (Schulterlang), Pony',
'9-7':'Lange Haare (Schulterlang), Zöpfe mit Haarnadeln am Kopf befestigt',
'10':'Lange Haare (Schulterlang), Haarreif',
'2-1':'Lange Haare (Schulterlang), Haarreif',
'5-3':'Lange Haare (Schulterlang), Haarspange',
'8-6':'Lange Haare (Schulterlang), Haarbänder',
'10-9':'Lange Haare (Schulterlang), Mittelscheitel',
'1':'Lange Haare (Schulterlang), Mittelscheitel',
'4-2':'Lange Haare gewellte (Schulterlang), ins Gesicht fallend',
'7-5':'Lange Haare gewellte (Schulterlang), gescheitelt',
'10-8':'Lange Haare gewellte Schulterlang), nach hinten gekämmt',
'3-1':'Lange Haare gewellte (Schulterlang), mit Haarband zusammengehalten',
'6-4':'Lange Haare gewellte (Schulterlang), mit zwei Haarbändern links und rechts',
'9-7':'Lange Haare gewellte (Schulterlang), Pony',
'10':'Lange Haare gewellte (Schulterlang), Zöpfe mit Haarnadeln am Kopf befestigt',
'2-1':'Lange Haare gewellte (Schulterlang), Zöpfe mit Haarnadeln am Kopf befestigt',
'5-3':'Lange Haare gewellte (Schulterlang), Haarreif',
'8-6':'Lange Haare gewellte (Schulterlang), Haarspange',
'10-9':'Lange Haare gewellte (Schulterlang), Haarbänder',
'1':'Lange Haare gewellte (Schulterlang), Haarbänder',
'4-2':'Lange Haare gewellte (Schulterlang), Mittelscheitel',
'7-5':'Lange Haare (bis Rücken), ins Gesicht fallend',
'10-8':'Lange Haare (bis Rücken), gescheitelt',
'3-1':'Lange Haare (bis Rücken), nach hinten gekämmt',
'6-4':'Lange Haare (bis Rücken), mit Haarband zusammengehalten',
'9-7':'Lange Haare (bis Rücken), mit zwei Haarbändern links und rechts',
'10':'Lange Haare (bis Rücken), Pony',
'2-1':'Lange Haare (bis Rücken), Pony',
'5-3':'Lange Haare (bis Rücken), Zöpfe mit Haarnadeln am Kopf befestigt',
'8-6':'Lange Haare (bis Rücken), Mittelscheitel',
'10-9':'Lange Haare (bis Rücken), Haarreif',
'1':'Lange Haare (bis Rücken), Haarreif',
'4-2':'Lange Haare (bis Rücken), Haarspange',
'7-5':'Lange Haare (bis Rücken), Haarspangen',
'10-8':'Lange Haare gewellte (bis Rücken), ins Gesicht fallend',
'3-1':'Lange Haare gewellte (bis Rücken), gescheitelt',
'6-4':'Lange Haare gewellte (bis Rücken), nach hinten gekämmt',
'9-7':'Lange Haare gewellte (bis Rücken), mit Haarband zusammengehalten',
'10':'Lange Haare gewellte (bis Rücken), mit zwei Haarbändern links und rechts',
'2-1':'Lange Haare gewellte (bis Rücken), mit zwei Haarbändern links und rechts',
'5-3':'Lange Haare gewellte (bis Rücken), Pony',
'8-6':'Lange Haare gewellte (bis Rücken), Zöpfe mit Haarnadeln am Kopf befestigt',
'10-9':'Lange Haare gewellte (bis Rücken), Haarreif',
'1':'Lange Haare gewellte (bis Rücken), Haarreif',
'4-2':'Lange Haare gewellte (bis Rücken), Haarspange',
'7-5':'Lange Haare gewellte (bis Rücken), Haarspangen',
'8':'Lange Haare gewellte (Schulterlang), unter Kopftuch',
'10-9':'Lange Haare, Dutt am Hinterkopf',
'2-1':'Lange Haare, Dutt rausfallende Strähnen',
'4-3':'Lange Haare, Dutt oben',
'6-5':'Lange Haare, Prinzessin-Leia- Gedächtnisfrisur',
'8-7':'Lange Haare, Zopf kunstvoll um den Kopf gewickelt',
'9':'Lange Haare, kunstvoll aufgetürmt',
'10':'Lange Haare, mit vielen Bändchen zusammengehalten',
'1':'Lange Haare (Schulterlang), viele Zöpfe',
'2':'Lange Haare, mit vielen Bändchen zusammengehalten',
'3':'Mittellange Haare mit mittels Brennschere erzeugten Locken',
'5-4':'Kurze Haare mit Fett nach hinten gestylt',
'7-6':'Mittellange Haare mit Fett nach hinten gestylt',
'9-8':'Lange Haare mit Fett nach hinten gestylt',
'10':'Lange Haare mit Fett nach hinten gestylt',
'3-1':'Lange gewellte Haare (Schulterlang), Haarband',
'6-4':'Lange Haare (Schulterlang), Stirnband',
'8-7':'Lange gewellte Haare (Schulterlang), Stirnband',
'9':'Lange gewellte Haare (Schulterlang), Haarband',
'10':'Lange Haare (Schulterlang), hinters Ohr geklemmt',
'2-1':'Lange Haare (Schulterlang), hinters Ohr geklemmt',
'4-3':'Lange gewellte Haare (Schulterlang), hinters Ohr geklemmt',
'7-5':'Lange Haare (bis Rücken), hinters Ohr geklemmt',
'8':'Sehr lange Haare (bis Hüfte)',
'9':'Sehr lange Haare (bis Hüfte) Pony',
'10':'Sehr lange Haare (bis Hüfte) gewellt'}
Haartracht_m_temp = {'3-1':'Glatze (durch Haarausfall)',
'7-4':'Glatze (rasiert)',
'9-8':'Glatze mit ein paar Haarfuseln, welche wild nach oben stehen',
'13-10':'Halbglatze kurz',
'19-14':'Halbglatze, mittellang',
'20':'Halbglatze, lange Haare',
'1':'Halbglatze, lange Haare',
'4-2':'Halbglatze, Zopf',
'8-5':'Halbglatze mit über den Schädel gekämmten Haaren',
'10-9':'Stirnglatz Rest kurz',
'12-11':'Stirnglatz Rest mittellang',
'14-13':'Stirnglatz Rest lang',
'18-15':'Geheimratsecken, Rest kurz',
'20-19':'Geheimratsecken, Rest mittellang',
'2-1':'Geheimratsecken, Rest mittellang',
'5-3':'Geheimratsecken, Rest lang',
'7-6':'Geheimratsecken, Rest Zopf',
'9-8':'Geheimratsecken, Rest Haarband',
'10':'Starke Geheimratsecken, Rest Zopf',
'12-11':'Starke Geheimratsecken, Rest kurz',
'14-13':'Starke Geheimratsecken, Rest mittellang',
'15':'Starke Geheimratsecken, Rest lang',
'16':'Starke Geheimratsecken, Rest Haarband',
'19-17':'Kurz rasiert',
'20':'Kurz rasiert (unregelmäßig)',
'1':'Kurz rasiert, Zopf am Hinterkopf',
'2':'Kurz, schlecht geschnitten (Fransen)',
'6-3':'Sehr kurz',
'11-7':'Igel-Frisur',
'12':'Igel-Frisur, Zopf am Hinterkopf',
'15-13':'Seitenscheitel',
'17-16':'Seitenscheitel, schlecht geschnitten (Fransen)',
'20-18':'Mittelscheitel',
'3-1':'Mittelscheitel, schlecht geschnitten (Fransen)',
'6-4':'Seitenscheitel, an den Schläfen kurz rasiert',
'8-7':'Seitenscheitel, schlecht geschnitten (Fransen), an den Schläfen kurz rasiert',
'11-9':'Mittelscheitel, an den Schläfen kurz rasiert',
'13-12':'Mittelscheitel, schlecht geschnitten (Fransen), an den Schläfen kurz rasiert',
'15-14':'Seitenscheitel, schlecht geschnitten (Fransen)',
'18-16':'Seitenscheitel, an den Schläfen kurz rasiert',
'20-19':'Seitenscheitel, schlecht geschnitten (Fransen), an den Schläfen kurz rasiert',
'3-1':'Mittelscheitel, an den Schläfen kurz rasiert',
'9-4':'Prinz-Eisenherz-Frisur',
'17-10':'Topffrisur',
'20-18':'Lockenkopf, kurz',
'1':'Lockenkopf, kurz',
'5-2':'Lockenkopf, mittellang',
'7-6':'Mittellange Haare (bis Kinn), Pony',
'9-8':'Mittellange Haare (bis Kinn), nach hinten gekämmt',
'13-10':'Mittellange Haare (bis Kinn), Mittelscheitel',
'19-14':'Mittellange Haare (bis Kinn), gescheitelt',
'20':'Mittellange Haare (bis Kinn), ins Gesicht fallend',
'1':'Mittellange Haare (bis Kinn), ins Gesicht fallend',
'3-2':'Mittellange Haare (bis Kinn), Zöpfe an den Schläfen',
'4':'Mittellange gewellte Haare (bis Kinn), ins Gesicht fallend',
'7-5':'Mittellange gewellte Haare (bis Kinn), Mittelscheitel',
'9-8':'Mittellange gewellte Haare (bis Kinn), Pony',
'11-10':'Mittellange gewellte Haare (bis Kinn), Haarreif',
'12':'Lange Haare (Schulterlang), ins Gesicht fallend',
'14-13':'Lange Haare (Schulterlang), gescheitelt',
'15':'Lange Haare (Schulterlang), Zöpfe an den Schläfen',
'16':'Lange Haare (Schulterlang), nach hinten gekämmt',
'18-17':'Lange Haare (Schulterlang), mit Haarband zusammengehalten',
'19':'Lange Haare (Schulterlang), mit Haarspange zusammengehalten',
'20':'Lange Haare (Schulterlang), mit Haarreif',
'1':'Lange Haare (Schulterlang), mit Haarreif',
'2':'Lange Haare (Schulterlang), Stirnband',
'3':'Lange Haare (Schulterlang), Pony',
'4':'Lange gewellte Haare (Schulterlang), mit Haarband zusammengehalten',
'6-5':'Lange gewellte Haare (Schulterlang), gescheitelt',
'7':'Lange gewellte Haare (Schulterlang), Stirnband',
'8':'Lange Haare (Schulterlang), viele Zöpfe',
'13-9':'Vorne kurz, hinten lang (Vokuhila)',
'15-14':'Vorne kurz, hinten lang (Vokuhila) kombiniert mit Halbglatze',
'17-16':'Kurze Haare mit Fett nach hinten gestylt',
'19-18':'Mittellange Haare mit Fett nach hinten gestylt',
'20':'Lange Haare mit Fett nach hinten gestylt'}


def parseAuswahl(Liste):
    templist = []
    for key,value in Liste.items():
        if '-' in key:
            templist.append([value, int(key.split('-')[0])-int(key.split('-')[1])])
        else:
            templist.append([value, 1])
    return templist
  
Haartracht_m = parseAuswahl(Haartracht_m_temp)
Haartracht_w = parseAuswahl(Haartracht_w_temp)
  
        
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
          
        
        
alrik = NSC()
print(alrik.Geschlecht, alrik.Altersklasse, alrik.Alter, alrik.Körpergröße)
print(alrik.Haarfarbe, alrik.Augenfarbe,  alrik.Körperbau, alrik.Haartracht)
        
        
