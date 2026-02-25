word = "Python"
print(word)
print(word[0])
print(word[4])
print(word[-1])
print(word[-3])
# print(word[6]) 
'''Out of range error if we are getting the index value more than the length'''


# slicing
print(".....Slicing.....")
word = "Hello world"
print(len(word))
print(word[0:5])
print(word[1:7])
print(word[:8])
print(word[::])
print(word[::2])
print(word[::3])
print(word[8:2])
print("Negative indexing..")
print(word[::-1])
print(word[-2:-8])
print(word[-8:-2])
print(word[14:16])
print(word[8:2:-1])
print(word[-8:-2:-1])
print(word[-2:-8:-1])





''' 
-11 -10  -9   -8 -7  -6   -5   -4  -3  -2  -1
h      e   l   l o _ w o r l d
0   1 2 3 4 5 6 7 8 9 10

'''