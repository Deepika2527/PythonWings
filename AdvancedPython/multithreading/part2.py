from threading import *
from time import *


def test(s):
    l.acquire()
    for i in s:
        print("inside the thread,", i)
        sleep(1)
    l.release()

l = Semaphore(2)
# t = Thread(target = test,args=("Hello",))
# t2 = Thread(target = test,args=("Django",))
# t3 = Thread(target=test,args=("React",))
# t.start()
# t2.start()
# t3.start()
# t.join()
# t2.join()
# t3.join()

t = Thread(target = test,args=("AAAA",))
t2 = Thread(target = test,args=("BBB",))
t3 = Thread(target=test,args=("CCC",))
t.start()
t2.start()
t3.start()
t.join()
t2.join()
t3.join()



    

