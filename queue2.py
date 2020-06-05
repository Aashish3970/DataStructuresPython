from collections import deque
import threading
import time

class Queue:
    def __init__(self):
        self.buffer=deque()
    
    def enqueue(self,val):
        self.buffer.appendleft(val)
    
    def dequeue(self):
        return self.buffer.pop()
    
myQueue= Queue()
def placeOrder(orders):
    for item in orders:
        print("Placing order for:",item)
        myQueue.enqueue(item)
        time.sleep(0.5)

def serveOrder():
    time.sleep(1)
    while True:
        order=myQueue.dequeue()
        print("Serving:",order)
        time.sleep(2)


if __name__=='__main__':
    orders=['pizza','samosa','pasta','biryani','burger']

    t=time.time()

    t1=threading.Thread(target=placeOrder,args=(orders,))
    t2=threading.Thread(target=serveOrder) 

    t1.start()

    t2.start()

    t1.join()
    t2.join()

    print("Done in:",time.time()-t)

