from kampf import Kampf
from math import pow
from operator import attrgetter
from waffen import *
from ruestung import *
from wuerfelklasse import *
from Zustand import *
from kampfposition import kampfposition
import logging

class Charakter(Kampf):        
                
    def __init__(
                self, 
                name = "Norbert Noname", 
                Waffenfertigkeit = 14, 
                Verteidigung = 19, 
                SchadensReduktion = 0,
                Lebenspunkte = 6, 
                StartINI = 5, 
                AngriffSchwelle = 20, 
                ParadeSicherheitsSchwelle = 1,
                ParadeSchwelle = 2, 
                ParadeRisikoSchwelle = 4,
                Fokus = 6,
                Waffe = Waffenlos,
                Ruestung = Nackt
                ):
        
        super(Charakter, self).__init__()
        self.name = name
        
        #Werte
        self.Waffenfertigkeit = Waffenfertigkeit
        self.Waffe = Waffe
        self.Ruestung = Ruestung
        self.Schaden = list(self.Waffe.Schaden)
        self.TP = str(str(self.Schaden[0])+'W'+str(self.Schaden[1])+'+'+str(self.Schaden[2]))
        self.Geschwindigkeit = self.Waffe.WGS + self.Ruestung.Tick
        self.Verteidigung_basis = Verteidigung
        self.SchadensReduktion_basis = SchadensReduktion
        self.Lebenspunkte = Lebenspunkte
        self.StartINI = StartINI
        self.Fokus_max = Fokus
        self.Zauberbuch = []
        self.Zustand = []
        self.Kampfposition = kampfposition('Stehend')
        
        #Verhalten
        self.AngriffSchwelle = AngriffSchwelle                 #Angriff mit Risikowurf bei > Schwelle Differenz Verteidigung - Waffenfertigkeit
        self.ParadeSchwelle = ParadeSchwelle                 #Aktive Parade bei < Schwelle benötigten Erfolgsgraden
        self.ParadeSicherheitsSchwelle = ParadeSicherheitsSchwelle      #Aktive Parade mit Risikowurf bei < Schwelle benötigten Erfolgsgraden
        self.ParadeRisikoSchwelle = ParadeRisikoSchwelle      #Aktive Parade mit Risikowurf bei < Schwelle benötigten Erfolgsgraden
        
        #Statusvariablen
        self.hp = 5 * self.Lebenspunkte
        self.Fokus = self.Fokus_max
        self.status = 0                                     #Gesundheitsstufe
        self.kfw = self.Waffenfertigkeit
        self.Verteidigung = self.Verteidigung_basis - self.Waffe.Merkmal.get('Unhandlich',0)*2 + self.Ruestung.VTD
        self.SchadensReduktion = self.SchadensReduktion_basis + self.Ruestung.SR
        self.Geschwindigkeit = self.Waffe.WGS + self.Ruestung.Tick
        self.siege = 0
        
    def __str__(self):
        return self.name
        
    def __repr__(self):
        return self.name
            
    def neustartCharakter(self):
        self.Tickleiste.initiere(self,self.StartINI - randrange(1,7))
        self.hp = 5 * self.Lebenspunkte
        self.Fokus = self.Fokus_max
        self.status = 0
        self.kfw = self.Waffenfertigkeit
        self.Verteidigung = self.Verteidigung_basis - self.Waffe.Merkmal.get('Unhandlich',0)*2 + self.Ruestung.VTD
        self.SchadensReduktion = self.SchadensReduktion_basis + self.Ruestung.SR
        self.Geschwindigkeit = self.Waffe.WGS + self.Ruestung.Tick
        self.Schaden = list(self.Waffe.Schaden)
        self.neustartZauber()
        self.Verwundet = None
    
    def bewegeTicks(self, ticks):
        self.Tickleiste.bewege(self, ticks)
        
    def aktivZustand(self,Zustand):
        self.Zustand.append[Zustand]
        
    def deaktivZustand(self,Zustand):
        self.Zustand.remove[Zustand]
        
    def nimmSchaden(self, Schaden, SR = 0):
        self.hp -= max(0, Schaden - min(0,self.SchadensReduktion - SR))
        if self.hp > self.Lebenspunkte*4:
            x = 0
        else: 
            x = 4 - ((self.hp) // self.Lebenspunkte)
        if self.Verwundet is not None: 
            x = max(4,x + self.Verwundet)
        self.status = int(pow(2,x)/2)
        self.kfw = self.Waffenfertigkeit - self.status
        return(max(0, Schaden - self.SchadensReduktion))
    
    def Patzer(self):
        patzer = PatzerWurf()
        if patzer < 4:
            self.Kampfposition.neu('Liegend, Nahkampf')
            self.bewegeTicks(10)
            Benommen(self)
            logging.debug("Benommen")
        elif patzer < 7:
            pass
            logging.debug("Beschädigte Waffe")
        elif patzer < 10:
            self.bewegeTicks(3)
            logging.debug("Desorientiertheit")
        elif patzer < 13:
            self.bewegeTicks(6)
            logging.debug("Straucheln")
        elif patzer < 16:
            self.Kampfposition.neu('Liegend, Nahkampf')
            logging.debug("Sturz")
        elif patzer < 19:
            self.bewegeTicks(3)
            logging.debug("Gelegenheitsangriff")
        elif patzer < 16:
            Blutend(self, Stufe=2)
            logging.debug("Schwere Verwundung")
        
    def verzehrFokus(self, Kosten):
        self.Fokus -= Kosten
        
    def waehleAktion(self, Verteidiger = None):
        if Verteidiger is None:
            Verteidiger = self.Gegner    
        Zauberwahl = self.waehleZauber(Verteidiger)
        if Zauberwahl == -1:
            Aktionresult = self.Attacke(Verteidiger)
        else:
            Aktionresult = self.Zauberbuch[Zauberwahl].zaubern(self,Verteidiger)
            logging.debug(str(self.name)+" zaubert "+self.Zauberbuch[Zauberwahl].name)
            if Aktionresult >= 0:
                logging.debug("Erfolgreich mit "+str(Aktionresult)+" Punkten")
            else:
                logging.debug("Fehlgeschlagen")
                
    def Attacke(self, Verteidiger):
        if (self.kfw + self.AngriffSchwelle) < Verteidiger.Verteidigung:
            risiko = 1
        else:    
            risiko = 0
        
        logging.info(str(self) + " greift an mit Wert "+str(self.kfw)+" und "+ str(self.TP)+" TP gegen Verteidigung "+str(Verteidiger.Verteidigung))
        
        self.WuerfelErgebnis = WuerfelProbe(self.kfw,Verteidiger.Verteidigung,risiko)
        
        logging.debug(str(self) + " würfelt und kommt auf "+str(Verteidiger.Verteidigung + self.WuerfelErgebnis[0])+"!")
        
        if self.WuerfelErgebnis[2]  or self.WuerfelErgebnis[0] <= -15:
            self.Patzer()   
            logging.debug(str(self) + " patzt!")     
            
        if self.WuerfelErgebnis[0] >= 0 and not self.WuerfelErgebnis[2]: #Angriff Erfolgreich
        
            if self.WuerfelErgebnis[0] < Verteidiger.ParadeSicherheitsSchwelle: #Aktive Parade Sicherheit
                
                Verteidiger.aktiveParade(self, -1)        
            
            elif self.WuerfelErgebnis[0] < Verteidiger.ParadeSchwelle: #Aktive Parade
            
                Verteidiger.aktiveParade(self)
                
            elif self.WuerfelErgebnis[0] < Verteidiger.ParadeRisikoSchwelle: #Aktive Parade Risiko
                
                Verteidiger.aktiveParade(self, 1)                                        
        
        if self.WuerfelErgebnis[3] or self.WuerfelErgebnis[0] >= 15: #ticks -1 bei krit
            self.bewegeTicks(self.Geschwindigkeit -1)
        else:
            self.bewegeTicks(self.Geschwindigkeit)
            
        
       
                
        if self.WuerfelErgebnis[0] >= 0 and not self.WuerfelErgebnis[2]:
            Schaden = Verteidiger.nimmSchaden(wuerfelSchaden(self.Schaden, self.Waffe.Merkmal.get('Scharf',1))
                                           + (self.Waffe.Merkmal.get('Wuchtig',0)+1)*(int(self.WuerfelErgebnis[0]/3) + (3 if self.WuerfelErgebnis[3] else 0)), self.Waffe.Merkmal.get('Durchdringung',0))
            EG =  int(self.WuerfelErgebnis[0]/3) + (3 if self.WuerfelErgebnis[3] else 0)
            logging.info(str(self)+" verursacht "+str(Schaden)+" Punkte Schaden mit "+str(EG)+" Erfolgsgraden")                           
            return(Schaden, EG)
        elif self.WuerfelErgebnis[2]:
            return (0, min(int(self.WuerfelErgebnis[0]/3) - 3 , -1))
        else:            
            return (0, int(self.WuerfelErgebnis[0]/3))
            logging.info(str(self) + ' verfehlt!')
        
        
    def aktiveParade(self, Angreifer, risiko = 0):
        self.WuerfelErgebnis = WuerfelProbe(self.kfw,15,risiko)
        if self.WuerfelErgebnis[2]:
            self.Patzer()
            logging.debug(str(self) + " patzt!")    
        
        if self.WuerfelErgebnis[3] or self.WuerfelErgebnis[1] >= 5: #ticks -1 bei krit
            self.bewegeTicks(2)
        else:
            self.bewegeTicks(3)
            
        AAEG = max(0,self.WuerfelErgebnis[1] # EG
                                        + int(self.WuerfelErgebnis[0] > 0  #gelungen
                                        + (3 if self.WuerfelErgebnis[3] else 0) #krit
                                        + self.Waffe.Merkmal.get('Defensiv',0))) #defensiv
            
        logging.info('Aktive Parade von '+ str(self) +': Würfel: '+str(15+ self.WuerfelErgebnis[0])+' und '+str(AAEG)+' EG')
            
        Angreifer.WuerfelErgebnis[0] -= AAEG
    
    
    def lernZauber(self, Zauber):
        if not Zauber in self.Zauberbuch:
            self.Zauberbuch.append(Zauber)
        
    def waehleZauber(self,  Verteidiger = None):
        if Verteidiger is None:
            Verteidiger = self.Gegner  
        try:
            return self.Zauberbuch.index(max((Spruch for Spruch in self.Zauberbuch if Spruch.Kosten <= self.Fokus and (Spruch.aktiv == 0 or Spruch.stapelbar == 1)),key = attrgetter('prio')))
        except ValueError:
            return -1    
            
    def neustartZauber(self):
        for Spruch in self.Zauberbuch:
            Spruch.aktiv = 0