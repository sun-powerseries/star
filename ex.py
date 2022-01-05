name = input('enter file:')
handle = open(name, 'r')

counts = dict()
for line = line.split()
for word in words:
counts[word] = counts.get(word,0) +1

bigcount = none
bigword = none
for word,count in counts.items():
if bigcount is non or count > bigcount:
bigword = word
bigcount = counts
print(bigword, bigcount)
