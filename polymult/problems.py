import random
import time

from Poly import PolyMult as Poly

def generate_random_poly(size):
    p = [0 for x in range(size)]
    q = [0 for x in range(size)]
    for i in range(size):
        p[i] = random.uniform(-1.0,1.0)
        q[i] = random.uniform(-1.0,1.0)
    return (p,q)

out = open('out.txt','w')
out.close()
poly = Poly()
n = 32
while n < 524288:
    try:
        simp = []
        div = []
        for i in range(5): # timing the same problem set 5 times then taking the average.
            p,q = generate_random_poly(n)
            # First time the simple algorithm
            start = time.time()
            ans = poly.simple(p,q)
            simp.append(time.time() - start)
            # Secondly time the divide and conquer algorithm
            start = time.time()
            ans = poly.div_and_conc(p,q)
            div.append(time.time() - start)
        out = open('out.txt','a')
        out.write('\n\nn = %s' % str(n))
        out.write('\nsimple = %f, %f, %f, %f, %f' % (simp[0],simp[1],simp[2],simp[3],simp[4]))
        out.write('\ndivide = %f, %f, %f, %f, %f' % (div[0],div[1],div[2],div[3],div[4]))
        out.close()
    except Exception as e:
        print 'Error', e
        break
    n *= 2
