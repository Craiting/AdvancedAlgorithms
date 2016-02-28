

class dna_align:
 
    def __init__(self):
        self.sub = {
            ('c','t'):-3, ('g','t'):-1, ('a','t'):-3, ('t','c'):-3, ('t','g'):-1, ('t','a'):-3,
            ('c','g'):-3, ('g','c'):-3, ('g','c'):-3, ('c','a'):-1, ('a','c'):-1, ('a','g'):-3,
            ('a','a'): 5, ('c','c'): 5, ('g','g'): 5, ('t','t'): 5
        }
        self.ins = { 'a':-3, 'c':-4, 'g':-2, 't':-1 }
        self.dele = { 'a':-3, 'c':-4, 'g':-2, 't':-1 }

    def recursive(self, A, B):
        self.wordA = A
        self.wordB = B
        return self.rec_call(len(A), len(B))
    
    def rec_call(self, A, B):
        if A == 0:
            return B*-2
        if B == 0:
            return A*-2
        return max(self.rec_call(A-1,B)-2, self.rec_call(A,B-1)-2, self.rec_call(A-1, B-1) + self.sub[(self.wordA[A-1].lower(), self.wordB[B-1].lower())])


    def NWScore(self,X,Y):
        score = {}
        score[(0,0)] = 0
        for i in range(1,len(Y)):
            score[(0,i)] = score[(0, i-1)] + self.ins[(Y[i].lower())]
        for i in range(1,len(X)):
            score[(i,0)] = score[(i-1,0)] + self.dele[(X[i].lower())]
            for j in range(1,len(Y)):
                scoreSub = score[(i-1,j-1)] + self.sub[(X[i].lower(),Y[j].lower())]
                scoreDel = score[(i-1,j)] + self.dele[(X[i].lower())]
                scoreIns = score[(i,j-1)] + self.ins[(Y[j].lower())]
                score[(i,j)] = max(scoreSub, scoreDel, scoreIns)
        lastline = []
        for j in range(len(Y)):
            lastline[j] = score[(len(X),j)]
        print lastline
        return score
