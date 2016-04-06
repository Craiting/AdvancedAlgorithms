# sudo apt-get install python-matplotlib
import matplotlib.pyplot as plt

x = [32,64,128,256,512,1024,2048,4096,8192] # n
simple_y = [0.000995063781,0.003899192,0.0156164169,0.06266417503,0.2544161319,1.013564538,4.08225603104,15.89235,63.260811758]
divide_y = [0.00259981,0.00797038,0.024173116,0.07366385,0.22179155,0.66378946,1.99465136,5.974885463,18.1825761318]
fft_y = [0.003559207,0.00794019699,0.017751789093,0.03924088478,0.085623216629,0.18574285507,0.4023638248,0.87264795303,1.8181104]
# slope simple is 1.99452
# slope divide and conquer is 1.596482

plt.loglog(x, simple_y, 'r', x , divide_y, 'g', basey=2, basex=2)
simple_line, = plt.plot(x, simple_y, label='Simple Algorithm')
divide_line, = plt.plot(x, divide_y, label='Divide and Conquer Algorithm')
fft_line, = plt.plot(x, fft_y, label="FFT Algorithm")
plt.xlabel('Problem size (log n)')
plt.ylabel('Time seconds (log s)')
plt.title('Polynomial Multiplication Algorithms')
plt.legend([simple_line,divide_line,fft_line],['Simple', 'Divide and Conquer', 'FFT'])
plt.show()
