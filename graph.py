import csv
from itertools import chain
from collections import Counter
import re
from itertools import islice
import matplotlib.figure as fg
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.dates import date2num


def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

def flatten(listOfLists):
    "Flatten one level of nesting"
    return chain.from_iterable(listOfLists)

worduse = []
dates = []
tentweets = []
datelist = []
flatdates = []
tweetlist = []
finaldate = []
finaltweet = []
reworduse = []

W = raw_input('Search term: ')

with open('tweets.csv', 'rU') as tweets:
    reader = csv.reader(tweets)
    for all in reader:
        
        tweetlist.append(all[7:8])
        dates.append(all[5::6])

flattext = flatten(dates)

for all in flattext:
    
    flatdates.append(all)

datespat = re.compile(r'([0-9]{4,4}-[0-9]{2,2}-[0-9]{2,2})+')
words = re.compile(r'(?<!@)\b\w+')

for all in flatdates:

    datelist.append(datespat.findall(all))


textdate = flatten(datelist)
for all in textdate:
    finaldate.append(all)

texttweet = flatten(tweetlist)
for all in texttweet:
    finaltweet.append(all)

finaltweet.pop(0)

counts = Counter()

tentweets = [finaltweet[x:x+10] for x in xrange(0, len(finaltweet),10)]
tendate = finaldate[0::10]
for list in tentweets:
    for x in list:
        counts.update(words.findall(x.lower()))
    worduse.append(counts[W])
    counts.clear()
    #for all in reversed(worduse):
#reworduse.append(all)
x = range(len(tendate))
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111)
plt.bar(x, worduse, width=0.4)
#plt.xticks(np.arange(min(x), max(x)+1, 2.0), tendate, rotation='vertical')
plt.xticks(x, tendate, rotation='vertical')
plt.ylabel('Word Frequency')
plt.setp(ax.get_xticklabels()[::2], visible=False)
plt.title('"%s" Frequency vs. Date' %W, fontsize=12)
plt.tight_layout()
plt.show()


