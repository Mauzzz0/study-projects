import random
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView

Window.size= (1800,900)
Window.clearcolor = (1, 1, 1, 1)
__width__ = 17
__height__ = 50
__fsize__ = "15"

mx_lvl = list()
maxdepth = 0

class Label01(Label):
    pass
class Label0(Label):
    pass
class Label1(Label):
    pass
class Label00(Label):
    pass

class TreeApp(App):
    def build(self):
        bl = GridLayout(cols=1,size_hint=(None,None),width=(2**(maxdepth+1)*__width__),height=(maxdepth+1)*__height__)
        for i in range(maxdepth+1):
            inside_bl = GridLayout(cols = 2**i,size_hint=(None,None),width=(2**(maxdepth+1)*__width__),height=__height__)
            for j in range(2 ** i):
                lc = 0
                rc = 0
                try: lc = mx_lvl[i+1][j*2] 
                except: pass
                try: rc = mx_lvl[i+1][j*2+1] 
                except: pass 

                if lc != 0 and rc != 0:
                    widget = Label01(text=str(mx_lvl[i][j]), color=(0,0,0, 1),font_size=__fsize__)
                elif lc != 0 and rc == 0:
                    widget = Label0(text=str(mx_lvl[i][j]), color=(0,0,0, 1),font_size=__fsize__)
                elif lc == 0 and rc != 0:
                    widget = Label1(text=str(mx_lvl[i][j]), color=(0,0,0, 1),font_size=__fsize__)
                elif lc == 0 and rc == 0 and mx_lvl[i][j] != 0:
                    widget = Label00(text=str(mx_lvl[i][j]), color=(0,0,0, 1),font_size=__fsize__)
                else:
                    widget = Label00(text=str(mx_lvl[i][j]), color=(0, 0, 0, 0),font_size=__fsize__)

                inside_bl.add_widget(widget)
            bl.add_widget(inside_bl)
        root = ScrollView(size_hint=(None,None), size=(Window.width, Window.height))
        root.add_widget(bl)
        return root

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
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren():
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        else:
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
    def MxLvl(self):
        self.root.MxLvl()
    def maxdepthfunc(self):
        self.maxdepth = self.root.depthOnly()[1]
        return self.maxdepth
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
    def preorder(tree):
        print("Preorder of tree '%s':" % tree.__name__,end=" ")
        tree.root.preorder()
        print()
    @staticmethod
    def inorder(tree):
        print("Inorder of tree '%s':" % tree.__name__,end=" ")
        tree.root.inorder()
        print()
    @staticmethod
    def postorder(tree):
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
    def hasOnlyLeftChild(self):
        return self.leftChild and not self.rightChild
    def hasOnlyRightChild(self):
        return self.rightChild and not self.leftChild
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

    def depthOnly(self, c=-1, maxi=0):
        c += 1
        if c > maxi:
            maxi = c
        if self.leftChild:
            c, maxi = self.leftChild.depthOnly(c, maxi)
        if self.rightChild:
            c, maxi = self.rightChild.depthOnly(c, maxi)
        c -= 1
        return c, maxi

    def MxLvl(self,c=-1):
        global mx_lvl
        c+=1
        if self.leftChild:
            c = self.leftChild.MxLvl(c)
        if not self.hasAnyChildren():
            mx_lvl[c].append(self.key)
            g = 0
            for i in range(c,maxdepth):
                g+=1
                for j in range(2**g):
                    mx_lvl[c+g].append(0)
        elif self.hasBothChildren():
            mx_lvl[c].append(self.key)
        elif self.hasOnlyLeftChild():
            mx_lvl[c].append(self.key)
            mx_lvl[c+1].append(0)
            g = 0
            for i in range(c+2,maxdepth+1):
                g+=1
                for j in range(2**g):
                    mx_lvl[i].append(0)
        elif self.hasOnlyRightChild():
            mx_lvl[c].append(self.key)
            mx_lvl[c + 1].append(0)
            g = 0
            for i in range(c + 2, maxdepth + 1):
                g += 1
                for j in range(2 ** g):
                    mx_lvl[i].append(0)
        if self.rightChild:
            c = self.rightChild.MxLvl(c)
        
        c-=1
        return c
    def preorder(self):
        print(self.key, end=" ")
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()
    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.key, end=" ")
    def inorder(self):
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

def GenerateTrees():
    global mx_lvl
    global maxdepth
    treeA = BinarySearchTree("A")
    for _ in range(30):
        rnd = random.randrange(100)
        treeA[rnd] = rnd
    # [1,2,3,4,5,6,7,8,9,10,11,12,13,14,13.5,12.5,11.5,8.5,6.5,4.5,2.5] TODO: Километровая линия
    # [11,12,13,14,13.5,12.5,11.5,14.5,14.1,14.6,14.51,14.65] #TODO: Дробные широкие цифры
    # [50,35,75,12,6,3,2,1,8,6,10,4,5,11,9,13,14,15,16,20,21,17,19,18,23,28,22,24,20]
    # [11,12,13,14,15,16,17,18,19,20,21] TODO: this!!
    #for _ in [11,12,13,14,15,16,17,18,19,20,21]:
    #    treeA[_] = _
    BinarySearchTree.preorder(treeA)
    BinarySearchTree.inorder(treeA)
    BinarySearchTree.postorder(treeA)

    maxdepth = treeA.maxdepthfunc()
    print("MaxDepth:" + str(maxdepth))
    mx_lvl = [[] for x in range(maxdepth+1)]
    treeA.MxLvl()
    print(mx_lvl)


if __name__ == "__main__":
    GenerateTrees()
    TreeApp().run()