import os
print("Currentworkingdir", os.getcwd())
print("List of Dirs:", os.listdir())
print("---------------------------------------")
# os.mkdir("TestFolder")
# os.makedirs(r'ParentF\ChildF')
# os.removedirs("TestFolder")
# os.removedirs('ParentF\ChildF')

# folder = "TestFolder"

# print(os.path.exists(folder))

# if not os.path.exists(folder):
#     os.mkdir(folder)
# else:
#     print("Already existed")

# folder = r"C:\Users\cool\Desktop\PythonWings\TestFolder"
# filename = "dummy.txt"

# file_path =os.path.join(folder,filename)
# with open(file_path,"w") as f:
#     f.write("HelloPython...")


print("---------------------------------------------------")

# Nfolder = r"C:\Users\cool\Desktop\PythonWings\NewFolder"
# os.makedirs(Nfolder,exist_ok=True)
# newfile = "Read.txt"
# file_pt = os.path.join(Nfolder,newfile)
# with open(file_pt,"w") as f:
#     f.write("Hello Im a new Theory file")
# print("------------------------------------------")
# os.rename(r"C:\Users\cool\Desktop\PythonWings\NewFolder\Readme.txt",r"C:\\Users\cool\Desktop\PythonWings\NewFolder\updated.txt")


# print("-------------------------------------------------------")

# splt = r"C:\Users\cool\Desktop\PythonWings\NewFolder\updated.txt"
# res = os.path.split(splt)
# print(res)

# splt1 = r"C:\Users\cool\Desktop\PythonWings\NewFolder"
# reslt = os.path.split(splt1)
# print(reslt)

print(os.getcwd())
ab_path = r"C:\Users\cool\Desktop\PythonWings\NewFolder"
print("Absoulte_Path", os.path.exists(ab_path))
os.chdir(r"C:\Users\cool\Desktop\PythonWings\NewFolder")
print(os.getcwd())

relative_path = r"PythonWings\NewFolder"

print("Relative_path", os.path.exists(relative_path))