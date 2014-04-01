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

w = raw_input('Search term: ')

with open('tweets.csv', 'rU') as tweets:
    reader = csv.reader(tweets)
    for all in reader:

        text.append(all[7:8])

flattext = flatten(text)

for all in flattext:

    finaltext.append(all)


for line in finaltext:
    if re.search(w, line, re.IGNORECASE):
        print line





