import random
import time
import numpy
MILLI = 1000

cache = {}
def knap(objs, sac):
    if (len(objs),sac) in cache:
        return cache[(len(objs),sac)]
    if sac < 0:
        return 99999999999999999999l
    if len(objs) == 0:
        return sac
    cache[(len(objs),sac)] = min(knap(objs[1:], sac-objs[0]), # Do use
               knap(objs[1:], sac))       # Dont use
    return cache[(len(objs),sac)]

def create_point(m):
    n = 22
    k = 11.0000
    objects = [int(float(str(random.uniform(0,1.0))[:m])*10**m) for x in range(n)]
    start = time.clock()
    sol = knap(objects, k*10**m)
    stop = time.clock()
    totaltime_ms = (stop - start) * MILLI
    return (totaltime_ms, float(sol)/(10**m))

points = {12:[],11:[],10:[],9:[],8:[],7:[],6:[],5:[],4:[],3:[]}
# p = create_point(12)
# print p
for j in range(30):
   for i in range(3,13)[::-1]:
       p = create_point(i)
       points[i].append(p)
   print j

f = open('results2.txt', 'w')
real_answer = float(numpy.mean([x[1] for x in points[12]]))
for key in points:
    f = open('results.txt','a')
    f.write('m = %d\n' % key)
    for point in points[key]:
        f.write('(%f, %f)\n' % (point[0],abs(real_answer - point[1])))
    # avg_time = float(numpy.mean([x[0] for x in points[key]]))
    # avg_num = float(numpy.mean([x[1] for x in points[key]]))
    # error = abs(real_answer - avg_num)
    # f.write("m = %d (%f, %f)\n" % (key, avg_time, error))
    f.close()
