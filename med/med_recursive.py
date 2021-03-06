# This file runs the recursive algorithm and prints a table
from MED import MED

misfile = open('misspells.txt')
# misfile = open('wordtest.txt')

record = {}
med = MED() # instantiate MED object
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
            if count == 11:
                print "Maximal edit distance %s -> %s" % (words[0],words[1])

    except:
        break

table = {}
for key, value in record.iteritems():
    if value in table:
        table[value] += 1
    else:
        table[value] = 1

# Prints out a nice table
print " Edit dist |   Count"
for key, value in table.iteritems():
    if len(str(key)) == 1:
        print "     %s     |    %s" % (key, value)
    elif len(str(key)) == 2:
        print "     %s    |    %s" % (key, value)
    else:
        print "     %s    |    %s" % (key, value)
