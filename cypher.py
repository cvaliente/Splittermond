import string
from collections import Counter
from random import random
import operator
codestring = 'vkuvdgvdhowhjhulqrhqxqgehidoglhcxeudvfkdwqxgpughvlhzrowhlpdqhlhdqhpkwxgnhlhxvhuuvfkzuqkwhdkwhucloghukzdhqvfodqjhcrjhwyloxoqjhevuvklvdglhyhuxfwhpwhlhpdqyhuoxfwhvhvvlquhpyuolvhzloikhqkhghflcfhvkvhvwcxehlhq'
cypher = {}

lettercount = Counter(codestring).most_common()

buchstabenhaeufigkeit = {'E':17.40,
'N':9.78,
'I':7.55, 
'S':7.27, 
'R':7.00, 
'A':6.51, 
'T':6.15, 
'D':5.08, 
'H':4.76, 
'U':4.35, 
'L':3.44, 
'C':3.06, 
'G':3.01, 
'M':2.53, 
'O':2.51, 
'B':1.89, 
'W':1.89, 
'F':1.66, 
'K':1.21, 
'Z':1.13, 
'P':0.79, 
'V':0.67, 
'J':0.27, 
'Y':0.04, 
'X':0.03, 
'Q':0.02, 
}

for i in range(0,10000):
    buchstabenhaeufigkeit_random = {}
    
    for letter, value in buchstabenhaeufigkeit.items():
        buchstabenhaeufigkeit_random[letter] = value * (0.5 + (random()/1))
    
    sorted_buchstabenhaeufigkeit = sorted(buchstabenhaeufigkeit_random.items(), key=lambda x: x[1], reverse=True)
    
    
    for element in list(zip(lettercount, sorted_buchstabenhaeufigkeit)):
        cypher[element[0][0]]=element[1][0]
    
    
    for letter in string.ascii_lowercase:
        if letter not in cypher.keys():
            cypher[letter] = letter
         
    decodestring = ''   
    for letter in codestring:
        decodestring += cypher[letter]
        
    if 'UNG' in decodestring and 'EIN' in decodestring and 'IST' in decodestring:
        print(decodestring)

