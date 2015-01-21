from random import randint

def WuerfelProbe(basis,zielwert, probentyp = 0): 
    #probentyp 1: risiko
    #probentyp 0: standard
    #sonst: sicherheit
    wurf = [randint(1,10), randint(1,10)]
    
    if probentyp == 0: #standardwurf
        x = sum(wurf)
    elif probentyp == 1: #risikowurf
        result = sorted(wurf + [randint(1,10), randint(1,10)])
        if sum(result[0:2]) < 4:
            x = sum(result[0:2])
        else:
            x = sum(result[2:4])
    else: #sonst: sicherheitswurf.
        x = max(wurf)
    
    roll = basis + x - zielwert
    
    return [roll + (int(x > 18) - int(x < 4)) * 9 , int(roll/3) + (int(x > 18) - int(x < 4)) * 3, int(x < 4)]
        
def wuerfelSchaden(Schaden, Scharf = 1):
    return sum([max(Scharf,randint(1,Schaden[1])) for _ in range(Schaden[0])])+Schaden[2]