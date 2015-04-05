##numplot simple statistics generation
##This program converts a csv file with one row of data into a short list of the 
##frequency and percentage of each item in that row.

##Instructions:
##First, put this file in the same directory as a csv file with one row of relevant data.  
##Name that data data.csv
##In the console, cd into that folder and run 'python numplot.py'
##Instructions:
##First, put this file in the same directory as a csv file with one row of relevant data.  
##Name that data data.csv
##In the console, cd into that folder and run 'python numplot.py'

##Instructions:
##First, put this file in the same directory as a csv file with one row of relevant data.  
##Name that data data.csv
##In the console, cd into that folder and run 'python numplot.py'

##Instructions:
##First, put this file in the same directory as a csv file with one row of relevant data.  
##Name that data data.csv
##In the console, cd into that folder and run 'python numplot.py'

##Example Input: A CSV file with 1 row 82 columns, each cell containing a 1,2 or 3
##Example Output: 
# '1': 36, 43.9%
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
