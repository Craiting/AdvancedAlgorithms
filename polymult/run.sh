#!/bin/sh
#SBATCH -N 1
#SBATCH --ntasks-per-node 24
#SBATCH --time 2-00:00:00
#SBATCH --job-name polynomial

python /home/A01055143/AdvancedAlgorithms/polymult/problems.py
