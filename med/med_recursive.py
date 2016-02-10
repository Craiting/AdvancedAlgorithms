
from MED import MED

misfile = open('wordtest.txt')


record = {}
med = MED()
while True:
    try:
        words = map(str, misfile.next().replace('\n','').split('->'))
        if words:
            if ',' in words[1]:
                new_words = words[1].split(',')
                count = med.recursive(words[0],new_words[1], len(words[0]), len(new_words[1]))
                record[(words[0],new_words[1])] = count
                count = med.recursive(new_words[0],new_words[1], len(new_words[0]), len(new_words[1]))
                record[(new_words[0],new_words[1])] = count
            else:
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

print "# Changes  |   Count"
for key, value in table.iteritems():
    print "     %s     |    %s" % (key, value)
