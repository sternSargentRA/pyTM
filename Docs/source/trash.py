import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc


N = 5
x = np.arange(N)
y = x**2 - 2*x + 4

fig = plt.figure()
ax = fig.add_subplot(111)
rects1 = ax.bar(x[1:], y[1:], width=1.0, color='none')
rects1 = ax.bar(x[0], y[0], width=1.0, color='grey')

# add some
ax.set_xlabel('k')
ax.set_ylabel(r'y(k)')
ax.set_title('Backward Rectangle Integration Rule')
ax.set_ylim((0, .5 + max(y)))

ax.text(rects1[0].get_x()+rects1[0].get_width()/2., 2., r'$x_{%s}$' %1,
        ha='center', va='bottom')

xx = np.linspace(0, 4, 100)
yy = xx**2 - 2*xx + 4

ax.plot(xx, yy, '-b')
ax.plot(x, y, 'bD')

for i in xrange(len(x)):
    ax.annotate(r'y(%s)' %i, xy=(x[i], y[i]), xytext=(-5, 5), ha='right',
                textcoords='offset points')

plt.savefig('backwardrect.png', dpi=500)