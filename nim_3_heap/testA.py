from random import randint
from nim3recursive import RecursiveAlgorithm
from nim3memo import MemoizeAlgorithm
from nim3dy import DynamicAlgorithm

rec = RecursiveAlgorithm()
mem = MemoizeAlgorithm()
dyn = DynamicAlgorithm()

for i in range(10000):
    a = randint(0,5)
    b = randint(0,5)
    c = randint(0,5)
    if rec.Win(a,b,c) == mem.Win(a,b,c) == dyn.Win(a,b,c):
        pass
    else:
        print 'bad', (a,b,c)
    if i % 100 == 0:
        print i

print 'Done'
