cache = {}
def Win(a, b, c):
    if (a,b,c) in cache:
        return cache[(a,b,c)]
    else:
        if ((a>1)+(b>1)+(c>1)) == 1 :
            cache[(a,b,c)] = True
            return True
        if (a == 0) and (b == 0) and (c == 0):
            cache[(a,b,c)] = False
            return False
        for i in range(1,a+1):
            if not Win(a-i, b, c):
                cache[(a-i,b,c)] = True
                return cache[(a-i,b,c)]
        for i in range(1,b+1):
            if not Win(a, b-i, c):
                cache[(a, b-i, c)] = True
                return cache[(a, b-i, c)]
        for i in range(1,c+1):
            if not Win(a, b, c-i):
                cache[(a, b, c-i)] = True
                return cache[(a,b,c-i)]
        cache[(a,b,c)] = False
        return cache[(a,b,c)]

line = raw_input() # run, then hit 3 numbers and hit enter
x = int(line[0])
y = int(line[1])
z = int(line[2])

print Win(x,y,z)
#print cache
#print cache[(x,y,z)]
