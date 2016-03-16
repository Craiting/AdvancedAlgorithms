import unittest
from alignment import Needleman, Hirschberg

class TestAlgorithms(unittest.TestCase):
    def setUp(self):
        self.n = Needleman()
        self.h = Hirschberg()

    def test1(self):
        seqa = 'atcggggaat'
        seqb = 'ttgcaac'
        a,b = self.n.align(seqa,seqb)
        x,y = self.h.align(seqa,seqb)
        nscore = self.n.score(a,b,'t.txt')
        hscore = self.h.score(a,b,'t.txt')
        # compare the needleman score to the Hirschberg score
        self.assertEqual(nscore, hscore)

    def test2(self):
        seqa = 'atcggggaattgttacgtaaact'
        seqb = 'ttgcaacccttgaagagag'
        a,b = self.n.align(seqa,seqb)
        x,y = self.h.align(seqa,seqb)
        nscore = self.n.score(a,b,'t.txt')
        hscore = self.h.score(a,b,'t.txt')
        # compare the needleman score to the Hirschberg score
        self.assertEqual(nscore, hscore)

    def test3(self):
        seqa = 'atcggggaactccttgaatccactttgcaattgcaattgcagtaa'
        seqb = 'ttgccggcgttgcaagacccagtacttgcaa'
        a,b = self.n.align(seqa,seqb)
        x,y = self.h.align(seqa,seqb)
        nscore = self.n.score(a,b,'t.txt')
        hscore = self.h.score(a,b,'t.txt')
        # compare the needleman score to the Hirschberg score
        self.assertEqual(nscore, hscore)

    def test4(self):
        seqa = 'atcgggaactccttgaatccactttgggaagacccagtacttggaaggaactccttgaatccactttgt'
        seqb = 'ttgaagacccagtacttgcaagacccaagacccagtacttgagtacttgaagacccagtacttgaagacccagtacttgaac'
        a,b = self.n.align(seqa,seqb)
        x,y = self.h.align(seqa,seqb)
        nscore = self.n.score(a,b,'t.txt')
        hscore = self.h.score(a,b,'t.txt')
        # compare the needleman score to the Hirschberg score
        self.assertEqual(nscore, hscore)

    def test5(self):
        seqa = 'atcgtgcaagacccagaat'
        seqb = 'ttgcaatgcaagacccatgcaagacccatgcaagacttgattgattgtacttgagtacttgaagacccagtgtacttgagtacttgaagacccagtgaccac'
        a,b = self.n.align(seqa,seqb)
        x,y = self.h.align(seqa,seqb)
        nscore = self.n.score(a,b,'t.txt')
        hscore = self.h.score(a,b,'t.txt')
        # compare the needleman score to the Hirschberg score
        self.assertEqual(nscore, hscore)

    def test5(self):
        seqa = 'atcgtgcaacccatgcaagacccatgcaagacttgattgacccatgcaagacccatgtacttgcaatgcaagacccatgcaagacccatgcaagactttgcaatgcaagacccatgcaagacccatgcaagacgcaatgcaagacccatgcaagacccatgcaagacgagtacttggtacttgaagacccagtgtacttgagtacttgaagtacttgaagacccagtgtacttgagtacttgaagtacttgaagacccagtgtacttgagtacttgaagtacttgaagacccagtgtacttgagtacttgaagtacttgaagacccagtgtacttgagtacttgaagtacttgaagacccagtgtacttgagtacttgaagtacttgaagacccagtgtacttgagtacttgaagtacttgaagacccagtgtacttgagtacttgaagtacttgaagacccagtgtacttgagtacttgaagtacttgaagacccagtgtacttgagtacttgaaagtacttgagtacttgagaaagtacttgagtactgtacttgaggaat'
        seqb = 'ttgcaatgcaagacccatgcaagacccatgcaagacttgcaatgcaagacccatgtgctgcaattgcaatgcaagacccatgcaagacccatgcaagacgcaagacccatgcaagacccatgcaagacaatgcaagacccatgcaagacccatgcaagactgcaatgcaagacccatgcaagacccatgcaagactgcaatgcaagactgcaatgcaagatgcaatgcaagacccatgcaagacccatgcaagaccccatgcatgcaatgcaagacccatgcaagacccatgcaagacagacccatgcaagacccatgcatgcaatgcaagacccatgcaagacccatgcaagacagacccatgcaagaccaagacccatgcaagactgattgattgtatgcaatgcaagacccatgcaagacccatgcaagactgcaatgcaagacccatgcaagacccatgcaagaccttgagtacttgaagacccagtgtacttgagtacttgacttgagtacttgaagaagacttgagtacttgaagacccagcttgaagacctgaccac'
        a,b = self.n.align(seqa,seqb)
        x,y = self.h.align(seqa,seqb)
        nscore = self.n.score(a,b,'t.txt')
        hscore = self.h.score(a,b,'t.txt')
        # compare the needleman score to the Hirschberg score
        self.assertEqual(nscore, hscore)


if __name__ == '__main__':
    unittest.main()
