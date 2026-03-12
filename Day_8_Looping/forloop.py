l = [1,2,3,5]

for i in l:
    print(i)

n = []

for i in l:
    n.append(i)
    print(n)

for j in range(1,9):
    if j%2 == 0:
        print(j)

'''
num =int(input("Enter the number: "))
for k in range(1,num):
    print(k * 1)'''

marks = [78,89,98,56,67,88]
total = 0
for m in marks:
    total += m
print("Total Marks...", total)

cart = ["Milk","Bread","Eggs","Rice"]
for item in cart:
    print("Buying items: ",item)


for i in range(1,11):
    if i == 3:
        continue
    print(i)

std = ["Anu","Deepika","Bonkers",'Absent',"Jp"]
for s in std:
    if s == "Absent":
        break
    print(s, 'is present')
def test():
    pass
l1 = [[12,34,5],[234,90]]
for a in l1:
    for b in a:
        print(b)
'''Task list comprehensions...'''

s = {1,34,5,6,78}
for k in s:
    print(k)

'''print("***********")
print("Hello", end="")
print("Anu")
print("How are", end = " ")
print("You")

print("Welcome", end ="-")
print("To",end = "-")
print("The", end='-')
print("Worlf of", end ="-")
print("Python", end = "$$$")'''



print('*' * 2)
print('-'* 4 + "*" * 3)
    