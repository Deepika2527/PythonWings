A = {1,2,3,4,5,6,7,8,9,10}
a ={1,2,3,4,5}
b= {4,5,6,7,8,9,10}
B = {1,2,3,4,5,6,7,8,9,10}

print(A.issuperset(B))
print(B.issuperset(A))
print("subSet")
print(a.issubset(A))
print(A.issubset(a))
print("**********")


a = {1,2,4,5,6,7,8}
b = {10,12,6,8,2,15}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))
print(a)
print(b)


'''

Task
| &  - ^
isdishjoint()



'''


print(a.intersection_update(b))
print(a)
print(b)




