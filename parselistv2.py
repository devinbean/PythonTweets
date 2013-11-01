import csv
from itertools import chain
from collections import Counter
from operator import itemgetter 
import re

def flatten(listOfLists):
    "Flatten one level of nesting"
    return chain.from_iterable(listOfLists)

text = []
finaltext = []
counter = 0
type = raw_input('search or list? ')
type1 = raw_input('handle or words? ')

if type in 'search':
    w = raw_input('Search term: ')

with open('tweets.csv', 'rU') as tweets:
    reader = csv.reader(tweets)
    for all in reader:

        text.append(all[7:8])

flattext = flatten(text)

for all in flattext:

    finaltext.append(all)

if type1 in 'handle':

    counts = Counter()
    handles = re.compile(r'@([A-Za-z0-9_]+)')

    for sentence in finaltext:
        counts.update(handles.findall(sentence.lower()))

if type1 in 'words':

    counts = Counter()
    
    words = re.compile(r'(?<!@)\b\w+')
    
    for sentence in finaltext:
        counts.update(words.findall(sentence.lower()))


if type in 'list':
    for w,c in sorted(counts.iteritems(), key = itemgetter(1), reverse=True):
        print '{0:10} ==> {1:10d}'.format(w, c)

if type in 'search':
    print counts[w]






    