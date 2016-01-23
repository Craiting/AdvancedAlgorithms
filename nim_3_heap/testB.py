from random import randint
from nim3recursive import RecursiveAlgorithm
from nim3memo import MemoizeAlgorithm
from nim3dy import DynamicAlgorithm

mem = MemoizeAlgorithm()
dyn = DynamicAlgorithm()

for i in range(10000):
    a = randint(0,50)
    b = randint(0,50)
    c = randint(0,50)
    if mem.Win(a,b,c) == dyn.Win(a,b,c):
        pass
    else:
        print 'bad', (a,b,c)
    if i % 100 == 0:
        print i
