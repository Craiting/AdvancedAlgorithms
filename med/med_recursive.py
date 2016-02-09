
from MED import MED

misfile = open('wordtest.txt')


record = {}
med = MED()
while True:
    try:
        words = map(str, misfile.next().replace('\n','').split('->'))
        if words:
            count = med.recursive(words[0],words[1], len(words[0]), len(words[1]))
            record[(words[0],words[1])] = count
    except:
        break

table = {}
for key, value in record.iteritems():
    if value in table:
        table[value] += 1
    else:
        table[value] = 1
print table

