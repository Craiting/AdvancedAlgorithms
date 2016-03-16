#!/bin/sh
#SBATCH -N 1
#SBATCH --ntasks-per-node 24
#SBATCH --time 2-00:00:00
#SBATCH --job-name dna_first_go

python /home/A01055143/dna_project/dna_alignment/pair.py
