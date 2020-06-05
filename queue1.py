#implementation of queue
from collections import deque
class Queue:
    def __init__(self):
        self.buffer= deque()
    def enqueue(self,val):
        self.buffer.appendleft(val)
    def dequeue(self):
        return self.buffer.pop()
    def isEmpty(self):
        return len(self.buffer)==0
    def size(self):
        return len(self.buffer)

queue1=Queue()

queue1.enqueue({"Name":"Aashish","Age":26, "Profession":"Engineering"})
queue1.enqueue({"Name":"Itani","Age":25, "Profession":"Doctor"})
queue1.enqueue({"Name":"Radhika","Age":30, "Profession":"Businessman"})

print(queue1.isEmpty())
print(queue1.size())
print(queue1.dequeue())