# -*- coding: utf-8 -*- 
from kampf import Kampf
from archetypen import Aderion    
from waffen import *
from ruestung import *
from copy import deepcopy

Teilnehmer1 = Aderion
Teilnehmer1.Ruestung = Hybrid

VangarasstabZHmax = Waffe('VangarasstabZHmax', [3, 6, +6], 12, 'Klingenwaffen', 2, 7, {'Wuchtig':1,'Lange Waffe':1,'Vielseitig':1})


def erstelleTestSubjekt(Charakter, Ruestung = None, Waffe = None):
    if Waffe is not None:
        Charakter.Waffe = Waffe
        Charakter.name += " " + Waffe.name
    if Ruestung is not None:
        Charakter.Ruestung = Ruestung    
        Charakter.name += " " + Ruestung.name
    Charakter.neustartKampf();
    return Charakter

def RuestungsTest(Charakter, Ruestung1 = None, Waffe1 = None, Ruestung2 = None, Waffe2 = None):
    Teilnehmer1 = erstelleTestSubjekt(deepcopy(Charakter), Ruestung = Ruestung1, Waffe = Waffe1)
    Teilnehmer2 = erstelleTestSubjekt(deepcopy(Charakter), Ruestung = Ruestung2, Waffe = Waffe2)
    Testkampf = Kampf(0)
    Testkampf.Runden = 10000
    Testkampf.Arena(Teilnehmer1, Teilnehmer2)
    
RuestungsTest(Aderion, Hybrid, Vangarasstab, Ausweichen, VangarasstabZHmax)