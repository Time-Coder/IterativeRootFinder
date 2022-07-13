# 寻找函数迭代根

IterativeRootFinder.py 提供了一个寻找函数迭代根的类。用于寻找定义在 `[0, 1]` 上的严格单调递增的连续自映射函数的二次迭代根。方法如下：
```python
import math
import numpy as np
import matplotlib.pyplot as plt
from IterativeRootFinder import *

# 定义一个待求迭代根的函数 g
def g(x):
    return math.sin(math.pi/2*x)

# 在 ]0, 1[ 范围内任选两个数 Lambda 和 Mu
Lambda = 0.5
Mu = 0.5

# 定义一个 [0, 1] 映射到 [0, 1] 的严格单调递增的连续自映射 alpha
def alpha(t):
    return t

# 将 g, Lambda, Mu, alpha 传入 IterativeRootFinder
root_finder = IterativeRootFinder(g, Lambda, Mu, alpha)

# 绘制 g(x), f(x), f(f(x)) 的图像
x = np.linspace(0, 1, 300)
yf = np.zeros((300,))
yg = np.zeros((300,))
yff = np.zeros((300,))

for i in range(x.shape[0]):
    yg[i] = g(x[i])
    yf[i] = root_finder.f(x[i])
    yff[i] = root_finder.f(root_finder.f(x[i]))

plt.plot(x, yg, label="y = g(x)")
plt.plot(x, yf, color=(140/255,117/255,112/255), label="y = f(x)")
plt.plot(x, yff, 'r--', label="y = f(f(x))", linestyle='--', dashes=(4, 4))
plt.legend(loc='upper left')

plt.xlim(0, 1)
plt.ylim(0, 1)
ax = plt.gca()
ax.set_aspect(1)

plt.show()
```

您可直接运行 main.py，也可修改 main.py 以适应您的需求。