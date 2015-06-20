# functions.strings
# Some string functions that were/will be useful in
# the project

import difflib

def diff(a,b):
  for x,y in enumerate(difflib.ndiff(a,b)):
    if y[0] == '-':
      print 'Delete {} from position {}'.format(y[-1], x)
    elif y[0] == '+':
      print 'Add {} from position {}'.format(y[-1], x) 
