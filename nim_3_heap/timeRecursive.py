from nim3recursive import RecursiveAlgorithm
import time

n_cases = [2,3,4,5,6,7,8,9] # It takes quite a long time for 9 to run
MILLI = 1000

rec = RecursiveAlgorithm() # times recursive algorithm run for each case (n)
for pile_size in n_cases:
    start = time.clock()
    rec.Win(pile_size,pile_size,pile_size)
    stop = time.clock()
    total_time_um = (stop - start) * MILLI
    print "n=%s  t=%s" % (pile_size, total_time_um)
