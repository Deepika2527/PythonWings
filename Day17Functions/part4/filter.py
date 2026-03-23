print("Using map")
res = list(map(lambda n: n*2,[1,2,3,4,5]))
print(res)
res1 = list(map(lambda m: m+10,[10,20,20]))
print(res1)
l =['1','2','3']
res2 = list(map(int,l))
print(res2)
a = ['a','b','c']
res3 = list(map(str.upper,a))
print(res3)

cart = [1000,2000,3000]
res_4 = list(map(lambda n : n*0.9,cart))
print(res_4)

detials = [
    {"name":"laptop","price":1000},
    {"name":"mobile","price":2000},
    {"name":"tv","price":3000}
]
res_5 = list(map(lambda d: d['price'],detials))
print(res_5)
print(res_5[0])

details = {
    "a":"laptop",
    "b":"mobile",
    "c":"tv"
}
res_6 = list(map(lambda di :di.upper(), details.values()))
print(res_6)
res_7 = list(map(lambda di :di.upper(), details.keys()))
print(res_7)

dt = { 'a' : 10, 'b':20, 'c':30}

res_8 = list(map(lambda di : {di[0]:di[1]*2},dt.items()))
print(res_8)



marks = [34,56,78,90]
rs = list(filter(lambda m : m>=35, marks))
print(rs)



