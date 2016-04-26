import random

def knap(objs, sac):
    if sac > k:
        return 99999
    if len(objs) == 0:
        return sac
    return min(knap(objs[1:], sac+obj[0]) # Do use
               knap(objs[1:], sac))       # Dont use

n = 22
k = 11.0000

