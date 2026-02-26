l = "python"
print(l.center(12,'*'))
print(l.center(17,'*'))
text = "Hi"
print(text.ljust(6,'-'))
print(text.rjust(6,'-'))


print("Zfill")
print('123'.zfill(5))
print('-1234'.zfill(6))


otps = ["45","678","989"]
for otp in otps:
    print(otp.zfill(6))


name = "Bonkers"
age = '4'
print("My pet name is {} and he is {}".format(name,age))