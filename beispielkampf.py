# -*- coding: utf-8 -*- 
from kampf import Kampf
from archetypen import Aderion, Bederion	
from waffen import *
from ruestung import *
import pprint
from copy import deepcopy

# import cProfile
Testkampf = Kampf(1)
Testkampf.Runden = 1
Testkampf.verbose = 2

# Kaempft(Testkampf, Bederion, Aderion)

def RuestungsTest(Charakter, Ruestung1, Ruestung2):
    Teilnehmer1 = Charakter,
    Teilnehmer2 = deepcopy(Teilnehmer1),
    Teilnehmer1.Ruestung = Ruestung1,
    Teilnehmer2.Ruestung = Ruestung2,


Testkampf.Arena(Aderion, Bederion)

# Testkampf.Arena(Cederion, Sialdis)

'''
WaffenvergleichEH = {Waffe.name : 0 for Waffe in WaffenlisteEH}
for Waffe1 in WaffenlisteEH:
    for Waffe2 in WaffenlisteEH:
        Aderion.Waffe = Waffe1
        Bederion.Waffe = Waffe2
        Aderion.neustartCharakter()
        Bederion.neustartCharakter()
        Testkampf.Runden = 100
        Ergebnis = Testkampf.Arena(Aderion, Bederion)
        WaffenvergleichEH[Waffe1.name] += Ergebnis[0]
        WaffenvergleichEH[Waffe2.name] += Ergebnis[1]

WaffenvergleichZH = {Waffe.name : 0 for Waffe in WaffenlisteZH}
for Waffe1 in WaffenlisteZH:
    for Waffe2 in WaffenlisteZH:
        Aderion.Waffe = Waffe1
        Bederion.Waffe = Waffe2
        Aderion.neustartCharakter()
        Bederion.neustartCharakter()
        Testkampf.Runden = 100
        Ergebnis = Testkampf.Arena(Aderion, Bederion)
        WaffenvergleichZH[Waffe1.name] += Ergebnis[0]
        WaffenvergleichZH[Waffe2.name] += Ergebnis[1]

pprint.pprint(WaffenvergleichEH)
print (sum(WaffenvergleichEH.values()))
pprint.pprint(WaffenvergleichZH)
print (sum(WaffenvergleichZH.values()))
'''
