from wuerfelklasse import *

class Zustand():
    def __init__(self, Gegner, Stufe = 1, instant = False, forever = False, Dauer = 60, Geschwindigkeit = 10):
        self.Gegner = Gegner
        self.Stufe = Stufe
        if instant == False:
            self.Tickleiste = Gegner.Tickleiste
            self.Geschwindigkeit = Geschwindigkeit
            self.Dauer = Dauer
            self.Ende = self.Tickleiste.Position + self.Dauer
            self.Tickleiste.initiere(self,self.Tickleiste.Position + self.Geschwindigkeit)
        elif forever == False:
            self.Effekt()
            self.Tickleiste = Gegner.Tickleiste
            self.Dauer = Dauer
            self.Ende = self.Tickleiste.Position + self.Dauer          
            self.Tickleiste.initiere(self,self.Ende + 1)
        else:
            self.Effekt()
        
    
    def bewegeTicks(self):
        self.Tickleiste.bewege(self, 10)
        
    def Effekt(self):
        pass
    
    def waehleAktion(self):
        if self.Tickleiste.bestimmePosition(self) <= self.Ende:
            self.Effekt()
            self.bewegeTicks()
        if self.Tickleiste.bestimmePosition(self) > self.Ende:
            self.loesche(self)
    
    def loesche(self):
        self.Tickleiste.loesche(self)
        self.Gegner.deaktiv(self)
    
class Blutend(Zustand):
    def __init__(self, Gegner, Stufe = 1):        
        super().__init__(Gegner, Geschwindigkeit = 15, Dauer = 60)
        
    def Effekt(self):
        self.Gegner.nimmSchaden(self.Stufe * 3)
        

class Brennend(Zustand):
    def __init__(self, Gegner, Stufe = 1):        
        super().__init__(Gegner, Geschwindigkeit = 15, Dauer = 90)
        
    def Effekt(self):
        self.Gegner.nimmSchaden(sum(randrange(1,7) for _ in range(0,self.Stufe)))
        
class Verwundet(Zustand):
    def __init__(self, Gegner, Stufe = 1):        
        super().__init__(Gegner, instant = True, forever = True)
        
    def Effekt(self):
        self.Gegner.Verwundet += self.Stufe
        
class Benommen(Zustand):
    def __init__(self, Gegner, Stufe = 1):        
        super().__init__(Gegner, instant = True, Dauer = 60)
    
    def Effekt(self):
        self.Gegner.Geschwindigkeit += self.Stufe
    
    def loesche(self):
        self.Gegner.Geschwindigkeit -= self.Stufe
        super().loesche(self)