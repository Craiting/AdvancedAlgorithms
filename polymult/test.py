from Poly import PolyMult

p = PolyMult()
a = [1,2]
b = [3,4]
h = p.divide_conquer(a,b)
s = p.simple([1,2,3,4],[4,3,2,1])
h = p.div_and_conc([1,2,3,4],[4,3,2,1])
f = p.fft_mult([1,2,3,4],[4,3,2,1])
print '\n\n  FFT Tests\n+++++++++++++'
print 'simple', s
print 'divide', h
print 'FFT   ', f
s = p.simple([-.12,.53,.24,-.77],[.99,.43,-.34,.32])
h = p.div_and_conc([-.12,.53,.24,-.77],[.99,.43,-.34,.32])
f = p.fft_mult([-.12,.53,.24,-.77],[.99,.43,-.34,.32])
print 'simple', s
print 'divide', h
print 'FFT   ', f
s = p.simple([1,5,6,2.2,.11,.51,1,2],[3,2,1,2,5,7,1,2])
h = p.div_and_conc([1,5,6,2.2,.11,.51,1,2],[3,2,1,2,5,7,1,2])
f = p.fft_mult([1,5,6,2.2,.11,.51,1,2],[3,2,1,2,5,7,1,2])
print 'simple', s
print 'divide', h
print 'FFT   ', f
print '\n\n  Old Tests\n+++++++++++++'
s = p.simple([1,2,3],[3,2,1])
h = p.div_and_conc([1,2,3],[3,2,1])
print 'simple', s
print 'divide', h
s = p.simple([-.12,.53,.24,-.77],[.99,.43])
h = p.div_and_conc([-.12,.53,.24,-.77],[.99,.43])
print 'simple', s
print 'divide', h
s = p.simple([1,5,6],[3,2,1,2,5,7])
h = p.div_and_conc([1,5,6],[3,2,1,2,5,7])
print 'simple', s
print 'divide', h
