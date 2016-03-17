from alignment import Needleman

seq_a = 'actg'*6
seq_b = 'ttga'*6
n = Needleman()
# To test what size makes the O(n^2) algorithm not work I loop through making the
# sequences bigger until it breaks. Then I calculate the size and estimate the
# bytes estimating one character to equal 4 bytes.
i = 0
while True:
    print i
    try:
        a,b = n.align(seq_a,seq_b)
        seq_a += 'tccaaccatcaatcga'*10
        seq_b += 'tcaaaacttctcaaga'*10
    except Exception as e:
        print 'Error %s' % e
        print 'length a',len(seq_a)
        print 'length b', len(seq_b)
        break
    i+=1

print 'bytes=%s', str(len(seq_a)+len(seq_b)*4)
# My computer froze when this program took about 2.183g and the sequence length
# was about 7000 characters for each sequence.
