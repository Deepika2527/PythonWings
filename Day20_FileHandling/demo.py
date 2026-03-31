import csv

# f = open("data.csv","r")
# reader = csv.reader(f)
# for r in reader:
#     print(r)
#     print(r[0])

with open("data.csv","r") as file:
    print("Yisng withopen")
    data = csv.reader(file)
    for row in data:
        print(row)
# with open("data.csv","r") as file:
#     print("Using Dict Reader")
#     reader = csv.DictReader(file)
#     for row in reader:
#         print("-----Students----")
#         for k,v in row.items():
#             print(k, ":", v)
with open("data.csv","r") as file:
    print("Using Dict Reader")
    reader = csv.DictReader(file)
    for row in reader:
        print("-----Students----")
        print(row)
       
