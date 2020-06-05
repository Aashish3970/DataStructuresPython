#Queue implementation using List
stockPrice=[]
stockPrice.insert(0,100)
stockPrice.insert(0,131)
stockPrice.insert(0,155)
#Since i am inserting in 0th position everytime, the previous datas are shifted to right 
print(stockPrice)
print(stockPrice.pop())

#Instead of list as queue, we can use deque module

from collections import deque
q=deque()
#deque can be used as both queue and stack. appendleft for queu whereas append for stack
q.appendleft(100)
q.appendleft(20)
q.appendleft(250)
print(q.pop())
