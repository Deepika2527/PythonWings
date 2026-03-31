import csv
f = open("dummy.csv","w",newline="")
writer = csv.writer(f)
writer.writerow(['name','age','marks'])
writer.writerow(['std1',18,90])
writer.writerow(["std2",23,99])

with open("products.csv","w",newline="") as f:
    write = csv.writer(f)
    write.writerows([
        ['productN','quantity','price','paymentMode'],
        ["iphone",1,90000,"gpay"],
        ["laptop",1,45000,'cash']
    ])

print("Using DictWriter")
with open("employee.csv","w",newline="") as file:
    print("Started.....")
    heading = ["employeeN","employeeR","employeNo"]
    write = csv.DictWriter(file,fieldnames=heading)
    write.writeheader()
    write.writerow({"employeeN":"emp1","employeeR":"Tester","employeNo":"001"})
    write.writerows([
        {"employeeN":"emp2","employeeR":"Tester","employeNo":"002"},
        {"employeeN":"emp3","employeeR":"Tester","employeNo":"003"},
    ])
    print("Successful")
