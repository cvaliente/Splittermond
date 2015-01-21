from wuerfelklasse import WuerfelProbe, wuerfelSchaden

class Zauber():

    def __init__(self, name, Kosten, Ticks, prio, Zauberwert, stapelbar=0):    
        self.name = name
        self.Kosten = Kosten
        self.Ticks = Ticks
        self.prio = prio
        self.Zauberwert = Zauberwert
        self.aktiv = 0
        self.stapelbar = stapelbar
        
    def allg_zaubern(self, Zauberer, Schwierigkeit):
        if self.Kosten <= Zauberer.Fokus:
            Zauberer.bewegeTicks(self.Ticks + 3)
            WuerfelErgebnis = list(WuerfelProbe(self.Zauberwert - Zauberer.status, Schwierigkeit))
            if WuerfelErgebnis[0] >= 0:
                Zauberer.verzehrFokus(self.Kosten)
                return(WuerfelErgebnis)
            else:
                Zauberer.verzehrFokus(-WuerfelErgebnis[1])
                return(WuerfelErgebnis)
                

            
class Blitzschlag(Zauber):    
    def __init__(self, prio, Zauberwert):
        super(Blitzschlag, self).__init__("magischer Schlag", 4, 4, prio, Zauberwert, 1)
        self.Schaden = [1, 6, 3]
        
    def zaubern(self, Zauberer, Ziel):
        tp = 0
        ZauberErgebnis = self.allg_zaubern(Zauberer, Ziel.Verteidigung)
        if ZauberErgebnis[0] >= 0:
            tp = wuerfelSchaden(self.Schaden) + ZauberErgebnis[1]
            Ziel.nimmSchaden(tp)
        return(ZauberErgebnis[0])
        
class magischerSchlag(Zauber):    
    def __init__(self, prio, Zauberwert):
        super(magischerSchlag, self).__init__("magischer Schlag", 4, 4, prio, Zauberwert, 1)
        self.Schaden = [1, 6, 3]
        
    def zaubern(self, Zauberer, Ziel):
        tp = 0
        ZauberErgebnis = self.allg_zaubern(Zauberer, Ziel.Verteidigung)
        if ZauberErgebnis[0] >= 0:
            tp = wuerfelSchaden(self.Schaden) + ZauberErgebnis[1]
            Ziel.nimmSchaden(tp)
        return(ZauberErgebnis[0])
            
        
class magischeRuestung(Zauber):    
    def __init__(self, prio, Zauberwert):
        super(magischeRuestung, self).__init__("magische ruestung", 4, 1, prio, Zauberwert)
        
    def zaubern(self, Zauberer, Ziel):
        ZauberErgebnis = self.allg_zaubern(Zauberer, 18)
        if ZauberErgebnis[0] >= 0:
            Zauberer.Verteidigung += 2
            self.aktiv = 1
        return(ZauberErgebnis[0])

        
class flammendeWaffe(Zauber):    
    def __init__(self, prio, Zauberwert):
        super(flammendeWaffe, self).__init__("flammende Waffe", 4, 2, prio, Zauberwert)
        
    def zaubern(self, Zauberer, Ziel):
        ZauberErgebnis = self.allg_zaubern(Zauberer, 18)
        if ZauberErgebnis[0] >= 0:
            Zauberer.Schaden[2] = Zauberer.Schaden[2] + 1
            self.aktiv = 1
        return(ZauberErgebnis[0])
