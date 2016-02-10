# sudo apt-get install python-matplotlib
import matplotlib.pyplot as plt

x = [2,4,8,16,32,64]  # n, given by assignment
# these values were collected from data after running timeMemDyn.py
# time in milliseconds
mem_y = [0.02,.065,.327,2.132,14.081,94.886]
dyn_y = [.157,.857,7.514,88.018,1183.548,18953.987]

plt.loglog(x,mem_y, 'r', x, dyn_y, 'g', basey=2, basex=2)
mem_line, = plt.plot(x, mem_y,label='memoize')
dyn_line, = plt.plot(x, dyn_y,label='dynamic')
plt.xlabel('Input (log n)')
plt.ylabel('Time (log ms)')
plt.title('Memoize and Dynamic Nim Algorithm')
plt.legend([mem_line,dyn_line], ['Memoize','Dynamic'])
plt.show()
