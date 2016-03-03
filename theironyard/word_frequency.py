# I kept getting this error --> ImportError: cannot import name 'counter'   from this line -->  from collections import counter
# I am trying to figure out how to use this line from collections import counter
import re

wordfreq = {}
with open('sample.txt') as f:
    for line in f:
        for word in re.findall(r'[\w]+', line.lower()):
            wordfreq[word] = wordfreq.setdefault(word, 0) + 1

print (wordfreq)