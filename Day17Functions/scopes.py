def test():
    name  = "Anu"
    print(name)
test()
# print(name)


def billing(amount):
    cart = ['Jeans','T shirt',"frock"]
    print(f'I have purchased {cart} for amount {amount}')
billing([1000,500,1000])



print("Global")
insitute_name = "Ait"
def enquiry():
    print(f'Any one can step into {insitute_name} for course enquiry')
enquiry()

for i in range(1,10):
    print(i)
    print(insitute_name)


print("examples of local and global")
amount = 1000
def deposit():
    balance = 1000
    balance += amount
    print(balance)
deposit()
print(amount)


print("___________________________________")

batch_name = "Pfs001"
def access(name):
    enrolled = True
    print(f"Hi {name}, You are added into batch name {batch_name} ad you rae enrolled - {enrolled}")
access('AnuRadha')


print("------------------------------")
course = "react"
def demo():
    course = "python"
    print("Inside the function :", course)
    print(id(course))
demo()
print("Outside the function: ", course)
print(id(course))

print("___________Golbal keyword___________________")
x = 100
def test():
    global x
    x = 200
    print(x)
test()
print(x)

'''x = 100
def test():
    print(x)
    global x
    x = 200
    
test()
print(x)

SyntaxError: name 'x' is used prior to global declaration '''

balance = 1000
def deposit(amount):
    global balance
    balance += amount
    print("Total Balnce", balance)
deposit(1000)
deposit(1000)



count = 1
def counter():
    global count
    count += 1
    print("Counter value : ", count)
counter()
counter()



def outer():
    a = 10
    def inner():
        print(a)
    inner()
outer()


print("Example of nonlocal")
'''def nlouter():
    a = 'hello'
    def nlinner():
        a = "Hello"
        print(a)
    nlinner()
    print(a)
nlouter()'''

def nlouter():
    a = 'hello'
    def nlinner():
        nonlocal a
        a = "Hello"
        print(a)
        print(id(a))
    nlinner()
    print(a)
    print(id(a))
    
nlouter()

crs = "React"
def o_course():
    crs = "Python"
    def i_course():
        global crs
        crs = "django"
        print("Inside the inner Function : ", crs)
    i_course()
    print("Course outside of innerfun: ", crs)
o_course()
print("Gloablly Course : ", crs)



crse = "React"
def nlcourse():
    crse = "Python"
    def nlcourse():
        nonlocal crse
        crse = "django"
        print("Inside the inner Function : ", crse)
    nlcourse()
    print("Course outside of innerfun: ", crse)
nlcourse()
print("Gloablly Course : ", crse)


def shopping_cart():
    cart_total = 0
    def add_item(price):
        nonlocal cart_total
        cart_total += price
        print("Cart Total : ", cart_total)
    add_item(100)
    add_item(250)
    add_item(1000)
shopping_cart()
# shopping_cart()









