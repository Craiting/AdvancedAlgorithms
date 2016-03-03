# -*- coding: utf-8 -*-
# credit to leebird for the algorithm
# leebird's work has been heavily modified by me to fit the purpose of this assignment.

class Alignment(object):

    def __init__(self):
        self.seq_a = None
        self.seq_b = None
        self.len_a = None
        self.len_b = None
        self.substitute = {
            ('c','t'):-2, ('g','t'):-2, ('a','t'):-1, ('t','c'):-2, ('t','g'):-2,
            ('t','a'):-1, ('c','g'):-3, ('g','c'):-3, ('g','c'):-3, ('c','a'):-1,
            ('a','c'):-1, ('a','g'):-2, ('a','a'): 5, ('c','c'): 5, ('g','g'): 5,
            ('t','t'): 5, ('g','a'):-2
        }
        self.score_ins_del = { 'a':-3, 'c':-4, 'g':-2, 't':-1 }
        self.separator = u'|'

    def match(self, a, b):
        return self.substitute[(a,b)]

    def insert_delete(self, a):
        return self.score_ins_del[a] * len(a)

    def score(self, aligned_seq_a, aligned_seq_b):
        score = 0
        for a, b in zip(aligned_seq_a, aligned_seq_b):
            if a == b:
                print a, b, 5
                score += 5
            else:
                if a == self.separator:
                    print a, b, self.score_ins_del[b]
                    score += self.score_ins_del[b]
                elif b == self.separator:
                    print a, b, self.score_ins_del[a]
                    score += self.score_ins_del[a]
                else:
                    print a, b, self.match(a,b)
                    score += self.match(a,b)
        return score


class Needleman(Alignment):
    def __init__(self, *args):
        super(Needleman, self).__init__()
        self.matrix = None

    def init_matrix(self):
        rows = self.len_a + 1
        cols = self.len_b + 1
        self.matrix = [[0] * cols for i in range(rows)]

    def align(self, seq_a, seq_b):
        self.seq_a = seq_a
        self.seq_b = seq_b
        self.len_a = len(self.seq_a)
        self.len_b = len(self.seq_b)
        self.init_matrix()
        self.compute_matrix()
        return self.backtrack()

    def compute_matrix(self):
        seq_a = self.seq_a
        seq_b = self.seq_b
        len_a = self.len_a
        len_b = self.len_b

        for i in range(1, len_a + 1):
            self.matrix[i][0] = self.insert_delete(seq_a[i - 1]) + self.matrix[i - 1][0]
        for i in range(1, len_b + 1):
            self.matrix[0][i] = self.insert_delete(seq_b[i - 1]) + self.matrix[0][i - 1]

        for i in range(1, len_a + 1):
            for j in range(1, len_b + 1):
                score_sub = self.matrix[i - 1][j - 1] + self.match(seq_a[i - 1], seq_b[j - 1])
                score_del = self.matrix[i - 1][j] + self.insert_delete(seq_a[i - 1])
                score_ins = self.matrix[i][j - 1] + self.insert_delete(seq_b[j - 1])
                self.matrix[i][j] = max(score_sub, score_del, score_ins)

    def backtrack(self):
        aligned_seq_a, aligned_seq_b = [], []
        seq_a, seq_b = self.seq_a, self.seq_b
        i, j = self.len_a, self.len_b
        mat = self.matrix
        while i > 0 or j > 0:

            if j > 0 and mat[i][j] == mat[i][j - 1] + self.insert_delete(seq_b[j - 1]):
                aligned_seq_a.insert(0, self.separator * len(seq_b[j - 1]))
                aligned_seq_b.insert(0, seq_b[j - 1])
                j -= 1

            elif i > 0 and mat[i][j] == mat[i - 1][j] + self.insert_delete(seq_a[i - 1]):
                aligned_seq_a.insert(0, seq_a[i - 1])
                aligned_seq_b.insert(0, self.separator * len(seq_a[i - 1]))
                i -= 1

            elif i > 0 and j > 0 and mat[i][j] == mat[i - 1][j - 1] + self.match(seq_a[i - 1], seq_b[j - 1]):
                aligned_seq_a.insert(0, seq_a[i - 1])
                aligned_seq_b.insert(0, seq_b[j - 1])
                i -= 1
                j -= 1

            else:
                print(seq_a)
                print(seq_b)
                print(aligned_seq_a)
                print(aligned_seq_b)
                # print(mat)
                raise Exception('backtrack error', i, j, seq_a[i - 2:i + 1], seq_b[j - 2:j + 1])
                pass

        return aligned_seq_a, aligned_seq_b




class Hirschberg(Alignment):
    def __init__(self):
        super(Hirschberg, self).__init__()
        self.needleman = Needleman()

    def last_row(self, seqa, seqb):
        lena = len(seqa)
        lenb = len(seqb)
        pre_row = [0] * (lenb + 1)
        cur_row = [0] * (lenb + 1)

        for j in range(1, lenb + 1):
            pre_row[j] = pre_row[j - 1] + self.insert_delete(seqb[j - 1])

        for i in range(1, lena + 1):
            cur_row[0] = self.insert_delete(seqa[i - 1]) + pre_row[0]
            for j in range(1, lenb + 1):
                score_sub = pre_row[j - 1] + self.match(seqa[i - 1], seqb[j - 1])
                score_del = pre_row[j] + self.insert_delete(seqa[i - 1])
                score_ins = cur_row[j - 1] + self.insert_delete(seqb[j - 1])
                cur_row[j] = max(score_sub, score_del, score_ins)

            pre_row = cur_row
            cur_row = [0] * (lenb + 1)

        return pre_row

    def align_rec(self, seq_a, seq_b):
        aligned_a, aligned_b = [], []
        len_a, len_b = len(seq_a), len(seq_b)

        if len_a == 0:
            for i in range(len_b):
                aligned_a.append(self.separator * len(seq_b[i]))
                aligned_b.append(seq_b[i])
        elif len_b == 0:
            for i in range(len_a):
                aligned_a.append(seq_a[i])
                aligned_b.append(self.separator * len(seq_a[i]))

        elif len(seq_a) == 1:
            aligned_a, aligned_b = self.needleman.align(seq_a, seq_b)

        else:
            mid_a = int(len_a / 2)

            rowleft = self.last_row(seq_a[:mid_a], seq_b)
            rowright = self.last_row(seq_a[mid_a:][::-1], seq_b[::-1])

            rowright.reverse()

            row = [l + r for l, r in zip(rowleft, rowright)]
            maxidx, maxval = max(enumerate(row), key=lambda a: a[1])

            mid_b = maxidx

            aligned_a_left, aligned_b_left = self.align_rec(seq_a[:mid_a], seq_b[:mid_b])
            aligned_a_right, aligned_b_right = self.align_rec(seq_a[mid_a:], seq_b[mid_b:])
            aligned_a = aligned_a_left + aligned_a_right
            aligned_b = aligned_b_left + aligned_b_right

        return aligned_a, aligned_b

    def align(self, seq_a, seq_b, mode=None):
        self.seq_a = seq_a
        self.seq_b = seq_b
        self.len_a = len(self.seq_a)
        self.len_b = len(self.seq_b)
        return self.align_rec(self.seq_a, self.seq_b)
