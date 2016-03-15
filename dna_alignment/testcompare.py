from alignment import Hirschberg

human = open('human_neandertal/homosapian.txt')
neandertal = open('human_neandertal/Neandertal.txt')

h = human.readlines()
hum = ''.join(h[:2]).replace('\n','').lower()

n = neandertal.readlines()
nea = ''.join(n[:2]).replace('\n','').lower()

hirsch = Hirschberg()

a,b = hirsch.align(hum, nea)
final = hirsch.score(a,b, 'results/test.txt')
# print 'final score: ', final
print 'finished %s and %s' % ('hey', 'yo')
