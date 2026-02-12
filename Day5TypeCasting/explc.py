print(list([12,3]))
print(list((12,4)))
print(list({3,8,0,9,0}))
print(list({'a':3}))
# print(list(90))
print(list("python"))
# print(list(12.9))


# tuple
print(tuple([12,34]))
print(tuple({23,56}))
print(tuple({'name': 'Anu'}))
print(tuple("hello"))


# set 
print(set([1,2,3,4,5,9,0,0]))
print(set((2,90)))
print(set({'data':'Py', 'class':'online'}))
print(set('Bye'))

# dict

# print(dict([1,4,5,]))
# print(dict([('name','hello'), ('a', 300)]))
# print(dict((1)))


l = [12,34,56,78,12]
print(l)
print(l[0])
l1 = set(l)
print(l1)
print(type(l1))
# print(l1[0])
l2 = list(l1)
print(l2)



# None
def greet():
    print('hello')
    # return 'Bye..'
disp = greet()
print(disp)
# greet()




a = 10
b = 20
c = 10
d = 10

print(a)
print(b)
print(c)

print(id(a))
print(id(b))
print(id(c))
print(id(d))





