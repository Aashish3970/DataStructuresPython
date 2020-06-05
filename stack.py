#Write a function in python that can reverse a string using stack data structure
from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)


def reverse_string(line):
    stack= Stack()
    for i in line:
        stack.push(i)
    
    rstr='' #Empty string. now pop from stack and put it in this string
    while stack.size()!=0:
        rstr+=stack.pop()
    
    return rstr

if __name__== '__main__':
    print(reverse_string("Hi I am Aashish"))



    
