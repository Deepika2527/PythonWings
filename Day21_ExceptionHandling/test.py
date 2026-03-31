try:
    a = 10
    b = 0
    print(a/b)
except Exception:
    print("Hanlded b y exception")
except ZeroDivisionError:
    print("Zerodivison error")

try:
    a = 10
    b = 0
    print(a/b)

except ZeroDivisionError:
    print("Zerodivison error")
except Exception:
    print("Hanlded b y exception")