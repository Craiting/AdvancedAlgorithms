# This file contains the class with recursive and dynamic algorithm declarations
# Got help with this online. I tried to solve it on my own but used what I found
# online as a reference. The internet eased the pain a lot but I still feel like
# I learned from this assignment.


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
        cache = [[0 for x in range(n+1)] for x in range(m+1)]
        # fills in cache from bottom up
        for i in range(m+1):
            for j in range(n+1):
                if i == 0:
                    cache[i][j] = j
                elif j == 0:
                    cache[i][j] = i
                elif a[i-1] == b[j-1]:  # if last letter is the same then it moves on to the next letter
                    cache[i][j] = cache[i-1][j-1]
                else:
                    cache[i][j] = 1 + min(
                        cache[i-1][j],
                        cache[i][j-1],
                        cache[i-1][j-1]
                    )
        return cache[m][n]
