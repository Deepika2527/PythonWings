d =  {'name':'Bob','age':2, 'place': 'us', 'place': 'India'}
print(d)
print(type(d))

# acessing the values through keys
print("***************")
print(d['age'])
print("Updating the values")
d['age'] = 3
print(d)


st = set()
print(type(st))
d1 = {}
print(type(d1))


# ways to create dict
d1  = dict([('name','Alice'),('course','pfs'),('classmode','online')])
print(d1)


d2 = dict((('html','htm5'),('css','css3')))
print(d2)

# keywordarguments

d3 = dict(fname="Anu",lname="radha")
print(d3)


d4 = {1:3,4:5, 9:10}
print(d4)

d5 = dict(d4)
print(d5)
print(type(d5))



# 
print("Taking datatypes as a values........")
student= {
    'name' : 'Anu',
      'id' : 101,
      'marks' : 99.9,
      'isfirstrank' : True,
      'Iq' :  34+6j,
      'course' : ['html','css'],
      'versions' : ('html5','Css3'),
      'upskilling' : {'python','django'},
      'poc' : {'phn': 909090909, 'place' : 'uk'}
 

}
print(student)
print(student['course'][1])
print(student['versions'][1])
print(student['upskilling'])
print(student['poc']['phn'])


print("Lets see what dt are supported as a keys")

std={
    'name' : 'Bob',
    25 : 'age',
    True : 'ispassed',
    98+1j : 'complex',
    99.7 : 'float',
    (1,2) : 'tup',
    # {1:2} : 'dic'
    # {23,89} :'set'
    # [1,3] : 'Grades'

}
print(std)
