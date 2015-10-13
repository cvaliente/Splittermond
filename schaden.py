s = 0
for i in range(1,11):
    for j in range(1,11):
        for k in range(1,11):
            m = max(i,j,k)
            if m == 10:
                m=13
            s += m
            
print(s/1000)


s = 0
for i in range(1,11):
    for j in range(1,11):
        for k in range(1,11):
            for l in range(1,11):
                m = max(i,j,k,l)
                if m == 10:
                    m=15
                s += m
print(s/10000)
