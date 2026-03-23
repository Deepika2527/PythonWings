def demo(a,b):
    print(a, ":", b)
demo(10,20)
print("-----------------------------------")
def student(name,course,dur):
    print("Name :", name)
    print("Course: ", course)
    print("Duration: ", dur)
student("Anu",'Pfs',7)
student('Pfs','Deepu',7)
print("-----------------------------------")
def student(name,age,marks,ispassed):
    print(f"Student Name is {name} and her age is {age}, who scored {marks} Marks and she is Passed - {ispassed} ")
student("Anu",18,90,True)
print("-----------------------------------")
def fruits(fruit):
    for f in fruit:
        print(f)
fruits(['apple','mango','banana'])
print("-----------------------------------")
def mul(m,n):
    for i in range(1,n+1):
        print(f"Multiplication of {m} * {i} = {m*i}")
mul(5,10)

print("-----------------------------------")


def demo(a,b,c):
    print(a,b,c)
n = (12,12,12)
demo(*n)
demo([10,10,10],10,10)

print("-----------------------------------")

'''def test():
    pass
test()'''

def billing(items,price):
    print("Items : ", items)
    print("Price :" , price)
items =["Milk","Ghee","Sugar"]
price= (10,20,30,40)
billing(items,price)

print("-----------------------------------")

def count_char(sent):
    for sen in sent:
        print(sen)
count_char("Python")
print("-----------------------------------")
def show_stud(students):
    for k,v in students.items():
        print(k, "-", v)
show_stud(
    {"name" :"Rahul",
     "age":22}
)

# print("recusrive funtion")
# def fact(n):
#     if n ==0:
#         return 1z
#     else:
#         return n*fact(n-1)
# print(fact(5))
# print("fbonacci series")
# def fib(n):
#     if n<=1:
#         return n
#     else:
#         return fib(n-1)+fib(n-2)
# print(fib(11))

# print("recursive function to find sum of n natural numbers")
# def sum_taotal(n):
#     if n<=1:
#         return n
#     else:
#         return n+sum_taotal(n-1)
# print(sum_taotal(11))
