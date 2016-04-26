import random

cache = {}
def knap(objs, sac):
    if sac < 0:
        return 99999
    if len(objs) == 0:
        return sac
    return min(knap(objs[1:], sac-objs[0]), # Do use
               knap(objs[1:], sac))       # Dont use

n = 22
k = 11.0000
objects = [random.uniform(0,1.0) for x in range(n)]
sol = knap(objects, k)
print sol
