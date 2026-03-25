import math as m
print(m.factorial(4))
print(m.pow(3,2))
print(m.sqrt(16))
m1 = m.floor(5)
print(m.sqrt(m1))

print(m.floor(9.9))
print(m.floor(9.5))
print(m.floor(-9.5))

print(m.ceil(9.9))
print(m.ceil(9.5))
print(m.ceil(-9.5))
print(m.trunc(3.4))


import random as r
print(r.random())
print(r.randint(10,15))
print(r.randrange(0,50,2))

l= list(range(11))
print(l)
print(r.choice(l))
print(r.choices(l,k=7))
print(r.choices(l,k=11))
print(r.sample(l,k=7))
print(r.sample(l,k=11))
print(l)
l1= [23,45,67]
print(l1)
r.shuffle(l1)
print(l1)



