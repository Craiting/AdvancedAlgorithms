cache = {}
def Win(a, b, c):
    if (a,b,c) in cache:
        return cache[(a,b,c)]
    else:
        if (a == 0) and (b == 0) and (c == 0):
            return False
        for i in range(1,a+1):
            cache[(a-i, b, c)] = not Win(a-i, b, c) 
            return cache[(a-i,b,c)]
        for i in range(1,b+1):
            cache[(a, b-i, c)] = not Win(a, b-i, c) 
            return cache[(a,b-i,c)]
        for i in range(1,c+1):
            cache[(a, b, c-i)] = not Win(a, b, c-i) 
            return cache[(a,b,c-i)]
        return False

line = raw_input() # run, then hit 3 numbers and hit enter
x = int(line[0])
y = int(line[1])
z = int(line[2])

print Win(x,y,z)
#print cache
#print cache[(x,y,z)]

