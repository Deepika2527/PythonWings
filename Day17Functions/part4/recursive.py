print("recusrsive function")

def fact(n):
    if n==0:
        return 1
    else:
        return n * fact(n-1)
res = fact(6)
print(res)


print("Fib series")
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
print(fib(4))
