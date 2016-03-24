

class PolyMult:

    def simple(self,a, b):
        out = [0 for x in range(len(a)+len(b)-1)]
        for i in range(len(a)):
            for j in range(len(b)):
                out[i+j] = out[i+j] + a[i] * b[j]
        return out

    def div_and_conc(self, p, q):
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
            return [p[0]*q[0]]

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
        midsol += [0 for x in range(len(p)/2)]
        midsol.reverse()
        sol2.reverse()
        sol2 += [0 for x in range(2*mid)]
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
