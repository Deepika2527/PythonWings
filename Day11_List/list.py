l = [1,2,3,4]
print(l)
print(type(l))
#heterogenous
l1 = [1,2,True,90.7,-23,["hello",'world'],"python",(12,34),1,2]
print(l1)
print(type(l1))
# mutable
print(l1[2])
l1[2] = False
print(l1)

# we can alos create list using list()
l2 = list("python")
print(l2)
l3 = list(["python","django"])
print(l3)
l4 = list([(1,2,34)])
print(l4)
l5= list([{'nm':'Python'}])
print(l5)


# indexing

l6 = [10,3,4,67,90]
print(l6[0])
print(len(l6))
'''print(l6[5])If the values is exceeding then out of range
print(l6[-6])

'''
print(l6[-2])


# slicing
a = [1,2,3,45,90,145,10,29,0,23]
print(a[::])
print(a[:3:1])
print(a[7:2])

print(a[7:2:-1])
print(a[:11])
print(a[12:14])

a1 = [1,2,3,45,90,145,10,29,0,23]
a1[2:2] = [10]
print(a1)
a1[3:5] = [(10,34)]
print(a1)


a= [1,2]
b = [3,4]

print(4 in a)
print(1 in a)

print(a in [[1,2]])

print(a + b)
'''print(a * b)'''
print(a*4)


x = [4,5]
y = [6,7]
z= y


for n in range(len(x)):
    print(n, x[n])

for k,v in enumerate(y):
    print(k,v)

print(x == y)
print(z == y)



