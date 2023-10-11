#!/usr/bin/env python3

#By cuiiim6
#GNU/GPL License
#

#Sumar los primeros 10 numeros enteros

#suma = 1+2+3+4+5+6+7+8+9+10

import matplotlib.pyplot as plt

#print(suma)
fibo = []
N = 100
a = 1
b = 1


#print(a)
#print(b)
fibo.append(a)
fibo.append(b)
for x in range(N+1):
    c = a + b
   # print(c)
    fibo.append(c)
    a = b
    b = c

#print(fibo)

for i in range(len(fibo)-1):
    fibo[i+1]/fibo[i]

gold_ratio = fibo[len(fibo)-1]/fibo[len(fibo)-2]

print(gold_ratio)
x = [0,1,1,0,0]
y = [0,0,gold_ratio,gold_ratio,0]
plt.plot(x,y)
plt.gca().set_aspect('equal')
plt.show()

