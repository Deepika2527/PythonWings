l =[12,3,4,5,7]
res = {n:n+1 for n in l}
print(res)
print(type(res))


print("Using range")
reuslt = {i:i+1 for i in range(1,11,3)}
print(reuslt)

s= {1,2,4,5,6}
toStr = {w:str(w) for w in s}
print(toStr)

course = ['python','django','php','html']
starts =  {ch:ch.startswith("p") for ch in course}
print(starts)


n = [1,2,34,5,6,7,8]
even = {e:'Even' for e in n if e%2==0}
print(even)
odd = {o:'Odd' for o in n if o%2!=0}
print(odd)


pets = ['Doggy','Cat','Fish','Snake','Hamster','Birds']

p = {pt:len(pt) for pt in pets if len(pt)>3}
print(p)


n = [1,2,4,5,6,7,8,9,10]

even_odd = {i:'Even' if i%2==0 else 'Odd'  for i in  n}
print(even_odd)

m = [-3,5,6,7,-2,-9]
neg  = {x:'Pos' if x>0 else 'Neg' for x in m}
print(neg)

words = ['Pen','Notebook','Text','Scale','dstr','ten']
d = {w:'Long' if len(w)>4 else 'Short' for w in words}
print(d)

print("Using tuple.....")
t  = (1,2,4,5,7)
t1 = (i for i in t)
print(t1)
print(type(t1))
print(next(t1))
print(next(t1))

print("How do we use it")
t2 =  tuple(j for j in t if j>4)
print(t2)
print(type(t2))

t3 = tuple(j for j in range(0,50,5) if j >=30)
print(t3)


