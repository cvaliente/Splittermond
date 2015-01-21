from random import randrange

def WuerfelProbe(basis,zielwert, probentyp = 0): 
    #probentyp 1: risiko
    #probentyp 0: standard
    #sonst: sicherheit
    wurf = [randrange(1,11), randrange(1,11)]
    
    if probentyp == 0: #standardwurf
        x = sum(wurf)
    elif probentyp == 1: #risikowurf
        result = sorted(wurf + [randrange(1,11), randrange(1,11)])
        if sum(result[0:2]) < 4:
            x = sum(result[0:2])
        else:
            x = sum(result[2:4])
    else: #sonst: sicherheitswurf.
        x = max(wurf)
    
    roll = basis + x - zielwert
    
    return [roll + (int(x > 18) - int(x < 4)) * 9 , int(roll/3) + (int(x > 18) - int(x < 4)) * 3, int(x < 4)]
        
def wuerfelSchaden(Schaden, Scharf = 1):
    return sum([max(Scharf,randrange(1,Schaden[1]+1)) for _ in range(Schaden[0])])+Schaden[2]

def PatzerWurf():
    return randrange(1,11)+ randrange(1,11)