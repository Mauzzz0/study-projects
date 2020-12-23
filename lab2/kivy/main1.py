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
        for i in range(maxdepth+1):
            inside_bl = BoxLayout(orientation='horizontal')
            for j in range(2 ** i):
                try: inside_bl.add_widget(Label01(text=str(mx_lvl[i][j]), color=(0.5, 0.5, 0.5, 1)))
                except: inside_bl.add_widget(Label01(text="err", color=(0.5, 0.5, 0.5, 1)))

                #leftchild = 0
                #rightchild = 0
                #try:
                #    leftchild = mx_lvl[i + 1][(j * 2)]
                #except:
                #    leftchild = 0
                #try:
                #    rightchild = mx_lvl[i + 1][(j * 2) + 1]
                #except:
                #    rightchild = 0
                #if leftchild != 0 and rightchild != 0:
                #    inside_bl.add_widget(Label01(text=str(mx_lvl[i][j]), color=(0.5, 0.5, 0.5, 1)))
                ## inside_bl.add_widget(Label01(text=str(mx_lvl[i][j]),color=(0.5,0.5,0.5,1)))
                #elif leftchild != 0 and rightchild == 0:
                #    inside_bl.add_widget(Label0(text=str(mx_lvl[i][j]), color=(0.5, 0.5, 0.5, 1)))
                #elif leftchild == 0 and rightchild != 0:
                #    inside_bl.add_widget(Label1(text=str(mx_lvl[i][j]), color=(0.5, 0.5, 0.5, 1)))
                #elif leftchild == 0 and rightchild == 0:
                #    try:
                #        if str(mx_lvl[i][j]) == "0":
                #            inside_bl.add_widget(Label00(text="0", color=(0.5, 0.5, 0.5, 1)))
                #        else:
                #            inside_bl.add_widget(Label00(text=str(mx_lvl[i][j]), color=(0.5, 0.5, 0.5, 1)))
                #    except:
                #        None

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
        #if c == 0 and mx_lvl[c] != [self.key]:
        #    mx_lvl[c].append(self.key)
        debug = self.key
        # Сначала вход влево
        if self.leftChild:
            c = self.leftChild.MxLvl(c)
        #
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




        #
        # Потом вход вправо
        if self.rightChild:
            c = self.rightChild.MxLvl(c)

        c-=1
        return c
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
    global mx_lvl
    global maxdepth
    treeA = BinarySearchTree("A")
    treeA[17] = 17
    treeA[10] = 10
    treeA[11] = 11
    treeA[12] = 12
    treeA[13] = 13
    treeA[35] = 35
    treeA[5] = 5
    treeA[20] = 20
    treeA[40] = 40
    treeA[4] = 4
    treeA[45] = 45
    treeA[50] = 50
    treeA[51] = 51
    treeA[52] = 52
    treeA[53] = 53
    #treeA[3] = 3
    #treeA[41] = 41
    #treeA[42] = 42
    #treeA[43] = 43
    #treeA[44] = 44
    #treeA[9] = 9
    #treeA[8] = 8
    #treeA[7] = 7
    #treeA[6] = 6

    #treeA[3] = 3
    #treeA[4] = 4
    #treeA[4] = 4
    #treeA[2] = 2
    #treeA[2.5] = 2.5
    #treeA[1] = 1
    #treeA[11] = 11
    #treeA[29] = 29
    #treeA[38] = 38
    #treeA[39] = 39
    #treeA[10] = 10
    #treeA[16.5] = 16.5
    #treeA[17] = 17
    #treeA[9] = 9
    #treeA[16] = 16
    #treeA[36] = 36

    BinarySearchTree.preorder(treeA)
    BinarySearchTree.inorder(treeA)
    BinarySearchTree.postorder(treeA)

    maxdepth = treeA.maxdepthfunc()
    print("MaxDepth:" + str(maxdepth))
    mx_lvl = [[] for x in range(maxdepth+1)]
    treeA.MxLvl()
    print(mx_lvl)
    #treeA.root.podstrah()
    treeA.root.MxLink()

    #treeA.root.genMxLvln()
    #treeA.depthAndMxLvln()
    #treeA.root.MxLinkn()
    print("By-level matrix: " + str(mx_lvl))
    #print(mx_link)
    #print(mx_linkn)


if __name__ == "__main__":
    GenerateTrees()
    TreeApp().run()