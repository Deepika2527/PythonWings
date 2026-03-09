n= [12,3,4,5]
l = []

for m in n:
    l.append(m)
print(l)

print("Using list comprehension")
res = [r*r for r in n]
print(res)
print(n)
mul =  [m*2 for m in n]
print(mul)

cube = [c**3 for c in n]
print(cube)



print("Using range")
rng =  [n for n in range(21)]
print(rng)


word = ["Hello", 'all' , 'python']

result = [len(w) for w in word]
print(result)

num = [1,2,4,1,5,690,34,24,3,89]
even = [n for n in num if n%2==0]
print(even)
odd =  [o for o in num if o%2!=0]
print(odd)

word = ['python','java','php','django']
strtwith =  [ch for ch in word if ch.startswith("p")]
print(strtwith)



print("Using ifelse...")

no = [12,3,57,90,21,-9,17,34]

even_odd =  ['Even' if n%2==0 else 'Odd' for n in no]
print(even_odd)


num = [-3,5,8,10,-9,5]
replce =  [0 if i<0 else i for i in num]
print(replce)