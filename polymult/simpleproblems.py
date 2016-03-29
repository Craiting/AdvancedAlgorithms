import random
import time
import numpy

from Poly import PolyMult as Poly

def generate_random_poly(size):
    p = [0 for x in range(size)]
    q = [0 for x in range(size)]
    for i in range(size):
        p[i] = random.uniform(-1.0,1.0)
        q[i] = random.uniform(-1.0,1.0)
    return (p,q)

out = open('outsimp.txt','w')
out.close()
poly = Poly()
n = 32
while n < 80000:
    try:
        simp = []
        div = []
        for i in range(5):
            p,q = generate_random_poly(n)
            # First time the simple algorithm
            start = time.time()
            ans = poly.simple(p,q)
            simp.append(time.time() - start)
        out = open('outsimp.txt','a')
        out.write('\n\nn = %s' % str(n))
        out.write('\nsimple = %s' % (str(numpy.mean(simp))))
        out.close()
    except Exception as e:
        print 'Error', e
        break
    n *= 2
