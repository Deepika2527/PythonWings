subject = {'Math': 10 , 'Science' : 9 , 'Social' : 8, 'English':6}

print(subject)
print("Using setdefualt...")
print(subject.setdefault('Math'))
print(subject.setdefault('Telugu'))
subject.setdefault('telugu',5)
print(subject)
print("Using get")
print(subject.get('Math'))
print(subject.get('Hindi'))
subject.get('Hindi',3)
print(subject)
subject.pop('telugu')
print(subject)
subject.popitem()

print(subject)

# fromkeys
d = [1,2,4,5]
res = dict.fromkeys(d,12)
print(res)
# update
d1 = {1:2, 3:4 , 5:6}
print(d1)
d1.update({6:[1,23]})
print(d1)

# copy
std = {'name': 'Anu', 'clas':'python'}
new_std = std.copy()
print(new_std)



