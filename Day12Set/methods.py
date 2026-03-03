s = {1,2,3,4,6}
s.add(20)
print(s)
s.add((23))
print(s)
s.add((24,))
print(s)
# s.add(([13]))
# print(s)
s.add('python')
print(s)

'''s.add({1:3})
print(s)'''


print("update")
s.update((67,34))
print(s)
s.update(((110,11,),))
print(s)
s.update(({100:300}))
print(s)
s.update("hello")
print(s)
s.update(("Hi",))
print(s)
s.update((12,890))
print(s)
s.update(([567,891,'bye']))
print(s)


# pop
s1 = {1,2,43,5,6}
print('Pop')
s1.pop()
print(s1)

s1.remove(2)
print(s1)
'''s1.remove(100)
print(s1)
'''

s1.discard(43)
print(s1)
s1.discard(100)
print(s1)

s1.clear()
print(s1)

del(s1)
print(s1)


