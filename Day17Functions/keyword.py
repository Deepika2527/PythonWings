def test(name,age):
    print("Name : ", name)
    print("Age : ", age)
test(name = "Anu", age = 25)


def values(a,b,c,d):
    print('A :', a)
    print('B :', b)
    print('C :', c)
    print('D :', d)
values(a= 'A', b= "B", c= "C" ,d ='D')
print("_____________________________________")
values( c= "C1" ,d ='D2',a= 'A1', b= "B2")


print("Using postional and keyword")
def greet(name,time):
    print(f"Hello {name}. Good {time}")
greet("Anu",time= "Morning")

'''def demo(id,name):
    print(f"Hello {name} your id is {id}")
demo(name="Anu",101)
'''

def test(a,b,c):
    print(a)
    print(b)
    print(c)
test(10,11,12)
test(a="H",b="C",c="nONE")

print("for defining only positional")
def onlyp(name,role,/):
    print(f'Hello {name} your desigination is {role}')
    
onlyp("Anu", "Developer")
# onlyp(name= "Anu", role="Developer")


print("_____________________________________________________")
print("defining the fun ctuon with only keyword")
def onlyk(*,a,b):
    print("Value of A is :", a)
    print("Value of B is :",b)
onlyk(a=10,b=20)


print("Both postional and keyword")

def mix(a,b,/,*,c,d):
    print(f'The value of a is {a}, B is {b}, c is {c}, d is {d}')
mix([1,2],[3,4],c="Hello", d="all")



print("---------------------------------------------------------")
def disp(a,b):
    print(a)
    print(b)
    print(f'{a} - {b}')
disp(10,20)


