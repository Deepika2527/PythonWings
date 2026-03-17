def disp():
    print("Hello all....")
disp()


def greet():
    print("Python is very Interesting")
greet()


def add(a,b):
    print(a,b)
    print(a+b)
add(10,10)

def math(x,y):
    print(x+y)
    # return "Ending the function"
res = math(10,20)
print(res)
# print(type(res))



def maths(i,j):
    print("Addition", i+j)
    print("Subraction", i-j)
    print("Division", i/j)
    print("FloorDiv", i//j)
    print("Modulus", i%j)
maths(10,2)

def opt(a,b):
    return a+b, a-b
result = opt(10,2)
# print(result)
# print(type(result))
for r in result:
    print(r)

def funcwr():
    print("Hello Python")
    return 9+0
    print("Bye Python")
r = funcwr()
print(r)

