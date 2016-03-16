import os

# human vs neandertal
# pair = open('/home/A01055143/AdvancedAlgorithms/dna_alignment/pair.py', 'w')
# pair.write("from compare import compare\ncompare('/human_neandertal/%s','/human_neandertal/%s','%s')" % ('homosapian.txt','Neandertal.txt', 'human_neandertal'))
# pair.close()
# os.system('sbatch compare.sh')


# pairwise
# L1 = os.listdir('/home/A01055143/AdvancedAlgorithms/dna_alignment/diversity')
# tuples = [(x,y) for x in L1 for y in L1 if x != y]
# for entry in tuples:
#     if (entry[1], entry[0]) in tuples:
#         tuples.remove((entry[1],entry[0]))
# for t in tuples:
#     pair = open('/home/A01055143/AdvancedAlgorithms/dna_alignment/pair.py', 'w')
#     pair.write("from compare import compare\ncompare('/diversity/%s','/diversity/%s','%s')" % (t[0],t[1], t[0][:4]+'_'+t[1][:4]))
#     pair.close()
#     os.system('sbatch compare.sh')

# human vs apes
ape_list = os.listdir('/home/A01055143/AdvancedAlgorithms/dna_alignment/great_apes')
for ape in ape_list:
    pair = open('/home/A01055143/AdvancedAlgorithms/dna_alignment/pair.py', 'w')
    pair.write("from compare import compare\ncompare('/human_neandertal/%s','/great_apes/%s','%s')" % ('homosapian.txt',ape, 'human_'+ape[:-4]))
    pair.close()
    os.system('sbatch compare.sh')

os.system('squeue -u A01055143')
