from collections import namedtuple

Waffe = namedtuple('Waffe', 'name Schaden WGS Fertigkeit Last Haerte Merkmal')

		
Dornenhandschuh =Waffe('Dornenhandschuh', [1, 6, 0], 5, 'Klingenwaffen', 2, 7, {'Entwaffnend' : 1, 'Defensiv': 2, 'Parierwaffe': 1})
Katar = Waffe('Katar', [1, 6, +1], 6, 'Klingenwaffen', 2, 7, {'Scharf':2})
Liandia = Waffe('Liandia', [1, 6, +1], 6, 'Klingenwaffen', 2, 7, {'Entwaffnend' : 1, 'Defensiv': 1, 'Parierwaffe': 0})
Schlagring = Waffe('Schlagring', [1, 6, 0], 5, 'Klingenwaffen', 2, 7, {'Scharf':2})
Waffenlos = Waffe('Waffenlos', [1, 6, 0], 5, 'Klingenwaffen', 2, 7, {'Entwaffnend' : 1, 'Stumpf': 1, 'Umklammern': 1})

Anderthalbhander        = Waffe('Anderthalbhander', [2, 6, 0], 9, 'Klingenwaffen', 2, 7, {'Scharf': 3, 'Vielseitig':1})
AnderthalbhanderZH        = Waffe('Anderthalbhander ZH', [2, 6, 3], 9, 'Klingenwaffen', 2, 7, {'Scharf': 3, 'Zweihandig':1})
Breitschwert            = Waffe('Breitschwert', [1, 6, +4], 9, 'Klingenwaffen', 2, 7, {'Wuchtig':1})
Dolch                   = Waffe('Dolch', [1, 6, +1], 6, 'Klingenwaffen', 2, 7, {'Wurftauglich':1})
Falchion                = Waffe('Falchion', [1, 6, +5], 9, 'Klingenwaffen', 2, 7, {})
FulnischesHalbschwert   = Waffe('Fulnisches Halbschwert', [1, 6, +4], 8, 'Klingenwaffen', 2, 7, {'Teilbar':1})
Khopesh                 = Waffe('Khopesh', [1, 10, +1], 7, 'Klingenwaffen', 2, 7, {'Scharf':2})
Krummdolch              = Waffe('Krummdolch', [1, 6, +2], 7, 'Klingenwaffen', 2, 7, {})
Kurzschwert             = Waffe('Kurzschwert', [1, 6, +2], 7, 'Klingenwaffen', 2, 7, {})
Langschwert             = Waffe('Langschwert', [1, 6, +4], 8, 'Klingenwaffen', 2, 7, {'Scharf':2})
Maira                   = Waffe('Maira', [1, 6, +1], 6, 'Klingenwaffen', 2, 7, {'Scharf':2})
Pfauenfeder             = Waffe('Pfauenfeder', [2, 6, +4], 10, 'Klingenwaffen', 2, 7, {'Scharf':2, 'Wuchtig':1, 'Zweihandig':1})
Reitersabel             = Waffe('Reitersabel', [1, 6, +3], 8, 'Klingenwaffen', 2, 7, {'Reiterwaffe':2})
Scheibendolch           = Waffe('Scheibendolch', [1, 6, 0], 6, 'Klingenwaffen', 2, 7, {'Durchdringung':2})
Skavona                 = Waffe('Skavona', [1, 6, +2], 7, 'Klingenwaffen', 2, 7, {'Durchdringung':2})
Sabel                   = Waffe('Sabel', [1, 6, +4], 8, 'Klingenwaffen', 2, 7, {'Scharf':2})
WurfdolchNK             = Waffe('Wurfdolch (NK)', [1, 6, -1], 8, 'Klingenwaffen', 2, 7, {'Improvisiert':1,'Wurftauglich':1})
Zweihander              = Waffe('Zweihander', [2, 6, +4], 12, 'Klingenwaffen', 2, 7, {'Durchdringung':2,'Lange Waffe':1,'Scharf':3,'Wuchtig':1,'Zweihandig':1})
Doppelaxt = Waffe('Doppelaxt', [3, 6, +3], 13, 'Klingenwaffen', 2, 7, {'Durchdringung':2,'Unhandlich':1,'Wuchtig':1,'Zweihandig':1})
Keule = Waffe('Keule', [1, 6, +2], 7, 'Klingenwaffen', 2, 7, {'Primitiv':1})
Kriegsbeil = Waffe('Kriegsbeil', [1, 10, +3], 9, 'Klingenwaffen', 2, 7, {})
Kriegshammer = Waffe('Kriegshammer', [2, 10, +4], 12, 'Klingenwaffen', 2, 7, {'Unhandlich':1,'Wuchtig':1,'Zweihandig':1})
Schlagstock = Waffe('Schlagstock', [1, 6, +2], 6, 'Klingenwaffen', 2, 7, {'Stumpf':1})
Spitzhacke = Waffe('Spitzhacke', [3, 6, 0], 14, 'Klingenwaffen', 2, 7, {'Improvisiert':1,'Primitiv':1,'Wuchtig':1,'Zweihandig':1})
Streitaxt = Waffe('Streitaxt', [2, 10, +1], 11, 'Klingenwaffen', 2, 7, {'Scharf':2, 'Wuchtig':1, 'Zweihandig':1})
Streithammer = Waffe('Streithammer', [2, 6, +3], 11, 'Klingenwaffen', 2, 7, {'Scharf': 2, 'Vielseitig':1})
StreithammerZH = Waffe('Streithammer ZH', [2, 6, +6], 11, 'Klingenwaffen', 2, 7, {'Scharf': 2, 'Zweihandig':1})
Streitkolben = Waffe('Streitkolben', [1, 6, +5], 9, 'Klingenwaffen', 2, 7, {})
Stuhlbein = Waffe('Stuhlbein, Flasche, Nudelholz', [1, 6, -1], 9, 'Klingenwaffen', 2, 7, {'Improvisiert':1,'Primitiv':1})
WurfbeilNK = Waffe('Wurfbeil (NK)', [1, 6, +1], 10, 'Klingenwaffen', 2, 7, {'Improvisiert':1,'Wurftauglich':1})
WurfhammerNK = Waffe('Wurfhammer (NK)', [1, 6, +2], 11, 'Klingenwaffen', 2, 7, {'Improvisiert':1,'Wurftauglich':1})

FulnischesDoppelschwert = Waffe('Fulnisches Doppelschwert', [2, 10, +1], 11, 'Klingenwaffen', 2, 7, {'Doppelwaffe':1,'Teilbar':1,'Scharf':3,'Zweihandig':1})
Glefe = Waffe('Glefe', [2, 10, +1], 11, 'Klingenwaffen', 2, 7, {'Lange Waffe':1,'Wuchtig':1,'Zweihandig':1})
Hellebarde = Waffe('Hellebarde', [3, 6, +3], 12, 'Klingenwaffen', 2, 7, {'Lange Waffe':1,'Wuchtig':1,'Zweihandig':1})
Kampfstab = Waffe('Kampfstab', [1, 10, +2], 9, 'Klingenwaffen', 2, 7, {'Doppelwaffe':1,'Lange Waffe':1,'Defensiv':2,'Zweihandig':1})
Klingenstab = Waffe('Klingenstab', [2, 6, 0], 9, 'Klingenwaffen', 2, 7, {'Durchdringung':1,'Lange Waffe':1,'Vielseitig':1})
Lanze = Waffe('Lanze', [2, 10, +1], 15, 'Klingenwaffen', 2, 7, {'Reiterwaffe':6,'Lange Waffe':1,'Scharf':3,'Wuchtig':1,'Zweihandig':1})
Speer = Waffe('Speer', [1, 10, +5], 12, 'Klingenwaffen', 2, 7, {'Scharf':3,'Lange Waffe':1,'Vielseitig':1})
Sturmsense = Waffe('Sturmsense', [2, 10, +4], 13, 'Klingenwaffen', 2, 7, {'Lange Waffe':1,'Wuchtig':1,'Zweihandig':1})
ValkyrjaSpeer = Waffe('Valkyrja-Speer', [1, 10, +2], 8, 'Klingenwaffen', 2, 7, {'Wurftauglich':1})
Vangarasstab = Waffe('Vangarasstab', [3, 6, +1], 13, 'Klingenwaffen', 2, 7, {'Wuchtig':1,'Lange Waffe':1,'Vielseitig':1})
WurfspeerNK = Waffe('Wurfspeer (NK)', [1, 6, +2], 11, 'Klingenwaffen', 2, 7, {'Improvisiert':1,'Wurftauglich':1})
Zackenspiess = Waffe('Zackenspiess', [1, 6, +5], 11, 'Klingenwaffen', 2, 7, {'Durchdringung':2,'Lange Waffe':1,'Vielseitig':1,'Entwaffnend':1})

VangarasstabZH = Waffe('VangarasstabZH', [3, 6, +4], 13, 'Klingenwaffen', 2, 7, {'Wuchtig':1,'Lange Waffe':1,'Vielseitig':1})
ZackenspiessZH = Waffe('Zackenspiess', [1, 6, +8], 11, 'Klingenwaffen', 2, 7, {'Durchdringung':2,'Lange Waffe':1,'Vielseitig':1,'Entwaffnend':1})
SpeerZH = Waffe('Speer', [1, 10, +8], 12, 'Klingenwaffen', 2, 7, {'Scharf':3,'Lange Waffe':1,'Vielseitig':1})
KlingenstabZH = Waffe('Klingenstab', [2, 6, 3], 9, 'Klingenwaffen', 2, 7, {'Durchdringung':1,'Lange Waffe':1,'Vielseitig':1})

Kettensichel = Waffe('Kettensichel', [1, 10, 0], 8, 'Klingenwaffen', 2, 7, {'Entwaffnend' : 2, 'Umklammern': 1, 'Lange Waffe': 1, 'Vielseitig': 1})
KettensichelZH = Waffe('Kettensichel', [1, 10, 3], 8, 'Klingenwaffen', 2, 7, {'Entwaffnend' : 2, 'Umklammern': 1, 'Lange Waffe': 1, 'Vielseitig': 1})
Kriegsflegel = Waffe('Kriegsflegel', [2, 10, +4], 14, 'Klingenwaffen', 2, 7, {'Durchdringung':2, 'Wuchtig':1, 'Zweihandig':1})
Morgenstern = Waffe('Morgenstern', [1, 10, +5], 10, 'Klingenwaffen', 2, 7, {'Unhandlich': 1})
Peitsche = Waffe('Peitsche', [1, 10, -2], 15, 'Klingenwaffen', 2, 7, {'Entwaffnend' : 3, 'Improvisiert': 1, 'Umklammern': 1, 'Lange Waffe': 1, 'Unhandlich': 1})


WaffenlisteEH = [Anderthalbhander,Kettensichel,Morgenstern,Peitsche,
Schlagring,
Katar,
Liandia,
Dornenhandschuh,
Breitschwert,
Dolch,
Falchion,
FulnischesHalbschwert,
Khopesh,
Krummdolch,
Kurzschwert,
Langschwert,
Maira,
Reitersabel,
Scheibendolch,
Skavona,
Sabel,
WurfdolchNK,
Keule,
Kriegsbeil,
Schlagstock,
Streithammer,
Streitkolben,
Stuhlbein, 
WurfbeilNK,
WurfhammerNK,
Klingenstab,
Speer,
ValkyrjaSpeer,
Vangarasstab,
WurfspeerNK,
Zackenspiess
]

WaffenlisteZH = [AnderthalbhanderZH,
Pfauenfeder,KettensichelZH,Kriegsflegel,
Zweihander,
Kriegshammer,
Doppelaxt,
Spitzhacke,
Streitaxt,
StreithammerZH,
FulnischesDoppelschwert,
Glefe,
Hellebarde,
Kampfstab,
Lanze,
Sturmsense,VangarasstabZH,ZackenspiessZH,SpeerZH,KlingenstabZH
]
