#!/bin/sh
from alignment import Hirschberg
import thread

def compare(filea, fileb, outputfile):
    human = open(filea)
    neandertal = open(fileb)

    h = human.readlines()
    hum = ''.join(h).replace('\n','').lower()

    n = neandertal.readlines()
    nea = ''.join(n).replace('\n','').lower()

    hirsch = Hirschberg()

    a,b = hirsch.align(hum, nea)
    final = hirsch.score(a,b, 'results/'+outputfile)
    # print 'final score: ', final
    print 'finished %s and %s' % (filea, fileb)

try:
   thread.start_new_thread( compare, ('human_neandertal/homosapian.txt', 'human_neandertal/Neandertal.txt','humanVneandertal.txt', ) )
   thread.start_new_thread( compare, ('diversity/aborigine.txt', 'diversity/algeria.txt','aborigineValgeria.txt', ) )
except:
   print "Error: unable to start thread"
