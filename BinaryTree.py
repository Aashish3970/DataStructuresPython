class binarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addChild(self, data):
        if data == self.data:
            return
        if data <= self.data:
            # add data in the left subtree
            if self.left:
                # if there is an existing node in left side, we craete a child of node which is in self.left.
                self.left.addChild(data)
            else:
                self.left = binarySearchTreeNode(data)
        else:
            # add data in right subtree
            if self.right:
                self.right.addChild(data)
            else:
                self.right = binarySearchTreeNode(data)

    def inOrderTraversal(self):
        elements = []
        # at first visit all of the left nodes
        if self.left:
            elements += self.left.inOrderTraversal()

        # visit the root node
        elements.append(self.data)

        # visit all of the right nodes
        if self.right:
            elements += self.right.inOrderTraversal()

        return elements

    def search(self,value):
        if self.data== value:
            return True
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        if value >self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False



def buildTree(elements):
    root = binarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.addChild(elements[i])

    return root


if __name__ == '__main__':
    numbers = [10, 20, 190, 100, 2, 1, 30, 56, 5, 7]
    numbersTree = buildTree(numbers)
    print(numbersTree.inOrderTraversal())
    print(numbersTree.search(190))

    countryList=["Nepal","India","UK","USA","Bahrain","Germany"]
    countryTree=buildTree(countryList)
    print(countryTree.inOrderTraversal())
    print(countryTree.search("Nepal"))
    print(countryTree.search("Sweden"))
    