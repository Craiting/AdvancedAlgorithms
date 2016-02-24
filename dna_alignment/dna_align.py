

class dna_align:
 
    def __init__(self):
        self.match = {
            ('c','t'):-3, ('g','t'):-1, ('a','t'):-3, ('t','c'):-3, ('t','g'):-1, ('t','a'):-3,
            ('c','g'):-3, ('g','c'):-3, ('g','c'):-3, ('c','a'):-1, ('a','c'):-1, ('a','g'):-3
        }

    def recursive(self, A, B):
        self.wordA = A
        self.wordB = B
        return self.rec_call(len(A), len(B))
    
    def rec_call(self, A, B):
        if A == 0:
            return B*-2
        if B == 0:
            return A*-2
        return max(self.rec_call(A-1,B)-2, self.rec_call(A,B-1)-2, self.rec_call(A-1, B-1) + self.match[(self.wordA[-1].lower(), self.wordB[-1].lower())])

