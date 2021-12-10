import sys
import math
import cmath

print("pi =", math.pi)

print("e =", math.e)

print(math.sin(math.pi / 2))

r = 10 + 5j
print(r)

#

a = True
type(a)
print(a)

b = False
type(b)
print(b)

print(a and b)

print(a or b)

#

lista = [
    {"nome": "uno", "eta": 1},
    {"nome": "due", "eta": 2},
    {"nome": "tre", "eta": 3}
]
for i in range(len(lista)):
    print("Nome %s, età %s" % (lista[i]["nome"], lista[i]["eta"]))