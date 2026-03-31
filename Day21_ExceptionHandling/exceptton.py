


# print("using default exception")
# try:
#     a = 10
#     b= 0
#     print(a/b)
# except ZeroDivisionError as e:
#     print(f"Error is {e}")
# finally:
#     print("Succesfully")


# print("Example 2")
# try:
#     val = int(input("Enter a number:"))
# except ValueError as m:
#     print(f"error Type: {m}")
# finally:
#     print("Task completed....")

# print("example 3")
# try:
#     a = int(input("Enter a value1: "))
#     b = int(input("Enter a value2: "))
#     print(a/b)
# except ZeroDivisionError as e:
#     print(f"ErrorType {e}")
# except ValueError as e:
#     print(f"ErrorType {e}")

# print("example 4-basic")
# try:
#     a = int(input("Enter a value1: "))
#     b = int(input("Enter a value2: "))
#     print(a/b)

# except ZeroDivisionError as e:
#     print(f"ErrorType {e}")
# except ValueError as e:
#     print(f"ErrorType {e}")
# except Exception:
#     print("Not possible ")

try: 
    a = 10
    b = 0
except Exception:
    print("Handlede by exception")
except ZeroDivisionError:
    print("Zerodivison")





# print("started...")
# print(10/0)
# print("Stpped")