
class MemoizeAlgorithm:
    def __init__(self):
        self.cache = {}

    def Win(self, a, b, c):
        if (a,b,c) in self.cache:
            return self.cache[(a,b,c)]
        else:
            if ((a>1)+(b>1)+(c>1)) == 1 :
                self.cache[(a,b,c)] = True
                return True
            if (a == 0) and (b == 0) and (c == 0):
                self.cache[(a,b,c)] = False
                return False
            for i in range(1,a+1):
                if not self.Win(a-i, b, c):
                    self.cache[(a,b,c)] = True
                    return self.cache[(a,b,c)]
            for i in range(1,b+1):
                if not self.Win(a, b-i, c):
                    self.cache[(a, b, c)] = True
                    return self.cache[(a, b, c)]
            for i in range(1,c+1):
                if not self.Win(a, b, c-i):
                    self.cache[(a, b, c)] = True
                    return self.cache[(a,b,c)]
            self.cache[(a,b,c)] = False
            return self.cache[(a,b,c)]
