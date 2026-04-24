from threading import Thread
from threading import Event
from time import *
import queue




# print("Race condtion,mutex,semphore")
# q = queue.Queue()
# def producer():
#     for i in range(5):
#         print("From Producer", i)
#         q.put(i)
#         sleep(1)
# def consumer():
#     for i in range(5):
#         # sleep(1)
#         item = q.get()
#         print("From Consumer", item)
# t = Thread(target=producer)
# t1 = Thread(target=consumer)

# t.start()
# t1.start()



print("using flag...")


flag = Event()
def worker():
    print("work started")
    flag.wait()
    print("Work stopped")
def starter():
    sleep(5)
    flag.set()
    print("Stater finished")

t1= Thread(target=worker)
t2 = Thread(target=starter)

t1.start()
t2.start()
t1.join()
t2.join()
