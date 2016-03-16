#!/bin/sh
from alignment import Hirschberg
import thread

def compare(filea, fileb, outputfile):
    human = open('/home/A01055143/AdvancedAlgorithms/dna_alignment'+filea)
    neandertal = open('/home/A01055143/AdvancedAlgorithms/dna_alignment'+fileb)

    h = human.readlines()
    hum = ''.join(h).replace('\n','').lower()

    n = neandertal.readlines()
    nea = ''.join(n).replace('\n','').lower()

    hirsch = Hirschberg()

    a,b = hirsch.align(hum, nea)
    final = hirsch.score(a,b, '/home/A01055143/AdvancedAlgorithms/dna_alignment/results/'+outputfile)
    # print 'final score: ', final
    print 'finished %s and %s' % (filea, fileb)
