name = "Python is my fav subject"
print(name)
print(name.split())
print(name.split(','))
print(name.split(' '))
print('Apple, Banana, grapes, kiwi'.split(','))
print('Apple, Banana, grapes, kiwi, Grapes'.split(',',3))



l = ["A","B","C","D"]
print(l)
print("*".join(l))
'''
A B C D
A+*+B+*+....

'''
print("-".join(l))
print(",".join(l))

t = ('a','b')
print("#".join(t))


l2 = ["hello","world"]
print("%".join(l2))

nums = [1,2,3,4]
nums = [str(n) for n in nums]
print("*".join(nums))


dict ={
    'name' : 'Python',
    'class' : 'online'

}

print(','.join(dict))
