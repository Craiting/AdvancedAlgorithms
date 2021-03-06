import random
import time
import numpy
import math
MILLI = 1000
def knapsack(o,s):
    cache = {}
    def knap(objs, sac):
        if (len(objs),sac) in cache and len(objs) != 22:
            return cache[(len(objs),sac)]
        if sac < 0:
            return 99999999999999999999l
        if len(objs) == 0:
            return sac
        cache[(len(objs),sac)] = min(knap(objs[1:], sac-objs[0]), # Do use
                                     knap(objs[1:], sac))       # Dont use
        return cache[(len(objs),sac)]
    return knap(o,s)

def create_point(m):
    print m
    n = 22
    k = 11.0000
    objects = [int(math.floor(float(round(random.uniform(0,1.0),m))*10**m)) for x in range(n)]
    start = time.clock()
    sol = knapsack(objects, k*10**m)
    sol = knapsack(objects, k*10**m)
    sol = knapsack(objects, k*10**m)
    sol = knapsack(objects, k*10**m)
    sol = knapsack(objects, k*10**m)
    sol = knapsack(objects, k*10**m)
    sol = knapsack(objects, k*10**m)
    stop = time.clock()
    totaltime_ms = (stop - start)
    return (totaltime_ms, float(sol)/(10**m))

print 'it begins'
points = {11:[],10:[],9:[],8:[],7:[],6:[],5:[],4:[],3:[]}
# p = create_point(12)
# print p
for j in range(30):
    for i in range(3,12)[::-1]:
        p = create_point(i)
        points[i].append(p)
    # print j

f = open('work.txt', 'w')
#real_answer = float(numpy.mean([x[1] for x in points[12]]))
r = create_point(12)
real_answer = r[1]
for key in points:
    f = open('work.txt','a')
    f.write('m = %d\n' % key)
    for point in points[key]:
        f.write('(%f, %f)\n' % (point[0],abs(real_answer - point[1])))
    # avg_time = float(numpy.mean([x[0] for x in points[key]]))
    # avg_num = float(numpy.mean([x[1] for x in points[key]]))
    # error = abs(real_answer - avg_num)
    # f.write("m = %d (%f, %f)\n" % (key, avg_time, error))
    f.close()
