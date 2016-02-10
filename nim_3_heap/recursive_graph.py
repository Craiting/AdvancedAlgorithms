# sudo apt-get install python-matplotlib
import matplotlib.pyplot as plt

x = [2,3,4,5,6,7,8,9] # n, given by assignment
# these values were collected from data after running timeRecursive.py
y = [.053, .558, 6.387,72.566,956.729, 13844.630, 220196.644, 3211495.823] # time in milliseconds

plt.semilogy(x,y, basey=2) # y axis is log 2
plt.xlabel('Input (n)')
plt.ylabel('Time (log ms)')
plt.title('Recursive Nim Algorithm')
plt.show() # Shows the graph for the recursive empirical study
