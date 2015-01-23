from random import randrange

def WuerfelProbe(basis,zielwert, probentyp = 0): 
    #probentyp 1: risiko
    #probentyp 0: standard
    #sonst: sicherheit
    krit = False
    patzer = False
    wurf = [randrange(1,11), randrange(1,11)]
    
    if probentyp == 0: #standardwurf
        x = sum(wurf)
        if x > 18:
            krit = True
        if x < 4: 
            patzer = True
    elif probentyp == 1: #risikowurf
        result = sorted(wurf + [randrange(1,11), randrange(1,11)])
        if sum(result[0:2]) < 4:
            x = sum(result[0:2])
            patzer = True            
        else:
            x = sum(result[2:4])
            if x > 18:
                krit = True
    else: #sonst: sicherheitswurf.
        x = max(wurf)
        
    
    roll = basis + x - zielwert
    
    
    
    return [roll , int(roll/3), patzer, krit]
        
def wuerfelSchaden(Schaden, Scharf = 1):
    return sum([max(Scharf,randrange(1,Schaden[1]+1)) for _ in range(Schaden[0])])+Schaden[2]

def PatzerWurf():
    return randrange(1,11)+ randrange(1,11)