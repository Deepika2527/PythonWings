n = [1,2,3,4]
print(n[0])
print(n[1])

for i in range(1,10):
    print(i)

print("----------------------------------------")
n = [10,90,80,70]
it = iter(n)
print(list(it))
# res = list(it)
# print(res)
# print(it)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
print("Using set-------------------------------")
s = {12,45,6,7,99,0,12}
it = iter(s)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it))
# print(next(it))
print("Using Tuple")
t = (10,23,45,67)
tp = iter(t)
print(next(tp))
print(next(tp))


print("using dict")
dic = {"a":1,"b":2,"c":3}
d = iter(dic)
print(next(d))
print("Dict using values")
d= iter(dic.values())
print(next(d))
d = iter(dic.items())
print(d)
print(next(d))
print(next(d))
print(next(d))

print("Iter in functions..........")
def test(data):
    it = iter(data)
    print(next(it))
    print(next(it))
    print(next(it))
test([12,34,5,6677,89,90])

print("Using return")
def demo(d):
    return iter(d)
ans = demo({'a','b','c'})
print(next(ans))

print("using try catch")
def testing(d):
    it = iter(d)
    while True:
        try:
            print(next(it))
            print(next(it))
        except StopIteration:
            break
testing({123,5,6,7,99,0})


class Count:
    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num <=5:
            val = self.num
            self.num+=1
            return val
        else:
            raise StopIteration
c = Count()
for i in c:
    print(i)

class Mylist:
    def __init__(self):
        self.data = [10,20,30,40]
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.data):
            val = self.data[self.index]
            self.index +=1
            return val
        else:
            raise StopIteration
m = Mylist()
for r in m:
    print(r)
print("-----------------------------")
# for i in range(100000):
#     print(i)
num = iter(range(100))
print(next(num))
print(next(num))
print(next(num))
    

