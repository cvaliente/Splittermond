
class Ruestung():
    def __init__(self, name, VTD, SR, Beh, Tick):    
        self.name = name
        self.VTD = VTD
        self.SR = SR
        self.Beh = Beh
        self.Tick = Tick
   
Nackt = Ruestung(name='Nackt',
                        VTD=0,
                        SR=0,
                        Beh=0,
                        Tick=0)       
        
PlattePenUltimo = Ruestung(name='Schuppe Q6+TurmSchild Q4 + 4 Meisterschaften',
                        VTD=6,
                        SR=3,
                        Beh=0,
                        Tick=0)        
    
PlatteUltimo = Ruestung(name='Platte, schwer Q6+TurmSchild Q4 + 4 Meisterschaften',
                        VTD=6,
                        SR=4,
                        Beh=0,
                        Tick=1)

Hybrid = Ruestung(name='Kette schwer Q6, Lederschild Q4 + Ausw II',
                  VTD=7,
                  SR=2,
                  Beh=0,
                  Tick=0)

HybridZH = Ruestung(name='Kette schwer Q6 + Ausw II',
                  VTD=6,
                  SR=2,
                  Beh=0,
                  Tick=0)

Ausweichen = Ruestung(name='Ausweichen III',
                      VTD=6,
                      SR=0,
                      Beh=0,
                      Tick=0)
