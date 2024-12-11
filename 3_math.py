import math
a = -1
b = -2
c = 3

## 一元二次求根公式： -x² -2x + 3 = 0
## 平方就是 ** 2
## 平方根是 ** (1/2)
## math.sqrt() 是python的math库的求平方根函数
print((-b + (b ** 2 - 4 * a * c) ** (1/2)) / (2 * a))
print((-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
print((-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
