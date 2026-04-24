from threading import *
from time import *


# def test():
#     for i in range(10):
#         print(i)
# test()

# def demo():
#     for i in range(65,91):
#         print(chr(i))
# demo()


# def test():
#     print("Inside test...")
#     for i in range(10):
#         print(i)
# t= Thread(target=test)
# t.start()
# print("Hello im outside the thread")



# def w_join():
#     print("-----------------------------")
#     for i in range(10):
#         print("Inside thread: ", i)
# t = Thread(target=w_join)
# print("Before start method")
# t.start()
# t.join()
# print("After thread")



# def testing(a,b,c,d):
#     print("Name of the function", t.name)
#     print("Id of the thread :", t.ident)
#     print("Is threadalive:", t.is_alive())
    
#     print("deamon:", t.daemon)
#     print("Args values:", a , b)
#     print("Kwargs values:", c, d)
#     print("Total:", a+b+c+d)
# # testing(10,20,30,40)
# t = Thread(target=testing,name="myfucntion",args=(10,20),kwargs={"c":30,"d":40})
# t.start()
# print("*********************************************")


# def demo():
#     for i in range(65,91):
#         print("DemoFunct", i)
#         sleep(1)

# def test():
#     for j in range(65,91):
#         print("Test fun",chr(j))
#         sleep(2)
# t = Thread(target=demo)
# t1 = Thread(target=test)
# t.start()
# t1.start()


# def disp():
#     print("Hello...")
#     print("I complted python")
#     print("---------------------")
# t = Thread(target=disp)
# print("before start")
# t.start()
# print("Happy ending with python")

def dis():
    print("Hello...")
    print("I complted python")
    print("---------------------")
    sleep(1)
    print("It will never excutes")
t = Thread(target=dis,daemon=True)
print("before start")
t.start()
sleep(0.5)
print("Happy ending with python")

