name = "Anu"
print(name)
print(type(name))
print(len(name))
print("A")
print(type("A"))
print("welcome@1234*!*")
print(type("welcome@1234*!*"))

n1 = '''Im for testing docstring.
Please use me'''
print(n1)
print(type(n1))
print(n1[0])
print(n1[5])


'''The data is unsupported'''

# How sytrings are immutable
framework = 'django'
print(framework)
print(id(framework))
framework = 'Django'
print(framework)
print(id(framework))




char = "Hello"
print(char * 3)
print('Python Core' + 'Advanced')


s = "Apple"  
s1 = "Apple"  
print(s == s1)
print(s < s1)
print(s > s1)


word = "Python"
for word in "Python":
    print(word)







# using numbers
for n in range(1,10,2):
    print(n)
print('***')

char = 'python'
for ch in range(len(char)):
    print(ch)


string1 = "Hello"
for k,v in enumerate(string1):
    print(k,v)


print('Whose\'s laptop is this')
print("When you fall down just remeber to stand up and \"dust\" yourself..")
print("Hello all \n Plese wait the session will start...")
print("Loading \tpleasewait")
print("x4567")
print("\x45")
print("\x67")
# print("\a")
