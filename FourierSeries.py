% matplotlib
inline
import matplotlib
from sympy import *
import numpy as np
import scipy as sp
import sympy as sy
from matplotlib import pyplot as plt
from pylab import *

x, n = sy.symbols('x n')
AK = []
BK = []
k = 10


def f(x):  # заданная функция
    return (-5 * x)


# Вычисление коэффициентов Фурье
a0 = 1 / np.pi * integrate(f(x), (x, -pi, pi))


def ak(n):
    return 1 / np.pi * integrate(f(x) * sy.cos(n * x), (x, -pi, pi))


def bk(n):
    return 1 / np.pi * integrate(f(x) * sy.sin(n * x), (x, -pi, pi))


AK += [a0]
BK += [0]
for i in range(1, k):
    AK += [ak(i)]  # заполение массива коэффициентов ак
    BK += [bk(i)]  # заполнение массива коэффициентов вк
print("f(x)= ", a0 / 2, end="")  # вывод первых членов последовательности в разложении Фурье
for i in range(1, 5):
    print(" + ", ak(i), "*cos(x) + ", bk(i), "*sin(x)", end="")


def FF(x):  # подсчёт значения функции f(x) через сумму ряда в точке x
    S = a0 / 2
    for i in range(1, k):
        S += AK[i] * sp.cos(i * x) + BK[i] * sp.sin(i * x)
    return S


N = linspace(0, 20, 60)  # от 0 до 20 на 60 интервалов
P2 = sp.array([FF(t) for t in M])
figure()
plot(N, P2, 'r')  # график функции, посчитанный через разложение в ряд Фурье до K члена
xlabel('Ось OX')
ylabel('Ось OY')
title('График полученного ряда фурье')
show()