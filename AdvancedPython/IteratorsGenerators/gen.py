def gen():
    yield 1
    yield 2
    yield 3
g = gen()
print(next(g))
print(next(g))
print(next(g))
# print(next(g))

def even():
    for i in range(11):
        if i%2 == 0:
            yield i

g = even()
print(next(g))
print(next(g))
print("-------------------------")
for i in g:
    print(i)
print("----------------------")
def count(n):
    i = 1
    while i <=n:
        yield i
        i+=1
c = count(5)
print(next(c))
'''Task- complete the task with filehandling concept read the file form .txt and i want all the data to be printed'''
def read_file():
    with open ("data.txt","r") as f:
        for lines in f:
            yield lines

r = read_file()



