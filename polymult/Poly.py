

class PolyMult:
    
    def simple(self,a, b):
        out = [0 for x in range(len(a)+len(b)-1)]
        for i in range(len(a)):
            for j in range(len(b)):
                out[i+j] = out[i+j] + a[i] * b[j]
        return out        

    def divide_conquer(self, p, q):
        if len(p) == len(q) == 1:
            return [p[0]*q[0]]

        mid = len(p)/2
        pl = p[:mid]
        ph = p[mid:]
        ql = q[:mid]
        qh = q[mid:]
        sol1 = divide_conquer(pl,ql)
        sol2 = divide_conquer(ph,qh)
        sol3 = divide_conquer(sum(pl,ph),sum(ql,qh))
        midsol = sol3 - sol1 - sol2
