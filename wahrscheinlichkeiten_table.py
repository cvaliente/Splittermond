i = 0
sicherheit ={}
risiko ={}
normal ={}
sicherheitmeister ={}
risikomeister ={}
normalmeister ={}
sortiertesorten = [sicherheit,normal,risiko,sicherheitmeister,normalmeister,risikomeister]
sorten = {'Sicherheitswurf':sicherheit, 'Normaler Wurf':normal, 'Risikowurf':risiko, 'Sicherheitswurf als Großmeister':sicherheitmeister, 
          'Normaler Wurf als Großmeister':normalmeister, 'Risikowurf als Großmeister':risikomeister}

for ergebnis in range(1,22):
    for element in sorten:
        sorten[element][ergebnis]=0

for w1 in range(1,11):
    for w2 in range(1,11):
        for w3 in range(1,11):
            for w4 in range(1,11):
                for w5 in range(1,11):
                    i += 1
                    result = sorted([w1,w2,w3,w4])
                    if sum(result[0:2]) < 4:
                        risiko[sum(result[0:2])] +=1
                    else:                        
                        risiko[sum(result[2:4])] +=1
                    sicherheit[max(w1,w2)] += 1
                    normal[w1+w2] += 1                    
                    sicherheitmeister[max(w1,w2,w5)] += 1
                    if w1+w2 <4 :
                        normalmeister[w1+w2] += 1
                    else:
                        normalmeister[w1+w2+w5-min(w1,w2,w5)]+= 1
                    result = sorted([w1,w2,w3,w4])
                    if sum(result[0:2]) < 4:
                        risikomeister[sum(result[0:2])] +=1
                    else:                        
                        risikomeister[sum(sorted([w1,w2,w3,w4,w5])[3:5])] +=1

for ergebnis in sortiertesorten:
    summe = 0
    durchschnitt = 0
    for k, v in sorten.items():
         if v == ergebnis:
            print('\r\r=== ' + k + ' ===\r{| class="wikitable sortable"')
            print('|-\r! Ergebnis !! Wahrscheinlichkeit !! Kumulierte Wahrscheinlichkeit')
            for x in sorten[k]:
                v = sorten[k][x]*100/i
                durchschnitt += sorten[k][x]*x
                sorten[k][x] = [round(sorten[k][x]*100/i,2),round(100-summe,2)]        
                summe +=v 
                if x < 21:  
                    print('|-\r| '+ str(x) + ' || ' + str(sorten[k][x][0]) + ' || ' + str(sorten[k][x][1]))
            sorten[k][21] = durchschnitt/i
            print('|-\r| Durchschnitt: || ' + str(durchschnitt/i) + ' || \r|}')
    
    
    

'''
tablestring = '[table]'
for i in range(1,3):
    tablestring += '[tr][td]'
    for x in range(1,4):
        for name, value in sorten.items():
            if value == sortiertesorten[x+3*(i-1)-1]:
                tablestring += '[size=11pt][B]'+name +'[/B][/size][/td][td] Durchschnitt: '+str(value[21])+'[/td][td][/td][td][/td][td]'
    tablestring +='[/tr]\r\n[tr]'
    for x in range(1,4):
        tablestring +='[td]Ergebnis[/td][td]Wahrscheinlichkeit[/td][td] kumulierte Wahrscheinlichkeit[/td][td]      [/td]'
    tablestring +='[/tr]\r\n'
    for ergebniss in range(1,21):
        tablestring +='[tr]'
        for x in range(1,4):
            for name, value in sorten.items():
                if value == sortiertesorten[x*i-1]:
                    tablestring += '[td]'+str(ergebniss)+'[/td][td]'+str(value[ergebniss][0])+'%[/td][td]'+str(value[ergebniss][1])+'%[/td][td]      [/td]'
        
        tablestring +='[/tr]\r\n'
    tablestring += '[tr][/tr][tr][/tr]'
                

tablestring += '[/table]'
'''


    

