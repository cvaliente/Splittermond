from random import shuffle


class Kampf:        
    Positions = {}  
    def __init__(self, verbose=0):
        self.verbose = verbose
        self.Runden = 1
        self.Teilnehmer = []
        
    def neustartKampf(self):
        
        self.Runden -= 1
        
        shuffle(self.Teilnehmer)
        
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
        
        self.Teilnehmer.append(Angreifer)
        self.Teilnehmer.append(Verteidiger)
        
        for Charakter in self.Teilnehmer:
            Charakter.siege = 0
        
        while self.Runden > 0:
            
            self.neustartKampf()
                
            while Verteidiger.hp > 0 and Angreifer.hp > 0:
                if self.verbose >= 1:
                    print("####################")
                    print("Ticks:" + str(Angreifer.name) + " " + str(Angreifer.TickPosition) + " " + str(Verteidiger.name) + " " + str(Verteidiger.TickPosition))
                    print("LP:" + str(Angreifer.name) + " " + str(Angreifer.hp) + " " + str(Verteidiger.name) + " " + str(Verteidiger.hp))
                    print("Fokus:" + str(Angreifer.name) + " " + str(Angreifer.Fokus) + " " + str(Verteidiger.name) + " " + str(Verteidiger.Fokus))
                    print("---")
                
                min(self.Positions, key=self.Positions.get).waehleAktion(max(self.Positions, key=self.Positions.get), self.verbose)
        
            if Angreifer.hp > 0:
                self.SiegerMeldung(Angreifer)
            else:
                self.SiegerMeldung(Verteidiger)
        if self.verbose >= 0:
            print(Angreifer.name + " gewinnt " + str(Angreifer.siege) + " Mal,\n" + Verteidiger.name + " gewinnt " + str(Verteidiger.siege) + " Mal.")
        
        return [Angreifer.siege, Verteidiger.siege]
    
    

    
    
    



