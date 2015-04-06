##numplot simple statistics generation
##This program converts a csv file with one row of data into a short list of the 
##frequency and percentage of each item in that row.

##Instructions:
##First, put this file in the same directory as a csv file with one row of relevant data.  
##Name that data data.csv
##In the console, cd into that folder and run 'python numplot.py'

##Example Input: A CSV file with 1 row 82 columns, each cell containing a 1,2 or 3
##Example Output: 
# '1': 36, 43.9%
# '0': 30, 36.6%
# '2': 16, 19.5%
# '1': 36, 43.9%
# '0': 30, 36.6%
# '2': 16, 19.5%# '1': 36, 43.9%
# '0': 30, 36.6%
# '2': 16, 19.5%# '1': 36, 43.9%
# '0': 30, 36.6%
# '2': 16, 19.5%# '1': 36, 43.9%
# '0': 30, 36.6%
# '2': 16, 19.5%# '1': 36, 43.9%
# '0': 30, 36.6%
# '2': 16, 19.5%
from collections import Counter
import csv
import numpy
class Row(object):

    def __init__(self, items=[]):
        self.items = items
        self.total = float(len(items))
        self.order()
        self.add_percentages()

    def __repr__(self):
        return 'Row(%s)' % repr(self.items)

    __str__ = __repr__
    """The str and repr forms of this object are the same."""

    def order(self):
        dictionary = Counter(self.items)
        self.items = dictionary.most_common(100)

    def add_percentages(self):
        self.items = [(q,w,100*w/self.total) for [q,w] in self.items]

    def show_all(self):
        for [a,b,c] in self.items:
            string = "%r: %s, %0.1f%%" % (a,b,c)
            print(string)

def main(script, *args):
    data = numpy.loadtxt('data.csv', dtype=str, delimiter=';')
    print(data)
    a = Row(data)
    print(a)
    a.show_all()

if __name__ == '__main__':
    import sys
    main(*sys.argv)
    
subspecies and the sexes. The wings and lateral tail feathers are bluish 
while the tail is dark green. The legs are grey. The female is 
similar to the male though duller in colouration and has an underwing 
stripe, which is not present in the adult male. Juveniles are duller
than females and have an underwing stripe.[7]
Distribution and habitat[edit]
Natural range is eastern Australia, down to Tasmania. The eastern
rosella is found in lightly wooded country, open forests, 
woodlands, gardens, bushlands and parks.
The eastern rosella (Platycercus eximius) has
become naturalised in New Zealand.[8] By the 1970s
the population, probably originally from cage escapees,
strongly established throughout Auckland, Northland, & 
the far north, extending into west Waikato, as far south
as Kawhia, & Te Kuiti, & East to the Coromandel Peninsula.
Also in the Wellington-Hutt Valley Region, established in the 
1960s from escaped cage birds, later colonising the foothills 
of the Tararua Range, to Eketahuna in the east, & Otaki in the
west[9] (range up to 1985). Sightings from New Plymouth, Taupo,
Gisborne, Tiritea, Banks Peninsula, Nelson area, & Stewart Island.
The first occurrence of these parrots in New Zealand was about 
1910 when a small shipment of eastern rosellas, as well as a few 
crimson rosellas (P. elegans), that had been refused entry into
New Zealand by the Customs Department was released off Otago Heads
by the ship that brought them, as she was returning to Sydney. 
The two species crossed [& by 1955] no pure Crimson Rosellas 
remained in the Dunedin area.[10] The population of rosellas in 
Dunedin has always remained low, partially due to them being 
trapped & sold as caged birds, & that the climate can be extremely 
cold in comparison to their native homeland.
