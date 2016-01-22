
def Win(a, b, c):
    if (a == 0) and (b == 0 ) and (c == 0):
        return False
    for i in range(1,a+1):
        if not Win(a-i, b, c):
            return True
    for i in range(1,b+1):
        if not Win(a, b-i, c): 
            return True
    for i in range(1,c+1):
        if not Win(a, b, c-i):
            return True
    return False

line = raw_input() # run, then d  3 numbers and hit enter
x = int(line[0])
y = int(line[1])
z = int(line[2])

print Win(x,y,z)
