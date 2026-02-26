# append
a= [11,22,34]
a.append(12)
print(a)

a.extend([56,78])
print(a)
a.extend([(90)])
'''want to extend with tuple then add ,'''
a.extend([(57,)])
print(a)

# insert
b= [34,56,78]
b.insert(2,10)
print(b)
b.insert(6,3)
print(b)

'''b.insert(-1,100)
print(b)'''


z = [1,2,34,4,78]
z.pop()
print(z)
z.pop(2)
print(z)

y = [True,False,True,False]
y.remove(True)
print(y)


y.clear()
print(y)
'''del(y)
print(y)'''

s = [1,2,4,5,6,709,23,87,34]
'''s.sort()
print(s)'''
s.sort(reverse=True)
print(s)


r = ["python","Is","My","Life"]
r.reverse()
print(r)