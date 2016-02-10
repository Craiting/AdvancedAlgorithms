from nim3memo import MemoizeAlgorithm
from nim3dy import DynamicAlgorithm
import time

n_cases = [2,4,8,16,32,64]
MILLI = 1000

print '\nMEMOIZE' # All the results for the Memoize algorithm will appear below
for pile_size in n_cases:
    mem = MemoizeAlgorithm()
    start = time.clock()
    mem.Win(pile_size,pile_size,pile_size)
    stop = time.clock()
    total_time_um = (stop - start) * MILLI
    print "n=%s  t=%s" % (pile_size, total_time_um)


print '\nDYNAMIC' # All the results for the Dynamic algorithm will appear below
for pile_size in n_cases:
    dyn = DynamicAlgorithm()
    start = time.clock()
    dyn.Win(pile_size,pile_size,pile_size)
    stop = time.clock()
    total_time_um = (stop - start) * MILLI
    print "n=%s  t=%s" % (pile_size, total_time_um)
