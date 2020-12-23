from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Rectangle
from kivy.graphics import Color, Line
from kivy.core.window import Window
Window.size= (1920,1080)
Window.clearcolor = (1, 1, 1, 1)


mx_link = dict()
mx_lvl = list()
mx_linkn = dict()
mx_lvln = list()
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
        bl = BoxLayout(orientation='vertical', padding=5, spacing=5)
        for i in range(maxdepth):
            inside_bl = BoxLayout(orientation='horizontal')
            for j in range(2 ** i):

                leftchild = None
                rightchild = None
                try:
                    leftchild = mx_lvl[i + 1][(j * 2)]
                except:
                    leftchild = None
                try:
                    rightchild = mx_lvl[i + 1][(j * 2) + 1]
                except:
                    rightchild = None
                if leftchild is not None and rightchild is not None:
                    inside_bl.add_widget(Label01(text=str(mx_lvl[i][j]), color=(0.5, 0.5, 0.5, 1)))
                # inside_bl.add_widget(Label01(text=str(mx_lvl[i][j]),color=(0.5,0.5,0.5,1)))
                elif leftchild is not None and rightchild is None:
                    inside_bl.add_widget(Label0(text=str(mx_lvl[i][j]), color=(0.5, 0.5, 0.5, 1)))
                elif leftchild is None and rightchild is not None:
                    inside_bl.add_widget(Label1(text=str(mx_lvl[i][j]), color=(0.5, 0.5, 0.5, 1)))
                elif leftchild is None and rightchild is None:
                    try:
                        inside_bl.add_widget(Label00(text=str(mx_lvl[i][j]), color=(0.5, 0.5, 0.5, 1)))
                    except:
                        None

                    # inside_bl.add_widget(Label01(text="byex",color=(0.5,0.5,0.5,0.5))) # тупа гений-красавчик
            bl.add_widget(inside_bl)
        return bl
    # def build(self):
    #     bl = BoxLayout(orientation='vertical', padding=5, spacing=5)
    #     for i in range(maxdepth):
    #         inside_bl = BoxLayout(orientation='horizontal')
    #         for j in range(2 ** i):
    #
    #             leftchild = None
    #             rightchild = None
    #             try: leftchild = mx_lvl[i+1][(j*2)]
    #             except: leftchild = None
    #             try: rightchild = mx_lvl[i+1][(j*2)+1]
    #             except: rightchild = None
    #             if leftchild is not None and rightchild is not None:
    #                 inside_bl.add_widget(Label01(text=str(mx_lvl[i][j]),color=(0.5,0.5,0.5,1)))
    #             #inside_bl.add_widget(Label01(text=str(mx_lvl[i][j]),color=(0.5,0.5,0.5,1)))
    #             elif leftchild is not None and rightchild is None:
    #                 inside_bl.add_widget(Label0(text=str(mx_lvl[i][j]),color=(0.5,0.5,0.5,1)))
    #             elif leftchild is None and rightchild is not None:
    #                 inside_bl.add_widget(Label1(text=str(mx_lvl[i][j]),color=(0.5,0.5,0.5,1)))
    #             elif leftchild is None and rightchild is None:
    #                 try:
    #                     inside_bl.add_widget(Label00(text=str(mx_lvl[i][j]), color=(0.5, 0.5, 0.5, 1)))
    #                 except:
    #                     None
    #
    #
    #                 #inside_bl.add_widget(Label01(text="byex",color=(0.5,0.5,0.5,0.5))) # тупа гений-красавчик
    #         bl.add_widget(inside_bl)
    #     return bl

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

    def depthAndMxLvl(self):
        return self.root.depthAndMxLvl()[1]
    def depthAndMxLvln(self):
        return self.root.depthAndMxLvln()[1]
    def depthOnly(self):
        return self.root.depthOnly()[1]
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

    def depthOnly(self, c=0, maxi=0):
        c += 1
        if c > maxi:
            maxi = c
        if self.leftChild:
            c, maxi = self.leftChild.depthOnly(c, maxi)
        if self.rightChild:
            c, maxi = self.rightChild.depthOnly(c, maxi)
        c -= 1
        return c, maxi
    #def genMxLvl(self):
    #    global mx_lvl
    #    for i in range(maxdepth):
    #        mx_lvl[i] = [0 for x in range(2**i)]
    def genMxLvln(self):
        global mx_lvln
        for i in range(maxdepth):
            mx_lvln[i] = [None for x in range(2**i)]
    def podstrah(self):
        global mx_lvl
        for i in range(maxdepth):
            while len(mx_lvl[i]) != 2**i:
                mx_lvl[i].append(0)
    def depthAndMxLvl(self,c=0,maxi=0):
        global mx_lvl
        global maxdepth
        c+=1
        if c == 1:
            mx_lvl[c-1].append(self.key)
            mx_lvl[c].append (self.leftChild.key)
            mx_lvl[c].append (self.rightChild.key)
        else:
            if self.hasBothChildren():
                mx_lvl[c].append (self.leftChild.key)
                mx_lvl[c].append (self.rightChild.key)
            elif self.hasLeftChild():
                mx_lvl[c].append (self.leftChild.key)
                mx_lvl[c].append (0)
            elif self.hasRightChild():
                mx_lvl[c].append(0)
                mx_lvl[c].append(self.rightChild.key)
            else:
                if c != maxdepth:
                    mx_lvl[c].append(0)
                    mx_lvl[c].append(0)


        #if not self.hasAnyChildren() and c!= maxdepth:
        #    for i in range(2): mx_lvl[c].append(0)
        if c>maxi:
            maxi = c
        if self.leftChild:
            c,maxi= self.leftChild.depthAndMxLvl(c,maxi)
        if self.rightChild:
            c,maxi= self.rightChild.depthAndMxLvl(c,maxi)
        c-=1
        return c,maxi
    def depthAndMxLvln(self,c=0,maxi=0):
        global mx_lvln
        global maxdepth
        c+=1
        if c == 1:
            mx_lvln[c-1][0] = self
            mx_lvln[c][0] = self.leftChild
            mx_lvln[c][1] = self.rightChild
        else:
            if self.hasBothChildren():
                mx_lvln[c][0] = self.leftChild
                mx_lvln[c][1] = self.rightChild
            elif self.hasLeftChild():
                mx_lvln[c][0] = self.leftChild
                mx_lvln[c][1] = None
            elif self.hasRightChild():
                mx_lvln[c][0] = None
                mx_lvln[c][1] = self.rightChild
            else:
                if c != maxdepth:
                    mx_lvln[c].append(None)
                    mx_lvln[c].append(None)


        #if not self.hasAnyChildren() and c!= maxdepth:
        #    for i in range(2): mx_lvl[c].append(0)
        if c>maxi:
            maxi = c
        if self.leftChild:
            c,maxi= self.leftChild.depthAndMxLvln(c,maxi)
        if self.rightChild:
            c,maxi= self.rightChild.depthAndMxLvln(c,maxi)
        c-=1
        return c,maxi
    def MxLink(self):
        global mx_link
        if self not in mx_link.keys():
            mx_link[self.key] = [0,0]
        if self.hasBothChildren():
            mx_link[self.key][0]= self.leftChild.key
            mx_link[self.key][1]= self.rightChild.key
        if self.leftChild:
            self.leftChild.MxLink()
        if self.rightChild:
            self.rightChild.MxLink()
    def MxLinkn(self):
        global mx_linkn
        if self not in mx_linkn.keys():
            mx_linkn[self] = [None,None]
        if self.hasBothChildren():
            mx_linkn[self][0]= self.leftChild
            mx_linkn[self][1]= self.rightChild
        if self.leftChild:
            self.leftChild.MxLinkn()
        if self.rightChild:
            self.rightChild.MxLinkn()
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

def GenerateTrees():
    global mx_link
    global mx_linkn
    global mx_lvl
    global mx_lvln
    global maxdepth
    treeA = BinarySearchTree("A")
    treeA[17] = 17
    treeA[5] = 5
    treeA[35] = 35
    treeA[3] = 3
    treeA[4] = 4
    treeA[4] = 4
    treeA[2] = 2
    treeA[2.5] = 2.5
    treeA[1] = 1
    treeA[11] = 11
    treeA[29] = 29
    treeA[38] = 38
    treeA[39] = 39
    treeA[10] = 10
    treeA[16.5] = 16.5
    treeA[17] = 17
    #treeA[40] = 40
    treeA[9] = 9
    treeA[16] = 16

    BinarySearchTree.preorder(treeA)
    BinarySearchTree.inorder(treeA)
    BinarySearchTree.postorder(treeA)

    maxdepth = treeA.depthOnly()
    print("MaxDepth:" + str(maxdepth))
    mx_lvl = [[] for x in range(maxdepth)]
    mx_lvln = [[] for x in range(maxdepth)]
    treeA.depthAndMxLvl()
    treeA.root.podstrah()
    treeA.root.MxLink()

    #treeA.root.genMxLvln()
    #treeA.depthAndMxLvln()
    #treeA.root.MxLinkn()
    print("By-level matrix: " + str(mx_lvl))
    print(mx_link)
    print(mx_lvln)
    print(mx_linkn)


if __name__ == "__main__":
    GenerateTrees()
    TreeApp().run()
