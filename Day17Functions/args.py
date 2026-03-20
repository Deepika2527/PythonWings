def demo(*args):
    print(args)
demo(12,3,4,5,6)

def num(*n):
    for i in n:
        print(i)
num(12,13,45)
def total(*sm):
    print(sum(sm))
total(10,10,10,10,10,10,10,10,10,10,10,10,10,10,10)


def list(*items):
    print(len(items))
list("Anu","Karthik","Meghana")


print("----------------------------------------")
print("Using both ps and args")
def bth(spname,*args,total):
    print("Welcome to ", spname)
    print("List of items ", args),
    print("Total : ", total)
    for i in args:
        print(i)
bth("SuperMart","milk","Sugar","wheat","dhal","bread",total =300)
# bth(total =300, "SuperMart","milk","Sugar","wheat","dhal","bread")


# how doe unpackin g works with args
def number(*args):
    print(args)
n = [1,2,3,4,5,6,6]
number(*n)