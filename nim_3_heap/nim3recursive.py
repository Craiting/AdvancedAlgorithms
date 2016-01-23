
class RecursiveAlgorithm:

    def Win(self, a, b, c):
        if (a == 0) and (b == 0 ) and (c == 0):
            return False
        for i in range(1,a+1):
            if not self.Win(a-i, b, c):
                return True
        for i in range(1,b+1):
            if not self.Win(a, b-i, c):
                return True
        for i in range(1,c+1):
            if not self.Win(a, b, c-i):
                return True
        return False
