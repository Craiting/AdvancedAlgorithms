# sudo apt-get install python-matplotlib
import matplotlib.pyplot as plt

x = [] # n
simple_y = []
divide_y = []

plt.loglog(x, simple_y, 'r', x , divide_y, 'g', basey=2, basex=2)
simple_line, = plt.plot(x, simple_y, label='Simple Algorithm')
divide_line, = plt.plot(x, divide_y, label='Divide and Conquer Algorithm')
plt.xlabel('Problem size (log n)')
plt.ylabel('Time (log s)')
plt.title('Polynomial Multiplication Algorithms')
plt.legend([simple_line,divide_line],['Simple', 'Divide and Conquer'])
plt.show()
