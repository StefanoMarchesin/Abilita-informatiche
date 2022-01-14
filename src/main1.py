import sys
import math
import cmath
import time
import numpy as np

#per leggere i File
l = []
with open('input.txt', 'r') as f:
  for line in f:
    line = line.strip()
    if len(line) > 0:
      a = map( int, line.split(',') )
      l.append(list(a))

print(l)
print()
#prodotto fra matrici
n = np.array([ [1,2,3], [4,5,6] ])
m = np.array([ [1,2], [3,4], [5,6] ])
print(n)
print(m)

p = np.dot(n,m)
print(p)

print()
#classi e metodi
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def presentazione(self):
    print('ciao mi chiamo ' + self.name)

p1 = Person("Stefano", 22)
p1.presentazione()

print()
#eccezioni
def divisione(x, y):
  try:
    result = x/y
  except ZeroDivisionError:
    print("stai dividendo per 0")
  else:
    print('il risultato è ' + str(result))
  finally:
    print('tutto finito')

divisione(10,0)
divisione(10,1)

print()

#tuple
coordinate = ('x', 'y', 'z')
a = float(input('inserisci coordinata x: '))
b = float(input('inserisci coordinata y: '))
c = float(input('inserisci coordinata z: '))
valore = (a, b ,c)

r = zip(coordinate, valore)
print(tuple(r))

print()
#lambda function

somma = lambda a,b: a+b

print(somma(10,2))