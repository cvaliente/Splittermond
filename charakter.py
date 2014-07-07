from kampf import Kampf
from math import pow
from operator import attrgetter
from waffen import *
from ruestung import *
from wuerfelklasse import *

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
        self.Geschwindigkeit = self.Waffe.WGS + self.Ruestung.Tick
        self.Verteidigung_basis = Verteidigung
        self.SchadensReduktion_basis = SchadensReduktion
        self.Lebenspunkte = Lebenspunkte
        self.StartINI = StartINI
        self.Fokus_max = Fokus
        self.Zauberbuch = []
        
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
        self.TickPosition = self.StartINI - randint(1,6)
        self.siege = 0
    
    def bewegeZuPosition(self, neuePosition):
        while neuePosition in super().Positions.values():
            neuePosition += 0.01        
        super().Positions[self] = neuePosition
        return neuePosition
        
    def neustartCharakter(self):
        self.TickPosition = self.bewegeZuPosition(self.StartINI - randint(1,6))
        self.hp = 5 * self.Lebenspunkte
        self.Fokus = self.Fokus_max
        self.status = 0
        self.kfw = self.Waffenfertigkeit
        self.Verteidigung = self.Verteidigung_basis - self.Waffe.Merkmal.get('Unhandlich',0)*2 + self.Ruestung.VTD
        self.SchadensReduktion = self.SchadensReduktion_basis + self.Ruestung.SR
        self.Geschwindigkeit = self.Waffe.WGS + self.Ruestung.Tick
        self.Schaden = list(self.Waffe.Schaden)
        self.neustartZauber()
    
    def bewegeTicks(self, ticks):
        self.TickPosition = self.bewegeZuPosition( int(self.TickPosition) + ticks)
        
    def nimmSchaden(self, Schaden, SR = 0):
        self.hp -= max(0, Schaden - min(0,self.SchadensReduktion - SR))
        self.status = int(pow(2,4 - ((self.hp - 1) // self.Lebenspunkte))/2)
        self.kfw = self.Waffenfertigkeit - self.status
        return(max(0, Schaden - self.SchadensReduktion))
        
    def verzehrFokus(self, Kosten):
        self.Fokus -= Kosten
        
    def waehleAktion(self, Verteidiger, verbose = 0):    
        Zauberwahl = self.waehleZauber(Verteidiger)
        if Zauberwahl == -1:
            Aktionresult = self.Attacke(Verteidiger)
            if verbose == 2:
                print(str(self.name)+" greift an mit Wert "+str(self.kfw)+" und "+str(self.Schaden)+" TP gegen Verteidigung "+str(Verteidiger.Verteidigung))
                print(str(self.name)+" verursacht "+str(Aktionresult[0])+" Punkte Schaden mit "+str(Aktionresult[1])+" Erfolgsgraden")
        else:
            Aktionresult = self.Zauberbuch[Zauberwahl].zaubern(self,Verteidiger)
            if verbose == 2:
                print(str(self.name)+" zaubert "+self.Zauberbuch[Zauberwahl].name)
                if Aktionresult >= 0:
                    print("Erfolgreich mit "+str(Aktionresult)+" Punkten")
                else:
                    print("Fehlgeschlagen")
                
    def Attacke(self, Verteidiger):
        if (self.kfw + self.AngriffSchwelle) < Verteidiger.Verteidigung:
            risiko = 1
        else:    
            risiko = 0
        self.WuerfelErgebnis = WuerfelProbe(self.kfw,Verteidiger.Verteidigung,risiko)
        self.bewegeTicks(self.Geschwindigkeit + self.WuerfelErgebnis[2] * 5)
        
        if self.WuerfelErgebnis[0] >= 0: #Angriff Erfolgreich
        
            if self.WuerfelErgebnis[0] < Verteidiger.ParadeSicherheitsSchwelle: #Aktive Parade Sicherheit
                
                Verteidiger.aktiveParade(self, -1)        
            
            elif self.WuerfelErgebnis[0] < Verteidiger.ParadeSchwelle: #Aktive Parade
            
                Verteidiger.aktiveParade(self)
                
            elif self.WuerfelErgebnis[0] < Verteidiger.ParadeRisikoSchwelle: #Aktive Parade Risiko
                
                Verteidiger.aktiveParade(self, 1)                                        
                    
        if self.WuerfelErgebnis[0] >= 0:
            return(Verteidiger.nimmSchaden(wuerfelSchaden(self.Schaden, self.Waffe.Merkmal.get('Scharf',1))+ (self.Waffe.Merkmal.get('Wuchtig',0)+1)*self.WuerfelErgebnis[1], self.Waffe.Merkmal.get('Durchdringung',0)), self.WuerfelErgebnis[1])
        else:
            return (0, self.WuerfelErgebnis[1])

    def aktiveParade(self, Angreifer, risiko = 0):
        self.WuerfelErgebnis = WuerfelProbe(self.kfw,15,risiko)
        self.bewegeTicks(3 + self.WuerfelErgebnis[2] * 5)
        Angreifer.WuerfelErgebnis[0] -= max(0,self.WuerfelErgebnis[1] + int(self.WuerfelErgebnis[0]>0)*(1+self.Waffe.Merkmal.get('Defensiv',0)))
        Angreifer.WuerfelErgebnis[1] = int(Angreifer.WuerfelErgebnis[0]/3)
    
    
    def lernZauber(self, Zauber):
        if not Zauber in self.Zauberbuch:
            self.Zauberbuch.append(Zauber)
        
    def waehleZauber(self,  Verteidiger):
        try:
            return self.Zauberbuch.index(max((Spruch for Spruch in self.Zauberbuch if Spruch.Kosten <= self.Fokus and (Spruch.aktiv == 0 or Spruch.stapelbar == 1) and Spruch.Ticks < (Verteidiger.TickPosition - self.TickPosition)),key = attrgetter('prio')))
        except ValueError:
            return -1    
            
    def neustartZauber(self):
        for Spruch in self.Zauberbuch:
            Spruch.aktiv = 0