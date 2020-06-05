class Node:
    def __init__(self,data=None, next=None):
        self.data= data
        self.next= next
class linkedList:
    def __init__(self):
        self.head =None
    def insertBegin(self,data):
        node= Node(data,self.head)
        self.head= node
    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        itr= self.head
        llstr=''
        while itr:
            llstr += str(itr.data) +'-->'
            itr=itr.next
        print(llstr)
    
    def insertEnd(self,data):
        if self.head is None:
            self.head= Node(data,None)
            return
        itr= self.head
        while itr.next:
            itr=itr.next
        itr.next= Node(data,None)

    def insertValues(self,dataList):
        self.head=None
        for data in dataList:
            self.insertEnd(data)

    def getLength(self):
        count=0
        itr=self.head
        while itr.next:
            count += 1
            itr = itr.next
        return count
    
    def delElement(self,index):
        if index<0 or index>= self.getLength():
            raise Exception("invalid Index")
        
        if index==0:
            self.head= self.head.next
            return
        
        count=0
        itr=self.head
        while count != index-1:
            count+=1
            itr=itr.next
        itr.next=itr.next.next
        return
    def insertElement(self,index,data):
        if index<0 or index>= self.getLength():
            raise Exception("invalid Index")
        if index==0:
            self.insertBegin(data)
            return
        count=0
        itr=self.head
        while count != index-1:
            count+=1
            itr= itr.next
        node=Node(data,itr.next)
        itr.next=node
        return
        


if __name__=='__main__':
    ll= linkedList()
    # ll.insertBegin(5)
    # ll.insertBegin(10)
    # ll.isnertEnd(200)
    dataList=['Mango','apple','Orange','Aashish','Itani','Kiwi','Grapes']
    ll.insertValues(dataList)
    length=ll.getLength()
    print("The length of linked list is "+ str(length))
    ll.delElement(4)
    # ll.insertElement(2,9)
    ll.print()
    ll.insertElement(2,9)
    ll.print()
