import sys
import math
import cmath
import time

print("pi =", math.pi)

print("e =", math.e)

print(math.sin(math.pi / 2))

r = 10 + 5j
print(r)

print()
#boolean

a = True
type(a)
print(a)

b = False
type(b)
print(b)

print(a and b)

print(a or b)

print()
#liste

lista = [
    {"nome": "uno", "eta": 1},
    {"nome": "due", "eta": 2},
    {"nome": "tre", "eta": 3}
        ]
for i in range(len(lista)):
    print("Nome %s, età %s" % (lista[i]["nome"], lista[i]["eta"]))

T1 = time.time()

l1 = [1, 2]
l2 = ['a', 'b']
l3 = [3]
l = [(e1, e2, e3) for e1 in l1 for e2 in l2 for e3 in l3]
print(l)

l4 = range(10)
list(l4)
print(l4)
l = [el*2 for el in l4]
print(l)
l.append(20)
print(l)

T2 = time.time()
print('tempo di esequzione', T2-T1, 's')

l.pop()
print(l)

print()
#tuple

tub = (1,2,3)
#tub.append(4)
print(tub)

print()
#dizionari

d = {'nome': 'Mario', 'cognome': 'Rossi'}
print(d['nome'])

print()
#cicli

num = 42
x = input('scegli un numero da 1 a 100 ')
if int(x) == num:
  print('hai vinto')
else:
  print('riprova sarai più fortunato')

k = []
for i in range(0, 10):
  k.append(i)

print(k)

s = 0
j = True
i = 1
while j:
  s = s + 1/i
  if s > 10:
    break
  i+=1
  
print(i)
