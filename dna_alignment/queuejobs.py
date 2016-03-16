import os

# pairwise
L1 = os.listdir('/home/A01055143/dna_project/dna_alignment/diversity')
tuples = [(x,y) for x in L1 for y in L1 if x != y]
for entry in tuples:
    if (entry[1], entry[0]) in tuples:
        tuples.remove((entry[1],entry[0]))
for t in tuples:
    pair = open('pair.py', 'w')
    pair.write("from compare import compare\ncompare('/diversity/%s','/diversity/%s','%s')" % (t[0],t[1], t[0][:4]+'_'+t[1][:4]))
    pair.close()
    os.system('sbatch compare.sh')

os.system('squeue -u A01055143')
