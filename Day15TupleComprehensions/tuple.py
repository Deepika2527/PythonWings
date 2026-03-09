t = (1,2,9,10)
print(t)
print(type(t))

for tp in t:
    print(tp)




t1 = (12,90.9,34,True,[90.8,0])
print(t1)
print("Acessin the values")
print(t1[0])
'''trying to change the value of a particular using particular index
t1[0] = 10
print(t1)'''
t1[4][0] = 99.9
print(t1)


# tuple creation in another way
t2 = 10,4,False
print(t2)
print(type(t2))

# w3
t3 = tuple((12,34,))
print(t3)


t4 = tuple((89,))
print(t4)
print(type(t4))

t5 = ((23,))
print(t5)
print(type(t5))
t6 = ((23))
print(t6)
print(type(t6))


T = (12,34,5,6,89,6,9,-1)
print(T)
print(T.count(6))
print(T.index(34))
print(max(T))
print(min(T))

T = (12,34,5,6,89,6,9,-1)
for t in T:
    print(t)






