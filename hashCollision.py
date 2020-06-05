# Chaininig in Python:
# When two keys has same asicc values, they try to be mapped to a same position 
# in an array. Theis creates collision. TO solve this, linear probing is used. IN linear probing, now if the space 
# is that a key is trying to be mapped is occupied already, it while try to fnind the next
# slot and so on. Instead, we will use chaining. Chaining uses linked list. If two keys are trying to be
# mapped to a same position in array, we create a linked list and add both of them,

class hashTable:
    def __init__(self):
        self.arraySize=100
        self.arr= [[] for i in range(self.arraySize)] #array of list, in each list, we will make (key,value) tuple

    def getHash(self,key):
        ASCIsum=0
        for i in key: 
            ASCIsum+= ord(i)
        return ASCIsum % self.arraySize
    
    def __setitem__(self,key,value):
        position= self.getHash(key)
        found=False
        #At first we modify the value if the key is alraedy in the list.
        for idx, element in enumerate(self.arr[position]): #enumerate through the linked list in arr[position] if there is a linked list
            if len(element)==2 and element[0]== key: #if the key that we passed to this functino is already in linked list, we need to update this value
                self.arr[position][idx] =(key,value) #put the tuple in self.arr[position][idx] i.e (idx position of the list)
                found= True
                break
        if not found:
            self.arr[position].append((key,value))    #append the key,value tuple 

    def __getitem__(self,key):
        position=self.getHash(key)
        foundList=[]
        for i,(po,value) in enumerate(self.arr[position]):
            if key ==po:
                foundList.append((po,value))
                return foundList
        


t=hashTable()
t["March 10"]=100
t["march 8"]=20
t["March 10"]=150
t["March 10"]=0
t["March 100"]=200
t["March 010"]= 120
t["March 001 "]=230
print(t.arr)
print('\n'+ str( t["March 01"] ))