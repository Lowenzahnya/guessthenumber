from math import *
n = int(input("Введите диапазон:- "))
p = []
count = 0
a = 0
while count < n+1:
    b = 0
    for i in range(2, a):
        if i <= sqrt(a):
            if a % i == 0:
                b = 1
            else:
                pass
    if b != 1:
        p += [a]
    count += 1
    a += 1
print(p)
