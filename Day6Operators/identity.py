'''
''


a = 10
b= a
c = 200
d= 10
print(a is b)
print(a is c)
print(a is d)

l1 = [1,2,3]
l2 = [1,2,3]
l3 = l1

print(l1 is l2)
print(l1 == l2)
print(l1 is l3)



print(l1 is not l2)


st = 'hello'
st1 = 'hello'

print(st is st1)

s1 = " "
s2 = "False"
# print(id(s1))
# print(id(s2))
print(s1 is s2)
print(s1 == s2)
'''


# print('name' is d )


person = {
    'name' : 'deepika',
    'class' :'react',
    'mode' : 'online'
}

person1 = {
    'name' : 'deepika',
    'class' :'react',
    'mode' : 'online'
}
print(person)
print(person['name'])
# print(person['name'] is person)
print(person is person1)
