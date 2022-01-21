import sys
import math
import cmath
import time
import numpy as np
import linalg
#import matplotlib as mpl
#import matplotlib.pyplot as plt


#vectorisation
a = np.arange(0,np.pi,0.1)

x = np.sin(a)

y = np.zeros(len(a))
for i in range(len(a)):
  y[i] = np.sin(a[i])

print('gli aaray sono uguali?')
if (x==y).all:
  print("si")
else:
  print("no")

print()
#operazioni
b = np.array([4,3,2,1])
c = np.arange(1,5)

d = b + c
b+=1
print('somma ', d)
print('autoincremento', b)
print('prodotto per scalare', 5*c)

print()
#reshape
a = np.arange(1,9)

c_style = a.reshape((2,2,2), order='C')
f_style = a.reshape((2,2,2), order='F')

print('a', a)
print('C style')
print(c_style)
print('F style')
print(f_style)

print()
#allocazione memoria
a = np.arange(1,5)
  #b = np.zeros_like(a)

b[:] = a[:]
c = a
b[1] = 10
print('diversa memoria', b==a)
c[1] = 20
print('stessa memoria', c==a)