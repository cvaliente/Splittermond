from random import shuffle

class Kampf:        
    Positions = {}  
    def __init__(self, verbose=0):
        self.verbose = verbose
        self.Runden = 1
        self.Teilnehmer = []
        self.Tickleiste = Tickleiste()
        
    def neustartKampf(self):
        
        self.Runden -= 1
        
        shuffle(self.Teilnehmer)
        self.Tickleiste.leere()
        
        for Charakter in self.Teilnehmer:
            Charakter.neustartCharakter()
        
            
    def SiegerMeldung(self, Teilnehmer):
        Teilnehmer.siege += 1
        if self.verbose >= 2:
            print("---------------------")
            print(Teilnehmer.name + " gewinnt!")
            print("---------------------")
            
    def Arena(self, Angreifer, Verteidiger):
        if self.Runden > 10 and self.verbose > 0:
            self.verbose = 0
            
        for Kaempfer in (Angreifer, Verteidiger):
            Kaempfer.Tickleiste = self.Tickleiste      
            Kaempfer.verbose = self.verbose  
            self.Teilnehmer.append(Kaempfer)
        
        Angreifer.Gegner = Verteidiger
        Verteidiger.Gegner = Angreifer    
        
        for Charakter in self.Teilnehmer:
            Charakter.siege = 0
        
        while self.Runden > 0:
            
            self.neustartKampf()
                
            while Verteidiger.hp > 0 and Angreifer.hp > 0:
                if self.verbose >= 1:
                    print("####################")
                    print("Tickleiste: " + str(self.Tickleiste.Position))
                    print("Ticks:" + str(Angreifer.name) + " " + str(self.Tickleiste.bestimmePosition(Angreifer)) + " " + str(Verteidiger.name) + " " + str(self.Tickleiste.bestimmePosition(Verteidiger)))
                    print("LP:" + str(Angreifer.name) + " " + str(Angreifer.hp) + " " + str(Verteidiger.name) + " " + str(Verteidiger.hp))
                    print("Fokus:" + str(Angreifer.name) + " " + str(Angreifer.Fokus) + " " + str(Verteidiger.name) + " " + str(Verteidiger.Fokus))
                    print("---")
                
                self.Tickleiste.tick()
        
            if Angreifer.hp > 0:
                self.SiegerMeldung(Angreifer)
            else:
                self.SiegerMeldung(Verteidiger)
        if self.verbose >= 0:
            print(Angreifer.name + " gewinnt " + str(Angreifer.siege) + " Mal,\n" + Verteidiger.name + " gewinnt " + str(Verteidiger.siege) + " Mal.")
        
        return [Angreifer.siege, Verteidiger.siege]
    
    

    
class Tickleiste():
    def __init__(self):
        self.Tickleiste = {}
        self.Position = -20
        
    def initiere(self, Teilnehmer, Tick):
        if self.Tickleiste.get(Tick) is not None:
            self.Tickleiste[Tick].append(Teilnehmer)
        else:
            self.Tickleiste[Tick] = [Teilnehmer]
        
    def bestimmePosition(self,Teilnehmer):
        for tick in self.Tickleiste:
            if Teilnehmer in self.Tickleiste[tick]:
                return tick
                break
            
    def bewege(self, Teilnehmer, Ticks):
        tick = self.bestimmePosition(Teilnehmer)
        self.Tickleiste[tick].remove(Teilnehmer)                
        self.initiere(Teilnehmer, tick+Ticks)
    
    def leere(self):
        self.Tickleiste = {}
        self.Position = -20
        
    def loesche(self,Teilnehmer):
        self.Tickleiste[self.bestimmePosition(Teilnehmer)].remove(Teilnehmer)
                
    def tick(self):
        while self.Tickleiste.get(self.Position) is not None and self.Tickleiste.get(self.Position):
            self.Tickleiste.get(self.Position)[0].waehleAktion()            
        self.Position += 1
    



