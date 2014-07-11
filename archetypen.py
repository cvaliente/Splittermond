from charakter import Charakter
from zauberbuch import magischerSchlag, Blitzschlag, magischeRuestung, flammendeWaffe    
from waffen import *
from ruestung import *

Aderion = Charakter(
                    name="Aderion von Langschwert",
                    Waffenfertigkeit=13,
                    Verteidigung=20,
                    SchadensReduktion=0,
                    Lebenspunkte=7,
                    StartINI=9,
                    AngriffSchwelle=40,
                    ParadeSicherheitsSchwelle=0,
                    ParadeSchwelle=0,
                    ParadeRisikoSchwelle=0,
                    Waffe=Langschwert,
                    Ruestung=Hybrid
                    )    

Bederion = Charakter(
                    name="Bederion von Breitschwert",
                    Waffenfertigkeit=13,
                    Verteidigung=20,
                    SchadensReduktion=0,
                    Lebenspunkte=7,
                    StartINI=9,
                    AngriffSchwelle=40,
                    ParadeSicherheitsSchwelle=0,
                    ParadeSchwelle=0,
                    ParadeRisikoSchwelle=0,
                    Waffe=Breitschwert,
                    Ruestung=Hybrid
                    )        
                    
Cederion = Charakter(
                    name="Cederion von Falkenberg",
                    Waffenfertigkeit=13,
                    Verteidigung=22,
                    SchadensReduktion=2,
                    Lebenspunkte=8,
                    StartINI=9,
                    AngriffSchwelle=10,
                    ParadeSchwelle=3,
                    ParadeRisikoSchwelle=5
                    )                    
                    
Wulfhard = Charakter(
                    name="Wulfhard von Zwifels",
                    Waffenfertigkeit=13,
                    Verteidigung=24,
                    SchadensReduktion=2,
                    Lebenspunkte=9,
                    StartINI=8,
                    AngriffSchwelle=10,
                    ParadeSchwelle=3,
                    ParadeRisikoSchwelle=5
                    )                        
                    
TiaiKettensichel = Charakter(
                    name="Tiai Schimmersee mit Kettensichel",
                    Waffenfertigkeit=13,
                    Verteidigung=22,
                    SchadensReduktion=0,
                    Lebenspunkte=7,
                    StartINI=5,
                    AngriffSchwelle=10,
                    ParadeSchwelle=3,
                    ParadeRisikoSchwelle=5,
                    Fokus=20
                    )    
                    
TiaiMaira = Charakter(
                    name="Tiai Schimmersee mit Maira",
                    Waffenfertigkeit=11,
                    Verteidigung=22,
                    SchadensReduktion=0,
                    Lebenspunkte=7,
                    StartINI=5,
                    AngriffSchwelle=10,
                    ParadeSchwelle=3,
                    ParadeRisikoSchwelle=5,
                    Fokus=20
                    )
                    
Sialdis = Charakter(
                    name="Sialdis aus Sunjas Schar",
                    Waffenfertigkeit=12,
                    Verteidigung=20,
                    SchadensReduktion=1,
                    Lebenspunkte=8,
                    StartINI=6,
                    AngriffSchwelle=10,
                    ParadeSchwelle=3,
                    ParadeRisikoSchwelle=5,
                    Fokus=8
                    )
                    
SialdisLeder = Charakter(
                    name="Sialdis aus Sunjas Schar in leichtem Leder",
                    Waffenfertigkeit=12,
                    Verteidigung=22,
                    SchadensReduktion=0,
                    Lebenspunkte=8,
                    StartINI=6,
                    AngriffSchwelle=10,
                    ParadeSchwelle=3,
                    ParadeRisikoSchwelle=5,
                    Fokus=8
                    )
                    
SialdisZauber = Charakter(
                    name="Sialdis aus Sunjas Schar",
                    Waffenfertigkeit=12,
                    Verteidigung=20,
                    SchadensReduktion=1,
                    Lebenspunkte=8,
                    StartINI=9,
                    AngriffSchwelle=10,
                    ParadeSchwelle=3,
                    ParadeRisikoSchwelle=5
                    )                    
                    
SialdisBuffed = Charakter(
                    name=u"Sialdis aus Sunjas Schar mit Flammender Waffe und magischer Rüstung",
                    Waffenfertigkeit=12,
                    Verteidigung=23,
                    SchadensReduktion=1,
                    Lebenspunkte=8,
                    StartINI=6,
                    AngriffSchwelle=10,
                    ParadeSchwelle=3,
                    ParadeRisikoSchwelle=5
                    )
                    
Keira = Charakter(
                    name="Keira Alvios",
                    Waffenfertigkeit=12,
                    Verteidigung=19,
                    SchadensReduktion=0,
                    Lebenspunkte=7,
                    StartINI=3,
                    AngriffSchwelle=10,
                    ParadeSchwelle=3,
                    ParadeRisikoSchwelle=5
                    )
                                        
Vedrana = Charakter(
                    name="Vedrana Sertin",
                    Waffenfertigkeit=8,
                    Verteidigung=21,
                    SchadensReduktion=0,
                    Lebenspunkte=7,
                    StartINI=4,
                    AngriffSchwelle=10,
                    ParadeSchwelle=3,
                    ParadeRisikoSchwelle=5
                    )
                    


TiaiKettensichel.lernZauber(magischerSchlag(1, 7))
TiaiKettensichel.lernZauber(Blitzschlag(3, 11))
Sialdis.lernZauber(magischeRuestung(5, 8))
Sialdis.lernZauber(flammendeWaffe(3, 7))
