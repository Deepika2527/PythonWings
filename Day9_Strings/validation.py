sen = "welcomeAIT"
print(sen.isalpha())
sen1 = "hello world"
print(sen1.isalpha())

pswd = "Welcome12344"
print("Alphanumeric")
print(pswd.isalnum())
print('Welcome 123'.isalnum())

print('0-9 validates and returns true  decimal values')
print('1234'.isdecimal())
print('-1234'.isdecimal())
print('Ⅹ'.isdecimal())
print('½'.isdecimal())


print("isNumeric workkd with roman,super,fraction but not -ve")
print('1234'.isnumeric())
print('-1234'.isnumeric())
print('Ⅹ'.isnumeric())
print('½'.isnumeric())
print('⁰'.isnumeric())
print('34.6'.isnumeric())


print("Isdigit- Only for no's and super")
print('1234'.isdigit())
print('-1234'.isdigit())
print('Ⅹ'.isdigit())
print('½'.isdigit())
print('⁰'.isdigit())
print('34.6'.isdigit())
'''Task1 - take a mobile no , check then len it shouldreturn t
'''


print(isinstance('123',str))
print(isinstance('89.0',str))
print(isinstance(123,str))