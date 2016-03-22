

class Polysolver:

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
