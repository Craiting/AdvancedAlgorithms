from Poly import PolyMult

p = PolyMult()
a = [1,2]
b = [3,4]
h = p.divide_conquer(a,b)
s = p.simple([1,2,3],[3,2,1])
h = p.div_and_conc([1,2,3],[3,2,1])
print s
print h
s = p.simple([-.12,.53,.24,-.77],[.99,.43])
h = p.div_and_conc([-.12,.53,.24,-.77],[.99,.43])
print s
print h
s = p.simple([1,5,6],[3,2,1,2,5,7])
h = p.div_and_conc([1,5,6],[3,2,1,2,5,7])
print s
print h
