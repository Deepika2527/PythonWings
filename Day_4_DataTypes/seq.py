import sys

s1 =  'Hello Python...'
print(s1)
print(type(s1))
print(id(s1))
print(sys.getsizeof(s1))

# using " "
s1 = "Hello Anu.." \
"how are you doing Today...."
print(s1)
print(s1[0])
# s1[0] = 'h'
# print(s1)


#''' '''
s3 = ''' Hello Ait students...
          tom is a Holiday...'''

print(s3)

s4 = "html5"
print(s4)
print(type(s4))



# list

l = [1,2,4,5]
print(l)
print(type(l))
print(l[0])
print(l[2])
l[0] = 100
print(l)
l.append(900)
print(l)

l.remove(100)
print(l)

l1 = [12,12,True, 14.6, [3,5,6,7,'hello']]
print(l1)

print(l1[3])
# print(l1[3][2])

# tuple
t = (1,6,9,0,90,0)
print(t)
print(t[0]) 
# t[0] = 100
# print(t)

t1 = (False,'false',90,100,67.90)
print(t1)
print(type(t1))


# set - 


