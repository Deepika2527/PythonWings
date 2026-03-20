def students(**kwargs):
    print(kwargs)
students(st1="abc",st2="def",st3='ghi')


def billing(**lst):
    for k,v in lst.items():
        print(k, "-", v)
billing(milk=35,bread=55,ghee=100,jam=60,eggs=10)

# task onbvert tupel into list
def both(*args,**kwars):
    print("Args : ", args)
    print("Kwargs : ", kwars)
both([1,2,3,4],emp1= 100,sal =500000,role='Developer')


def enquiry(in_n,*courses,contact_n,**price):
    print("Institue Name : ", in_n)
    print("Courses : ", courses)
    print("ContactNo : ",contact_n )
    print("Prices : ", price)
enquiry("AIT", 'Pfs','Jfs','Mern',contact_n= 909090909, pfs = 40000, jfs = 40000,mern =40000)



