s = {1,2,4,5,6}
print(s)
print(type(s))

s1 = set({1,2,34})
print(s1)


l = []
t = ()
s = {}
di = {}


print(l)
print(t)
print(s)
print(di)


print(type(l))
print(type(t))
print(type(s))
print(type(di))


s1 = {1,5,False,True,90.0,87+7j,'Python',0}
print(s1)
'''print(s1[0])'''




'''a = {1,2,4,7}
b = {10,12}
# print(a + b)
print(a *2)'''


a = {1,2,4,7}
print( 1 in a)
print('2' in a)


for a1 in range(len(a)):
    print(a1)
    # print(a[a1])

for k,v in enumerate(a):
    print(k,v)