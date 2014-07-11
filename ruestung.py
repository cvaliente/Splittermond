from collections import namedtuple

Ruestung = namedtuple('Ruestung', 'name VTD SR Beh Tick')
   
Nackt = Ruestung('Nackt', 0, 0, 0, 0)       
        
PlattePenUltimo = Ruestung('Schuppe Q6+TurmSchild Q4 + 4 Meisterschaften', 6, 3, 0, 0)        
    
PlatteUltimo = Ruestung('Platte, schwer Q6+TurmSchild Q4 + 4 Meisterschaften', 6, 4, 0, 1)

Hybrid = Ruestung('Kette schwer Q6, Lederschild Q4 + Ausw II', 7, 2, 0, 0)

HybridZH = Ruestung('Kette schwer Q6 + Ausw II', 6, 2, 0, 0)

Ausweichen = Ruestung('Ausweichen III', 6, 0, 0, 0)
