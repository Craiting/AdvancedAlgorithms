cache = {}
def Win(a,b,c):
    cache[(0,0,0)] = False
    cache[(0,0,1)] = True
    cache[(0,1,0)] = True
    cache[(1,0,0)] = True
    cache[(1,1,0)] = False
    cache[(1,0,1)] = False
    cache[(0,1,1)] = False
    cache[(1,1,1)] = True
    cache[(0,2,2)] = False
    cache[(2,2,0)] = False
    cache[(2,0,2)] = False
    if(a,b,c) in cache:
        return cache[(a,b,c)]
    else:
        for i in range(1, a+1):
            for j in range(1, b+1):
                for k in range(1, c+1):
                    if ((i>1)+(j>1)+(k>1)) <= 1 :
                        cache[(i,j,k)] = True
                    tmp = []
                    for w in range(a+1):
                        if (w,j,k) in cache:
                            print 'first', (w,j,k), cache[(w,j,k)]
                            tmp.append(cache[(w,j,k)])
                    for e in range(b+1):
                        if (i,e,k) in cache:
                            print 'second', (i,e,k), cache[(i,e,k)]
                            tmp.append(cache[(i,e,k)])
                    for r in range(c+1):
                        if (i,j,r) in cache:
                            print 'third', (i,j,r), cache[(i,j,r)]
                            tmp.append(cache[(i,j,r)])
                    print (i,j,k), tmp
                    if False in tmp:
                        cache[(i,j,k)] = True
                    else:
                        cache[(i,j,k)] = False
        return cache[(a,b,c)]


line = raw_input()
line = str(line)
x = int(line[0])
y = int(line[1])
z = int(line[2])
print Win(x,y,z)
