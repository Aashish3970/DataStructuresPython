class hashTable:
    def __init__(self):
        self.arraSize=100
        self.arr=[None for i in range(self.arraSize)]
    def get_hash(self,key):
        sum=0
        for i in key:
            sum+= ord(i) #ord returns ascii value
        return sum % self.arraSize #hash value is the sum module size
    
    # def add(self,key,value): #Now we have to map the value to the place given by hash
    #     position=self.get_hash(key)
    #     self.arr[position]=value
    def __setitem__(self,key,value): #We replaced add by __setitem__
        position=self.get_hash(key)
        self.arr[position]=value
    
    # def getValue(self,key):
    #     position=self.get_hash(key)
    #     # if self.arr[position] is not None:
    #     return self.arr[position]
    def __getitem__(self,key):
        position=self.get_hash(key)
        # if self.arr[position] is not None:
        return self.arr[position]
    def __delitem__(self,key):
        position=self.get_hash(key)
        self.arr[position]=None

t= hashTable()
# t.add('March 10',100)
# print(t.getValue('March 10'))

#here,, instead of t.add() function, we want to do like in dictionary, t['March 10']= 100,
#To do this, we can do override operators. __getitem__ and __setitem__ will give these functinoality. 

t['March 10']= 100
t['April10']=120
t['Spetember 30']=500
for i in t.arr:
    if i is not None:
        print(i)
# print(i for i in t.arr if i is not None)