class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None

    def insert(self,data):
        if self.key is None:
            self.key=data
        else:
            if self.key==data:
                return
            if data < self.key:
                if self.lchild:
                    self.lchild.insert(data)
                else:
                    self.lchild=BST(data)
            else:
                if self.rchild:
                    self.rchild.insert(data)
                else:
                    self.rchild=BST(data)
                    
    def search(self,data):
        if self.key==data:
            print("Node is found")
        else:
            if data < self.key:
                if self.lchild:
                    self.lchild.search(data)
                else:
                    print("Node is not present in tree")
            else:
                if self.rchild:
                    self.rchild.search(data)
                else:
                    print("Node is not present in tree")

    def preorder(self):
        print(self.key,end=' ')
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end=' ')
        if self.rchild:
            self.rchild.inorder()

    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key,end=' ')

    def delete(self,data,rvalue):
        if self.key is None:
            print("Tree is empty!")
        if data < self.key:
            if self.lchild:
                self.lchild=self.lchild.delete(data,rvalue)
            else:
                print("Data is not there in tree")
        elif data > self.key:
            if self.rchild:
                self.rchild=self.rchild.delete(data,rvalue)
            else:
                print("Data is not there in tree")
        else:
            if self.lchild is None:
                temp=self.rchild
                if data == rvalue:
                    self.key=temp.key
                    self.lchild=temp.lchild
                    self.rchild=temp.rchild
                    temp=None
                    return
                self=None
                return temp
            if self.rchild is None:
                temp=self.lchild
                if data == rvalue:
                    self.key=temp.key
                    self.lchild=temp.lchild
                    self.rchild=temp.rchild
                    temp=None
                    return
                self=None
                return temp
            node=self.rchild
            while node.lchild:
                node= node.lchild
            self.key=node.key
            self.rchild=self.rchild.delete(node.key,rvalue)
        return self

    def min(self):
        current=self
        while current.lchild:
            current=current.lchild
        return print(current.key)

    def max(self):
        current=self
        while current.rchild:
            current=current.rchild
        return print(current.key)

    
            
def count(tree):
    if tree is None:
        return 0
    return 1+count(tree.lchild)+count(tree.rchild)
            
                    

root=BST(8)
l=[7,10,55,3,12,1,67,99,133]
for i in l:
    root.insert(i)

print("Pre order is")
root.preorder()
print()
root.delete(12,8)
root.preorder()
print()
root.min()
root.max()
