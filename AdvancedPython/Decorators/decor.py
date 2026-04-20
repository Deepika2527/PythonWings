# def disp(display):
#     def wrapper():
#         display()
#         print("Hi -With Intro😶‍🌫️")
#         display()
#         print("Bye -WIshing you luck 🌟🌟")
#     return wrapper


# @disp
# def display():
#     print("Anu is exicted that she finished PFS")
# display()


# print("---------------------example 2----------------------------------")
# def wish(greet):
#     def inner(name):
#         if name == "A":
#             print("Hello", name, 'Good Morning..!!')
#         else:
#             wish(greet)
#     return inner



# @wish
# def greet(name):
#     print("Hello", name)
# greet(name = "A")
# greet(name = "B")
# greet(name = "C")
# # print(greet.__name__)


# 
print("Example 3")

def access(func):
    def inner(user):
        if user == "Admin":
            print("Hello Admin, Only Admins can access....")
            func(user)
        else:
            print("Access denined❌")
    return inner


@access
def dashboard(user):
    print("Welcome to the dashboard", user)
# dashboard(user = "Admin")
dashboard(user="Developer")