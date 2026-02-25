sent = 'Hello js. js is done. Im upskilling on py with dot py extenstion py.'
print(sent.find('js'))
print(sent.find('py'))
print(sent.find("data"))
print(sent.rfind('py'))
print(sent.rfind('net'))

print("Using index")
print(sent.index('js'))
print(sent.rindex('js'))
'''print(sent.index('place'))'''


rept = "Abbaccaacabbaaaac"
print(rept.count('c'))
print(rept.count('A'))
print(rept.count('o'))



word = "hello world"
print(word.startswith('hello'))
print(word.endswith('world'))
print(word.startswith('Hello'))
print(word.endswith('World'))