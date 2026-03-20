total_orders= 0 #global
def store():
    daily_orders =0 #enclosing
    def place_order():
        global total_orders
        nonlocal daily_orders
        total_orders +=1
        daily_orders +=1
        print("Daily : ", daily_orders , "|" , "Total Orders : ", total_orders)

    place_order()
    place_order()
    place_order()
store()
store()




print("LEGB--------------------")

def locald():
    a = "Local"
    print(a)
locald()

def en_outer():
    b = "Enclosing"
    def en_inner():
        print(b)
    en_inner()
en_outer()


c = "global"
def g_demo():
    print(c)
g_demo()

print("________________________")
m = "Global"
def mixed_O():
    # m = "enclosing"
    def mixed_i():
        # m = "local"
        print(m)
    mixed_i()
    print(m)
mixed_O()
print(m)
        