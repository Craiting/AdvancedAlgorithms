

class PolyMult:
    
    def simple(self,a, b):
        out = [0 for x in range(len(a)+len(b)-1)]
        for i in range(len(a)):
            for j in range(len(b)):
                out[i+j] = out[i+j] + a[i] * b[j]
        return out        

