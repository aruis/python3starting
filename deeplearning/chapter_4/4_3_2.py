import numpy as np
import matplotlib.pylab as plt


def numerical_diff(f, x):
    h = 1e-4
    return (f(x + h) - f(x - h)) / (2 * h)


def function_1(x):
    return 0.01 * x ** 2 + 0.1 * x


def function_2(x):
    return np.sum(x ** 2)


# 求x0=3 ,x1 = 4时，关于x0的偏导数
def tunction_tmp1(x0):
    return x0 * x0 + 4 ** 2


# 求x0=3 ,x1 = 4时，关于x1的偏导数
def tunction_tmp2(x1):
    return 3 ** 2 + x1 * x1


x = np.arange(0.0, 20.0, 0.1)
y = function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x, y)
plt.show()

print(numerical_diff(function_1, 5))
print(numerical_diff(function_1, 10))
print(numerical_diff(tunction_tmp1, 3))
print(numerical_diff(tunction_tmp2, 4))
