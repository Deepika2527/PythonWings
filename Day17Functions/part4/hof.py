# print("High order functions")
# def disp(func):
#     print("Hello world")
#     func()
# def greet():
#     print("Welcome to python")
# disp(greet)

# print("-----------------------------------")
# def operations(func):
#     print("Performing some operations")
#     # func()
# def greet_morning():
#     print("Good morning")
# def greet_evening():
#     print("Good evening")
# # morning = operations(greet_morning)
# # evening = operations(greet_evening)
# # print(morning)
# # print(evening)
# print(operations(greet_morning))


print("useing return")
def outer():
    print("This is outer function")
    def inner():
        print("This is inner function")
    return inner
res = outer()
# print(res)
res()
print("Using retun with operations add")
def opertaion(choice):
    def add(a,b):
        return a+b
    def mul(a,b):
        return a*b
    if choice == "add":
        return add
    else:
        return mul
# calc = opertaion("add")
# print(calc(10,10))
cal = opertaion("mul")
print(cal(10,2))



def power(n):
    def inner(x):
        return x**n
    return inner
sq = power(2)
cube = power(3)
print(sq(5))
print(cube(5))


    