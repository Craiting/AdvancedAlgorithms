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
        for i in range(a+1):
            for j in range(b+1):
                for k in range(c+1):
                    tmp = []
                    if ((a>1)+(b>1)+(c>1)) == 1 :
                        cache[(i,j,k)] = True
                    for p in range(i+1):
                        if (p,j,k) in cache:
                            tmp.append(not cache[(p,j,k)])
                    for p in range(j+1):
                        if (i,p,k) in cache:
                            tmp.append(not cache[(i, p, k)])
                    for p in range(k+1):
                        if (i,j,p) in cache:
                            tmp.append(not cache[(i, j, p)])
                    # print tmp, (i,j,k)
                    if (i,j,k) not in cache:
                        if True in tmp:
                            cache[(i,j,k)] = True
                        else:
                            cache[(i,j,k)] = False
        # print cache
        return cache[(a,b,c)]


line = raw_input()
line = str(line)
x = int(line[0])
y = int(line[1])
z = int(line[2])
print Win(x,y,z)
