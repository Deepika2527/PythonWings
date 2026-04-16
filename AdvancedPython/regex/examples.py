import re

text = "Hello!123# how are you"
print(re.findall("[a-zA-Z]",text))
print(re.findall(r"\W+",text))
print(re.findall(r"\S+",text))
print(re.findall(r"\s+",text))
space = re.findall(r"\s",text)
print(len(space))



