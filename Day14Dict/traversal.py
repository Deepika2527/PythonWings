sub  = {'sci': 9, 'Math' : 10, 'soci' : 6}

for s in sub:
    print(s)
print("printing keys..")
for keys in sub:
    print(keys)
print("getting values...")
for val in sub.values():
    print(val)
print('keys and values...')
i = 0
for k,v in sub.items():
    print(i, k, v)
    i+=1
print("using enumerate")

for ke,va in enumerate(sub):
    print(ke,va)
print("enumerate getting keya and values using items")
for j, (key,val) in enumerate(sub.items()):
    print(j , key, val)



