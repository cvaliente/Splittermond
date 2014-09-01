import urllib.request
import statistics
from bs4 import BeautifulSoup
from collections import namedtuple, OrderedDict
from operator import attrgetter

def bbcode(tag, string, value = None):
    if value:
        return'['+tag+'='+value+']'+string+'[/'+tag+']'
    else:        
        return'['+tag+']'+string+'[/'+tag+']'

def bbcodeurl(urlstring,urlname):
    return bbcode('url',urlname, urlstring)
    #return '[url='+urlstring+']'+urlname+'[/url]'

def bbbold(text):
    return bbcode(tag='b', string = text)

def bbtt(text):
    return bbcode(tag='tt', string = text)

class bbtable():
    def __init__(self,rows):
        self.elements = rows
    
    def tablify(self, rows):
        return str('[table]\r\n' + rows + '[/table]')    
    
    def __str__(self):
        return(self.tablify(''.join(str(row) for row in self.elements)))

class tablerow(bbtable):    
    def cellify(self, rowfield):
        return str('[td]' + str(rowfield)+'[/td]')
    
    def rowify(self, cells):
        return str('[tr]' + str(cells)+'[/tr]\r\n')
    
    def __str__(self):
        return(self.rowify(''.join(self.cellify(field) for field in self.elements)))
        

class tableheaderrow(tablerow):
    def cellify(self, rowfield):
        return str('[td]' + bbbold(rowfield)+bbtt('   ')+'[/td]')

def getProdukte(bewertungsthreads):
    
    Produkt = namedtuple('Produkt','name id url Stimmen Durchschnitt Median')
    Produkte = []
    baseurl = "http://forum.splittermond.de/index.php?topic=%d.0"
    
    for threadid in bewertungsthreads:
        url=baseurl % threadid
        page=urllib.request.urlopen(url)
        soup = BeautifulSoup(page.read())
        Produktname = soup.find('title').string.split('/')[0].strip()
        polls = soup.find('dl',{'class':'options'})
        options = polls.findAll('dt',{'class':'middletext'})
        votes = polls.findAll('span',{'class':'percentage'})
        ergebnis = dict(zip([[int(s) for s in option.string.split() if s.isdigit()][0] for option in options], [int(vote.string.split(' ')[0]) for vote in votes]))
        einzelvotes = [item for sublist in [[k] * v for k,v in ergebnis.items()] for item in sublist]
        try:
            durchschnitt = str(round(statistics.mean(einzelvotes),2)) 
            median = str(statistics.median(einzelvotes))
            stimmen = len(einzelvotes)
        except ZeroDivisionError:
            durchschnitt = 'No votes yet'
            median = 'No votes yet'
        Produkte.append(Produkt(Produktname, threadid, url, stimmen, durchschnitt, median))
    return Produkte


def generateTable(bewertungsthreads):
    return bbtable([tableheaderrow(['Platz', 'Bewertung', 'Median', 'Stimmen', 'Produkt'])] 
            + [tablerow([index+1, element.Durchschnitt, element.Median, element.Stimmen, bbcodeurl(element.url, element.name)]) 
               for index, element in enumerate(sorted(bewertungsthreads, key=attrgetter('Durchschnitt')))])

Produktthreads = OrderedDict([
('Spielhilfen' , [1676, 1418]),
('Kaufabenteuer' ,[2003, 2097]),
('Kostenlos verfügbare Abenteuer' , [2097,2098, 2099, 2100, 2101,2219])
])


bewertungen = set([item for sublist in [getProdukte(threads) for threads in Produktthreads.values()] for item in sublist])
print('Hier die Sammlung aller Produktbewertungsthreads, inklusive Durchschnittsbewertung und Ranking.')
print('Ich versuche das Ganze auf aktuellen Stand zu halten. :)')
print('Noch ist es nicht sonderlich spektakulär, einfach weil es noch nicht viele Produkte gibt. Aber ich hoffe das ändert sich mit der Zeit. :)')

for key, value in Produktthreads.items():
    print('\r\n'+bbbold(key))
    print(generateTable([Spielhilfe for Spielhilfe in bewertungen if Spielhilfe.id in value]))
    
    