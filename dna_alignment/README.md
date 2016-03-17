## DNA Analysis Lab

#### Results
I ran all my comparisons at once using the supercomputers which us students have
access to. The setup for running them is found in the compare.py, pair.py,
jobs/queuejobs.py and jobs/compare.sh files. The text files showing how the
scoring is done with the final score as the last line are all found in the
results directory. Tables are included at the same level as this file. In order
to approximate the size of the solution matrix where the O(n^2) algorithm becomes
impractical, I made a script in estimatingmax.py which uses the Needleman
algorithm and continually increases the size of sequence until the computer runs
out of memory and throws an exception.

#### Summary
The fast performance algorithm must be very exciting for the science community
because it means scientists can compare DNA sequences much faster than before.
The speed increase is very noticeable when comparing the difference between the
Needleman and Hirschberg algorithms. The Needleman being O(n^2) is noticeably
slower even when the sequences reach sizes of about 80 bytes. As the sequences
get longer and longer, the speed difference becomes more and more noticeable. The
Needleman algorithm reaches a point where it requires too much memory is required
to complete the alignment. The point where the Hirschberg algorithm maxes out the
memory is going to have way longer sequences.
