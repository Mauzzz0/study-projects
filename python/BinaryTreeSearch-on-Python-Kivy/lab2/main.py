# Дерево двоичного поиска
# Список сыновей
# A = A ⋂ B  Из дерева А исключаются узлы, отсутствующие в дереве В.
# А - обратный, B - симметричный


class BinarySearchTree:
    def __init__ (self, name):
        self.root = None
        self.size = 0
        self.__name__ = name
    def length(self):
        return self.size
    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1
    def _put(self,key,val,currentNode):
        if key< currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val,parent=currentNode)
    def get(self,key):
        if self.root:
            res = self._get(key,self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None
    def _get(self,key,currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)
    def delete(self,key):
        if self.size>1:
            nodeToRemove = self._get(key,self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size -1
            else:
                raise KeyError ("[ERROR] Key not in tree")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError("[ERROR] Key not in tree")
    def remove(self,currentNode):
        if currentNode.isLeaf(): # this node has no child
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren(): # this node has two child
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        else:  # this node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                                currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild,
                                                currentNode.rightChild.rightChild)
    def __contains__(self, key):
        if self._get(key,self.root):
            return True
        else:
            return False
    def __delitem__(self,key):
        self.delete(key)
    def __getitem__(self,key):
        return self.get(key)
    def __len__(self):
        return self.size
    def __iter__(self):
        return self.root.__iter__()
    def __setitem__(self,k,v):
        self.put(k,v)

    @staticmethod
    def preorder(tree): # Decorator
        print("Preorder of tree '%s':" % tree.__name__,end=" ")
        tree.root.preorder()
        print()
    @staticmethod
    def inorder(tree): # Decorator
        print("Inorder of tree '%s':" % tree.__name__,end=" ")
        tree.root.inorder()
        print()
    @staticmethod
    def postorder(tree): # Decorator
        print("Postorder of tree '%s':" % tree.__name__,end=" ")
        tree.root.postorder()
        print()
        print()

class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
    def hasLeftChild(self):
        return self.leftChild
    def hasRightChild(self):
        return self.rightChild
    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self
    def isRightChild(self):
        return self.parent and self.parent.rightChild == self
    def isRoot(self):
        return not self.parent
    def isLeaf(self):
        return not (self.rightChild or self.leftChild)
    def hasAnyChildren(self):
        return self.rightChild or self.leftChild
    def hasBothChildren(self):
        return self.rightChild and self.leftChild
    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ
    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current
    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent
    def preorder(self): # Прямой
        print(self.key, end=" ")
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()
    def postorder(self): # Обратный
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.key, end=" ")
    def inorder(self): # Симметричный
        if self.leftChild:
            self.leftChild.inorder()
        print(self.key, end=" ")
        if self.rightChild:
            self.rightChild.inorder()
    def __iter__(self):
        if self.hasLeftChild():
            for elem in self.leftChild:
                yield elem
        yield self.key
        if self.hasRightChild():
            for elem in self.rightChild:
                yield elem


if __name__ == "__main__":       #         TREE A       Preorder: 17 5 2 11 9 16 35 29 38
    treeA = BinarySearchTree("A")#           17         Inorder: 2 5 9 11 16 17 29 35 38
    treeA[17] = 17               #        //    \\      Postorder: 2 9 16 11 5 29 38 35 17
    treeA[5] = 5                 #       5      _35
    treeA[35] = 35               #     // \\    // \\
    treeA[2] = 2                 #    2   _11 _29   38
    treeA[11] = 11               #        //\\
    treeA[29] = 29               #       _9 _16
    treeA[38] = 38               #
    treeA[9] = 9                 #
    treeA[16] = 16               #

    BinarySearchTree.preorder(treeA)   # A-pre
    BinarySearchTree.inorder(treeA)    # A-in
    BinarySearchTree.postorder(treeA)  # A-post

    treeB = BinarySearchTree("B")#         TREE B       Preorder: 8 3 2 1 5 17 20 38
    treeB[8] = 8                 #           8          Inorder: 1 2 3 5 8 17 20 38
    treeB[3] = 3                 #        //   \\       Postorder: 1 2 5 3 38 20 17 8
    treeB[17] = 17               #       3      17
    treeB[2] = 2                 #     // \\     \\     A ⋂ B == { 2, 5, 17, 38 }
    treeB[5] = 5                 #    2    5     20
    treeB[20] = 20               #   //           \\
    treeB[1] = 1                 #   1             38
    treeB[38] = 38

    BinarySearchTree.preorder(treeB)   # B-pre
    BinarySearchTree.inorder(treeB)    # B-in
    BinarySearchTree.postorder(treeB)  # B-post

    # Deleting
    for Node in treeA:          # A ⋂ B == { 2, 5, 17, 38 }  #      17
        if Node not in treeB:                                #   5 /  \ 38
            treeA.delete(Node)# del treeA[Node]              # 2 /

    print("\n[UPD] Tree A with nodes in common with tree B [UPD]")
    BinarySearchTree.preorder(treeA)  # newA-pre
    BinarySearchTree.inorder(treeA)  # newA-in
    BinarySearchTree.postorder(treeA)  # newA-post




    treeA1 = BinarySearchTree("awd")
    treeA1[5] = 5
    treeA1[10] = 10
    treeA1[3] = 3
    treeA1[1] = 1
    treeA1[4] = 4
    treeA1[6] = 6
    treeA1[11] = 11

    treeB1 = BinarySearchTree("Awdaw")
    treeB1[6] = 6
    treeB1[11] = 11
    treeB1[5] = 5

    for Node in treeB1:
        treeA1.delete(Node)

    BinarySearchTree.preorder(treeA1)