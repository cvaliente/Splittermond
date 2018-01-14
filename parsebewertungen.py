#!/usr/bin/python
# coding=utf-8

import urllib.request
from statistics import StatisticsError, mean
from bs4 import BeautifulSoup
from collections import namedtuple, OrderedDict
from operator import attrgetter
from multiprocessing.dummy import Pool as ThreadPool

# Collection of Thread IDs in several categories
Produktthreads = OrderedDict([
    ('Spielhilfen', [
     1676, 1418, 2653, 3340, 3341, 3510, 4023, 4241, 4389, 4682, 4681, 5170, 4868, 5089, 5414, 5668, 5785]),
    ('Zubehör', [
     2361, 3345, 3158, 3344, 5115, 5550]),
    ('Kaufabenteuer', [
     2003, 2097, 2360, 2752, 3006, 3343, 3342, 3523, 3524, 3525, 2652, 2651, 3817, 4098, 4244, 4245, 4252, 4302, 4690, 4744, 4745, 5171, 5175, 5174, 5172, 5173, 5373, 5538, 5549, 5537, 5536, 5535, 5696, 5787, 5786]),
    ('Kostenlos verfügbare Abenteuer',
     [2097, 2098, 2099, 2100, 2101, 2652, 2651, 4253])
])

# maintain anthologies separately
Anthologien = OrderedDict([
                           ('Unter Wölfen',[
                                            3523, 3524, 3525]),
                           ('Zwischen den Welten',[
                                            5009, 5010, 5011]),
                           ('An den Küsten der Kristallsee',[
                                                             3828, 3827, 3817, 3826]),
                           ('Alter Friede, neuer Streit',[
                                            5173, 5174, 5175]),
                           ('Verwunschene Mauern',[
                                            5537, 5536, 5535])
                           ])


# Add anthologies to collection to avoid duplicates
for Anthologie in Anthologien:
    for threadid in Anthologien[Anthologie]:
        if threadid not in Produktthreads['Kaufabenteuer']:
            Produktthreads['Kaufabenteuer'].append(threadid)

# URL of a thread (%d will be thread_id)
baseurl = "http://forum.splittermond.de/index.php?topic=%d.0"

# Number of parallel threads (should be equal to number of CPU cores)
concurrent_parses = 4


def bbcode(tag, string, value=None):
    """Return a text(string) enclosed by the bbcode tags"""
    if value:
        return'[' + tag + '=' + value + ']' + string + '[/' + tag + ']'
    else:
        return'[' + tag + ']' + string + '[/' + tag + ']'


def bbcodeurl(urlstring, urlname):
    """Return an bbcode url format for given url and description"""
    return bbcode('url', urlname, urlstring)


def bbbold(text):
    """Return the text with a bbcode bold tag"""
    return bbcode(tag='b', string=text)


def bbtt(text):
    """Return the text with a bbcode tt tag"""
    return bbcode(tag='tt', string=text)


class bbtable():

    """creates the frame of a bbcode table"""

    def __init__(self, rows):
        """needs the rows as input for this table"""
        self.elements = rows

    def tablify(self, rows):
        """adds start and end tags for tables"""
        return str('[table]\r\n' + rows + '[/table]')

    def __str__(self):
        """prints table in bbcode format"""
        return(self.tablify(''.join(str(row) for row in self.elements)))


class tablerow(bbtable):

    """creates a bbcode table row with correct tags"""

    def cellify(self, rowfield):
        """encloses cells with correct tags"""
        return str('[td]' + str(rowfield) + '[/td]')

    def rowify(self, cells):
        """encloses rows with the correct tags"""
        return str('[tr]' + str(cells) + '[/tr]\r\n')

    def __str__(self):
        """adds cell and row tags to elements"""
        return(self.rowify(''.join(self.cellify(field) for field in self.elements)))


class tableheaderrow(tablerow):

    """adds a header row"""

    def cellify(self, rowfield):
        return str('[td]' + bbbold(rowfield) + bbtt('   ') + '[/td]')


class ProduktParser():

    def __init__(self, Produktthreads, Produkt = namedtuple('Produkt', 'name id url Stimmen Durchschnitt'), Produkte = [], Anthologien = [], baseurl = baseurl):
        """set base properties: URLs, thread ids, format"""
        self.Produkt = Produkt
        self.Produkte = Produkte
        self.baseurl = baseurl
        self.Produktthreads = Produktthreads
        self.Anthologien = Anthologien
        self.bewertungen = set(
            [item for sublist in self.Produktthreads.values() for item in sublist])
        self.pool = ThreadPool(concurrent_parses)
        self.pool.map(self.getProdukt, self.bewertungen)
        self.getAnthologie()

    def getProdukt(self, threadid):
        """collect information for selected thread id"""
        url = self.baseurl % threadid
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page.read(), "html.parser")
        Produktname = soup.find('title').string.split('/')[0].strip()
        polls = soup.find('dl', {'class': 'options'})
        options = polls.findAll('dt', {'class': 'middletext'})
        votes = polls.findAll('span', {'class': 'percentage'})
        ergebnis = dict(zip([[int(s) for s in option.string.split() if s.isdigit()][
                        0] for option in options], [int(vote.string.split(' ')[0]) for vote in votes]))
        einzelvotes = [
            item for sublist in [[k] * v for k, v in ergebnis.items()] for item in sublist]
        try:
            durchschnitt = str(round(mean(einzelvotes), 2))
            stimmen = len(einzelvotes)
        except (ZeroDivisionError, StatisticsError) as e:
            durchschnitt = 'No votes yet'
            stimmen = 0
        self.Produkte.append(
            self.Produkt(Produktname, threadid, url, stimmen, durchschnitt))
        
    def getAnthologie(self):
        for Anthologie in self.Anthologien:
            Anthologiedurchschnittagg = 0
            Anthologiestimmen = 0
            for Spielhilfe in self.Produkte:
                if Spielhilfe.id in self.Anthologien[Anthologie]:
                    if  Spielhilfe.Durchschnitt != 'No votes yet':
                        Anthologiestimmen += Spielhilfe.Stimmen  
                        Anthologiedurchschnittagg += Spielhilfe.Stimmen * float(Spielhilfe.Durchschnitt)
            if Anthologiestimmen == 0:
                Anthologiedurchschnitt = 'No votes yet'
            else:
                Anthologiedurchschnitt = str(round(Anthologiedurchschnittagg/Anthologiestimmen, 2))
                          
            self.Produkte.append(
                self.Produkt(Anthologie, 0, 0, Anthologiestimmen, Anthologiedurchschnitt))
                    

    def generateTable(self, bewertungsthreads):
        """"generate a table for the threads"""
        return bbtable([tableheaderrow(['Platz', 'Bewertung', 'Stimmen', 'Produkt'])]
                       + [tablerow([index + 1, element.Durchschnitt, element.Stimmen, bbcodeurl(element.url, element.name)])
                          for index, element in enumerate(sorted(bewertungsthreads, key=attrgetter('Durchschnitt')))])

    def printProdukte(self):
        """"print the table"""
        for key, value in self.Produktthreads.items():
            print('\r\n' + bbbold(key))
            print(self.generateTable(
                [Spielhilfe for Spielhilfe in self.Produkte if Spielhilfe.id in value]))
            
        print('\r\n' + bbbold("Anthologien"))
        print(self.generateTable(
            [Spielhilfe for Spielhilfe in self.Produkte if Spielhilfe.name in [Anthologie for Anthologie in Anthologien]]))


if __name__ == '__main__':
    SplittermondParser = ProduktParser(Produktthreads=Produktthreads, Anthologien=Anthologien)
    print(
        'Hier die Sammlung aller Produktbewertungsthreads, inklusive Durchschnittsbewertung und Ranking.')
    print(
        'Das script ist verfügbar unter https://github.com/zaboron/Splittermond/blob/master/parsebewertungen.py')
    SplittermondParser.printProdukte()
