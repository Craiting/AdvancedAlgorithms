

class MED:

    def recursive(self, a, b, m, n):
        if m==0:
            return n
        if n==0:
            return m
        if a[m-1]==b[n-1]:
            return self.recursive(a,b,m-1,n-1)
        return 1 + min(self.recursive(a, b, m, n-1), # Insert
                       self.recursive(a, b, m-1, n), # Remove
                       self.recursive(a, b, m-1, n-1)) # Replace

    def dynamic(self, a, b, m, n):
        pass
