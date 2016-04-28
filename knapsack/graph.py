import numpy as np
import matplotlib.pyplot as plt


N = 50
# x = np.random.rand(N)
# y = np.random.rand(N)
x = []
y = []
colors = np.random.rand(N)
try:
    for i in range(300):
        a,b = map(float, raw_input().split())
        x.append(a)
        y.append(b)
except:
    pass
# plt.loglog(x, y, basey=2, basex=2)

# plt.scatter(x, y, s=10, c=colors, alpha=.5)
# # plt.plot(x, y, c=colors, alpha=.5)
# plt.set_yscale('log')
# plt.set_xscale('log')
fig = plt.figure()
ax = plt.gca()
ax.scatter(x, y, s=10, c=colors, alpha=.5)
ax.set_yscale('log')
ax.set_xscale('log')

plt.title('Time vs Accuracy Knapsack Algorithm')
plt.xlabel('Algorithm Runtime (log ms)')
plt.ylabel('Algorithm Error')
plt.show()
