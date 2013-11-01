import csv
from itertools import chain
from collections import Counter
import re

def flatten(listOfLists):
    "Flatten one level of nesting"
    return chain.from_iterable(listOfLists)

text = []
finaltext = []
counter = 0
w = raw_input('--> ')

with open('tweets.csv', 'rU') as tweets:
    reader = csv.reader(tweets)
    for all in reader:

        text.append(all[7:8])

flattext = flatten(text)

for all in flattext:

    finaltext.append(all)


counts = Counter()
words = re.compile(r'\w+')

for sentence in finaltext:
    counts.update(words.findall(sentence.lower()))

print counts[w]






    