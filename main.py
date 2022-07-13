import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from IterativeRootFinder import *

def g(x):
	return math.sin(math.pi/2*x)

Lambda = 0.5
Mu = 0.5

def alpha(t):
	return t

root_finder = IterativeRootFinder(g, Lambda, Mu, alpha)

x = np.linspace(0, 1, 300)
yf = np.zeros((300,))
yg = np.zeros((300,))
yff = np.zeros((300,))

for i in range(yf.shape[0]):
	yg[i] = g(x[i])
	yf[i] = root_finder.f(x[i])
	yff[i] = root_finder.f(root_finder.f(x[i]))

xi = []
yi = []
xticks = []
yticks = []
for i in np.arange(-4, 5, 1):
	xn, yn = root_finder.FP[i]
	xticks.append(r'$x_{' + str(i) + r'}$')
	yticks.append(r'$y_{' + str(i) + r'}$')
	xi.append(xn)
	yi.append(yn)
	plt.plot([0,xn], [yn,yn], 'k--', linewidth=0.5, linestyle='--', dashes=(4, 4))
	plt.plot([xn,xn], [0, yn], 'k--', linewidth=0.5, linestyle='--', dashes=(4, 4))

xi.insert(0, 0)
xi.append(1)
yi.insert(0, 0)
yi.append(1)
xticks.insert(0, '0')
xticks.append('1')
yticks.insert(0, '0')
yticks.append('1')

plt.plot(x, yg, label="y = g(x)")
plt.plot(x, yf, color=(140/255,117/255,112/255), label="y = f(x)")
plt.xticks([0,1], ['0', '1'])
plt.yticks([0,1], ['0', '1'])
plt.plot(x, yff, 'r--', label="y = f(f(x))", linestyle='--', dashes=(4, 4))
plt.plot(xi, yi, 'r.')
plt.plot([0,1], [0,1], 'k--', linewidth=0.5, linestyle='--', dashes=(4, 4))

x0, y0 = root_finder.FP[0]
x1, y1 = root_finder.FP[1]
Sx = np.linspace(x0, x1)
Sy = y0 + alpha((Sx-x0)/(x1-x0))*(y1 - y0)
plt.plot(Sx, Sy, 'r', label="y = S(x)")

plt.xlim(0, 1)
plt.ylim(0, 1)
ax = plt.gca()
ax.set_aspect(1)
plt.xlabel("x")
plt.ylabel("y")
plt.xticks(xi, xticks)
plt.yticks(yi, yticks)
plt.legend(loc='upper left')
plt.show()