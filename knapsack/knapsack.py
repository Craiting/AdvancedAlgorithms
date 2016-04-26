import random
import time
MILLI = 1000

cache = {}
def knap(objs, sac):
    if (len(objs),sac) in cache:
        return cache[(len(objs),sac)]
    if sac < 0:
        cache[(len(objs),sac)] = 99999999999999999999l
        return 99999999999999999999l
    if len(objs) == 0:
        cache[(0,sac)] = sac
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
for j in range(30):
    for i in range(3,13)[::-1]:
        p = create_point(i)
        points[i].append(p)
    print j

f = open('results.txt', 'w')
f.write(str(points))
print points
