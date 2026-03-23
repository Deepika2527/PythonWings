print("Function")
def square(n):
    return n*n
print(square(5))

print("Using lamda")
res = lambda n : n*n
print(res(2))

res1 = lambda st: st.upper()
print(res1("django"))


res2 = lambda x,y: x*y
print(res2(6,7))

print("Palindrome")
res3 = lambda s:"yes"  if s == s[::-1] else "no"
print(res3("madam"))
print(res3("anu"))


res4 = lambda n : n[-1]
print(res4([12,3,5]))

res5 = lambda d: sum(d.values())

print(res5({"a":10,"b":20}))
res6 = lambda di: di['c']
print(res6({"a":10,"b":20, "c": 30}))


res7 = lambda n :"even" if n%2==0 else "odd"
print(res7(10))
print(res7(11))


res8 = lambda n: ["even" if m%2==0 else "odd" for m in n]
print(res8([12,34,12]))

names = ["Anu","Krishna","Amala","Rakesh"]
res9 = lambda s : [s.startswith('A') for s in names]
print(res9(names))

