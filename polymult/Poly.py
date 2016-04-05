import cmath

class PolyMult:

    def fft(self, P):
        n = len(P)
        if n == 1:
            return P
        else:
            if n%2 > 0:
                n+=1
                P += [0]
            Peven = self.fft([P[i] for i in xrange(0, n, 2)])
            Podd = self.fft([P[i] for i in xrange(1, n, 2)])
            combined = [0] * n
            for m in xrange(n/2):
                combined[m] = Peven[m] + self.omega(n, -m) * Podd[m]
                combined[m+n/2] = Peven[m] - self.omega(n, -m) * Podd[m]
            return combined
        # Podd = [0j for x in range(n/2)]
        # Peven = [0j for x in range(n/2)]
        # for i in range((n/2)-1):
        #     Peven[i] = P[2*i]
        #     Podd[i] = P[2*i+1]
        # soleven = FFT(Peven, ,n/2)
        # solodd = FFT(Podd, ,n/2)
        # sol = [0j for x in range(n/2)]
        # for j in range((n/2)-1):
        #     sol[j] =

    def omega(self, p, q):
        return cmath.exp((2.0* cmath.pi * 1j * q) / p)

    def ifft(self, P):
        timesig = self.fft([x.conjugate() for x in P])
        return [x.conjugate()/len(P) for x in timesig]


    def simple(self,a, b):
        out = [0 for x in range(len(a)+len(b)-1)]
        for i in range(len(a)):
            for j in range(len(b)):
                out[i+j] = float(out[i+j]) + float(a[i]) * float(b[j])
        return out

    def div_and_conc(self, p, q): # wrapper to account for poly size difference
        if len(p) > len(q):
            q += [0 for x in range(len(p)-len(q))]
        elif len(q) > len(p):
            p += [0 for x in range(len(q)-len(p))]
        temp = self.divide_conquer(p,q)
        while True:
            if temp[-1] == 0:
                temp.pop()
            else:
                return temp

    def divide_conquer(self, p, q):
        if len(p) == len(q) == 1:
            return [float(p[0]*q[0])]

        mid = len(p)/2
        pl = p[:mid]
        ph = p[mid:]
        ql = q[:mid]
        qh = q[mid:]
        sol1 = self.divide_conquer(list(pl),list(ql))
        sol2 = self.divide_conquer(list(ph),list(qh))
        sol3 = self.divide_conquer(self.add_poly(list(pl),list(ph)),self.add_poly(list(ql),list(qh)))
        midsol = self.sub_poly(self.sub_poly(list(sol3), list(sol1)), list(sol2))
        midsol.reverse()
        midsol += [0.0 for x in range(len(p)/2)]
        midsol.reverse()
        sol2.reverse()
        sol2 += [0.0 for x in range(2*mid)]
        sol2.reverse()
        return self.add_poly(self.add_poly(sol1 ,midsol), sol2)

    def add_poly(self, a, b):
        tempa = a
        tempb = b
        if len(tempa) <= len(tempb):
            for i in range(len(tempa)):
                tempb[i] = tempb[i] + tempa[i]
            return tempb
        else:
            for i in range(len(tempb)):
                tempa[i] = tempa[i] + tempb[i]
            return tempa

    def sub_poly(self, a, b):
        tempa = a
        tempb = b
        if len(tempa) <= len(tempb):
            for i in range(len(tempa)):
                tempb[i] = tempa[i] - tempb[i]
            return tempb
        else:
            for i in range(len(tempb)):
                tempa[i] = tempa[i] - tempb[i]
            return tempa
