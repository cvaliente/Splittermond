import urllib.request
import statistics
from bs4 import BeautifulSoup
from collections import namedtuple, OrderedDict
from operator import attrgetter
from multiprocessing.dummy import Pool as ThreadPool

# Collection of Thread IDs in several categories
Produktthreads = OrderedDict([
('Spielhilfen' , [1676, 1418, 2361, 2653, 3344, 3340, 3345, 3158, 3510]),
('Kaufabenteuer' ,[2003, 2097, 2360, 2752, 3006, 3343, 3342]),
('Kostenlos verfügbare Abenteuer' , [2097,2098, 2099, 2100, 2101, 2652, 2651])
])


# URL of a thread (%d will be thread_id)
baseurl = "http://forum.splittermond.de/index.php?topic=%d.0"

# Number of parallel threads (should be equal to number of CPU cores)
concurrent_parses = 4 



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

class ProduktParser():
    def __init__(self, Produktthreads, Produkt = namedtuple('Produkt','name id url Stimmen Durchschnitt Median'), Produkte = [], baseurl = baseurl):
        self.Produkt = Produkt
        self.Produkte = Produkte
        self.baseurl = baseurl
        self.Produktthreads = Produktthreads
        self.bewertungen = set([item for sublist in self.Produktthreads.values() for item in sublist])
        self.pool = ThreadPool(concurrent_parses) 
        self.pool.map(self.getProdukt, self.bewertungen)
        
    def getProdukt(self, threadid):
        url=self.baseurl % threadid
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
            median = statistics.median(einzelvotes)
            if int(median) == median:
                median = int(median)
            median = str(median)
            stimmen = len(einzelvotes)
        except (ZeroDivisionError, statistics.StatisticsError) as e:
            durchschnitt = 'No votes yet'
            median = 'No votes yet'
            stimmen = 0
        self.Produkte.append(self.Produkt(Produktname, threadid, url, stimmen, durchschnitt, median))
        
    
    def generateTable(self, bewertungsthreads):
        return bbtable([tableheaderrow(['Platz', 'Bewertung', 'Median', 'Stimmen', 'Produkt'])] 
            + [tablerow([index+1, element.Durchschnitt, element.Median, element.Stimmen, bbcodeurl(element.url, element.name)]) 
               for index, element in enumerate(sorted(bewertungsthreads, key=attrgetter('Durchschnitt')))])
        
    def printProdukte(self):    
        for key, value in self.Produktthreads.items():
            print('\r\n'+bbbold(key))
            print(self.generateTable([Spielhilfe for Spielhilfe in SplittermondParser.Produkte if Spielhilfe.id in value])) 


if __name__ == '__main__':
    SplittermondParser = ProduktParser(Produktthreads= Produktthreads)
    print('Hier die Sammlung aller Produktbewertungsthreads, inklusive Durchschnittsbewertung und Ranking.')
    print('Ich versuche das Ganze auf aktuellen Stand zu halten. :)')
    print('Noch ist es nicht sonderlich spektakulär, einfach weil es noch nicht viele Produkte gibt. Aber ich hoffe das ändert sich mit der Zeit. :)')
    SplittermondParser.printProdukte()
