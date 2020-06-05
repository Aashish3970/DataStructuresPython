class treeNode:
    def __init__(self,data):
        self.data= data
        self.children=[]
        self.parent=None
    
    def addChild(self,child):
        child.parent=self       #any object that calls this addChild functino is self. so the parent of the created children will be this self i.e. the object that called this function
        self.children.append(child)

    def getLevel(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level

    def printTree(self):
        spaces = ' ' * self.getLevel() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.printTree()
        



def buildProductTree():
    root=treeNode("Electronics")
    # root.addChild("Laptops")
    # root.addChild("Cell Phones")
    # root.addChild("Companies")

    laptop=treeNode("Laptops")
    laptop.addChild(treeNode("Dell"))
    laptop.addChild(treeNode("Mac"))
    laptop.addChild(treeNode("Hp"))

    tv=treeNode("TV")
    tv.addChild(treeNode("Samsung"))
    tv.addChild(treeNode("LG"))

    root.addChild(laptop)
    root.addChild(tv)

    root.printTree()

if __name__=='__main__':
    buildProductTree()
    

