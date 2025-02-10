class node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
class BST:
    def create(self,data):
        return node(data)
    
    def insert(self,node,data):
        if node is None:
            return self.create(data)

        if data<node.data:
            node.left=self.insert(node.left,data)
        
        elif data>node.data:
            node.right=self.insert(node.right,data)
        
        return node

    def inorder(self,node):
        if node is not None:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)

    def preorder(self,node):
        if node is not None:
            print(node.data)
            self.preorder(node.left)
            self.preorder(node.right)

tree=BST()
root=tree.create(8)
a=int(input("Number of elements: "))
for i in range(a):
    tree.insert(root,int(input()))
tree.inorder(root)
