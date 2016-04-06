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

out = open('outfft.txt','w')
out.close()
poly = Poly()
n = 32
while n < 42768:
    try:
        simp = []
        div = []
        for i in range(5):
            p,q = generate_random_poly(n)
            # time the divide and conquer algorithm
            start = time.time()
            ans = poly.fft_mult(p,q)
            div.append(time.time() - start)
        out = open('outfft.txt','a')
        out.write('\n\nn = %s' % str(n))
        out.write('\ndivide = %s' % (numpy.mean(div)))
        out.close()
    except Exception as e:
        print 'Error', e
        break
    n *= 2
