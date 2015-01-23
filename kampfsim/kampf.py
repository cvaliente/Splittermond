from random import shuffle
import logging

class Kampf:        
    Positions = {}  
    def __init__(self, Runden = 1):
        self.Runden = Runden
        self.Teilnehmer = []
        self.Tickleiste = Tickleiste()
        
    def neustartKampf(self):
        
        self.Runden -= 1
        
        shuffle(self.Teilnehmer)
        self.Tickleiste.leere()
        
        for Charakter in self.Teilnehmer:
            Charakter.neustartCharakter()
        
            
    def SiegerMeldung(self, Teilnehmer):
        for ang in Teilnehmer:
            ang.siege += 1
        logging.warning("---------------------")
        logging.warning(', '.join(ang.name for ang in Teilnehmer) + " gewinnt!")
        logging.warning("---------------------")
            
    def Arena(self, Angreifer, Verteidiger):
            
        for Kaempfer in Angreifer + Verteidiger:
            Kaempfer.Tickleiste = self.Tickleiste     
            self.Teilnehmer.append(Kaempfer)
        
        
        for Charakter in self.Teilnehmer:
            Charakter.siege = 0
        
        while self.Runden > 0:
            
            self.neustartKampf()
            
            logging.info("~~~~~~~~~~ Kampfbeginn ~~~~~~~")
                
            while sum(max(vtd.hp,0) for vtd in Verteidiger) > 0 and sum(max(ang.hp,0) for ang in Angreifer) > 0:
                for kaempfer in Angreifer:
                    kaempfer.Gegner = [geg for geg in Verteidiger if geg.hp > 0][0]
                for kaempfer in Verteidiger:
                    kaempfer.Gegner = [geg for geg in Angreifer if geg.hp > 0][0]
                if self.Tickleiste.tick():
                    logging.info("####################")
                    for Kaempfer in Angreifer + Verteidiger:
                        logging.info("Ticks:" + str(Kaempfer.name) + " " + str(self.Tickleiste.bestimmePosition(Kaempfer)))
                        logging.info("LP:" + str(Kaempfer.name) + " " + str(Kaempfer.hp))
                    logging.info("---")
                
                
        
            if sum(max(ang.hp,0) for ang in Angreifer) > 0:
                self.SiegerMeldung(Angreifer)
            else:
                self.SiegerMeldung(Verteidiger)
        for Kaempfer in Angreifer + Verteidiger:
            logging.info(Kaempfer.name + " gewinnt " + str(Kaempfer.siege) + " Mal.")
        
        #return [Angreifer.siege, Verteidiger.siege]
    
    

    
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
        i = False
        j = False
        while self.Tickleiste.get(self.Position) is not None and self.Tickleiste.get(self.Position):
            if not j:
                logging.info("Tickleiste: " + str(self.Position))
                j = True
            self.Tickleiste.get(self.Position)[0].waehleAktion()
            i = True            
        self.Position += 1
        return i
    



