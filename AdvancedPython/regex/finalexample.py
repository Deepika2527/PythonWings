import re

# match1 = re.match("hello","hello world")
# print(match1)
# match2 = re.match("hello","world hello")
# print(match2)
# match3 = re.match("bc","ssc")
# print(match3)


# print("-------------------------------")


# print("-------------------------------")
# print("findall")
# fnd = re.findall("a","banana")
# print(fnd)
# find1 = re.findall("a ", "bana aa")
# print(find1)
# find2 = re.findall("123","welcome123")
# print(find2)
# find3 = re.findall("1 2 3","welcome123 1 2 3")
# print(find3)
# find4 = re.findall("xyz","abc")
# print(find4)


# print("----------------------------------")
# print("using span")
# spn =re.match("hello", "hello world")
# res = spn.span()
# print(res)
# print("-------------------------------")
# print("sub")
# replce = re.sub("cat","rat","cat is very fat")
# print(replce)



# print("--------------------")

# res = re.iter("a","banana")
# print(res)
# for r in res:
#     print(r.group(), r.span())



# print("quantifier")
# s = re.findall('a',"banana")
# print(s)
# s1= re.findall("a*","banana")
# print(s1)
# s2= re.findall("a*","banana na naaa")
# print(s2)
# s3 = re.findall("a+","banana")
# print(s3)
# s4 = re.findall("a+", "banaana na aa aa aaaa")
# print(s4)
# s5 = re.findall("colo?ur","color colour")
# print(s5)

# s6 = re.findall("a{2,4}","ba naa bananaa aaaa aaaaa")
# print(s6)



# s7 = re.findall("\d","1234welcome")
# print(s7)
# s8 = re.findall("\d","welcome34")
# print(s8)
# t1 = re.findall("^\d","123")
# print(t1)
# t2 = re.findall("^\d$","123")
# print(t2)
# t3 =re.findall("^\d$","1")
# print(t3)
# t4 = re.findall("^\d+$","123")
# print(t4)

# t5 = re.findall("[0-9]","welcome12309761584")
# print(t5)
# t6= re.findall("[abc]","welcome12309761584Abc")
# print(t6)
# t7 = re.findall("[a-z]","welcome12309761584")
# print(t7)
# t8 = re.findall("[A-Z]","welcome12309761584ABc")
# print(t8)




# a1 = re.findall("\n","hello\nworld")
# print(a1)

# a2 = re.findall(r"\b","hello\bworld")
# print(a2)


print(re.findall("<.*?>","<h1>Hello</hello>"))
print(re.findall("<.*>","<h1>Hello</hello>"))
print(re.findall("a.*","bananaaaa"))
print(re.findall("a.*?","bananan"))

print("-----------------------------------------testing")

spn =re.search("hello", "hello world")
res = spn.group()
print(res)


print("Part2")
print(re.findall(".b","abc tbbc cbc"))
print(re.findall(".a","bat mat rate late cape tap bag fat pattern latern"))
print(re.findall(".a","1a"))


print("Greedy")
print(re.findall("a+","aaaaaaa"))
print(re.findall("a+?","aaaaaa"))

text = "<h1>Hello</h1><p>para</p>"
print(re.findall("<.*>",text))
print(re.findall("<.*?>",text))


print(re.findall("\n","Hello\nworld"))
print(re.findall(r"\n","Hello\nworld"))
print(re.findall(r"\bworld","Hello world"))
print(re.findall("\bworld","Hello world"))
print(re.findall(r"\bworld\b","world HELLO world"))


s = re.finditer("a","capsicuma")
print(s)

for i in s:
    print(i.group(), i.span())



print



