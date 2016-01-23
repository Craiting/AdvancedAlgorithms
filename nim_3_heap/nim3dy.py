
class DynamicAlgorithm:
    def __init__(self):
        self.cache = {}
        self.cache[(0,0,0)] = False
        self.cache[(0,0,1)] = True
        self.cache[(0,1,0)] = True
        self.cache[(1,0,0)] = True
        self.cache[(1,1,0)] = False
        self.cache[(1,0,1)] = False
        self.cache[(0,1,1)] = False
        self.cache[(1,1,1)] = True
        self.cache[(0,2,2)] = False
        self.cache[(2,2,0)] = False
        self.cache[(2,0,2)] = False

    def Win(self,a,b,c):
        if(a,b,c) in self.cache:
            return self.cache[(a,b,c)]
        else:
            for i in range(a+1):
                for j in range(b+1):
                    for k in range(c+1):
                        tmp = []
                        if ((i>1)+(j>1)+(k>1)) <= 1 :
                            tmp.append(True)
                        for p in range(i+1):
                            if (p,j,k) in self.cache:
                                tmp.append(not self.cache[(p,j,k)])
                        for p in range(j+1):
                            if (i,p,k) in self.cache:
                                tmp.append(not self.cache[(i, p, k)])
                        for p in range(k+1):
                            if (i,j,p) in self.cache:
                                tmp.append(not self.cache[(i, j, p)])
                        if (i,j,k) not in self.cache:
                            if True in tmp:
                                self.cache[(i,j,k)] = True
                            else:
                                self.cache[(i,j,k)] = False
            return self.cache[(a,b,c)]
