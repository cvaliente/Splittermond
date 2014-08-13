import urllib.request
from bs4 import BeautifulSoup
from collections import namedtuple
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
    
    Produkt = namedtuple('Produkt','name id url Stimmen Durchschnitt')
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
        try:
            average = str(round(sum(k*v for k,v in ergebnis.items()) / sum(v for k,v in ergebnis.items()),2))
        except ZeroDivisionError:
            average = 'No votes yet'
        Produkte.append(Produkt(Produktname, threadid, url, str(sum(v for k,v in ergebnis.items())), average))
    return Produkte


def generateTable(bewertungsthreads):
    return bbtable([tableheaderrow(['Platz', 'Bewertung', 'Stimmen', 'Produkt'])] 
            + [tablerow([index+1, element.Durchschnitt, element.Stimmen, bbcodeurl(element.url, element.name)]) 
               for index, element in enumerate(sorted(bewertungsthreads, key=attrgetter('Durchschnitt')))])

abenteuer = [2003, 2097,2098, 2099, 2100, 2101]
spielhilfen = [1676, 1418]

bewertungen = getProdukte(abenteuer+spielhilfen)

Abenteuerbewertungen = [Abenteuer for Abenteuer in bewertungen if Abenteuer.id in abenteuer]

Spielhilfenbewertungen = [Spielhilfe for Spielhilfe in bewertungen if Spielhilfe.id in spielhilfen]
print('Hier die Sammlung aller Produktbewertungsthreads, inklusive Durchschnittsbewertung und Ranking.')
print('Ich versuche das Ganze auf aktuellen Stand zu halten. :)')
print('Noch ist es nicht sonderlich spektakulär, einfach weil es noch nicht viele Produkte gibt. Aber ich hoffe das ändert sich mit der Zeit. :)')
print(bbbold('\r\nSpielhilfen'))
print(generateTable(Spielhilfenbewertungen))
print(bbbold('\r\nAbenteuer'))
print(generateTable(Abenteuerbewertungen))