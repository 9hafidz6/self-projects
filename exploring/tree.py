# creating a tree in python 

class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None

class TreeNode:
    def createNode(self,data):
        return Node(data)

    def insert(self,node,data):
        if node is None:
            return self.createNode(data)
        if data < node.data:
            #data will traverse the left subtree
            node.left = self.insert(node.left,data)
        if data > node.data:
            #data will traverse the right subtree
            node.right = self.insert(node.right,data)
        return node 

    def traverse_inorder(self,root): # Depth First Search 
        if root is not None:
            self.traverse_inorder(root.left)
            print(root.data)
            self.traverse_inorder(root.right)

    def traverse_preorder(self,root):
        if root is not None:
            
            print(root.data)
            self.traverse_preorder(root.left)
            self.traverse_preorder(root.right)

    def traverse_postorder(self,root):
        if root is not None:
            self.traverse_postorder(root.left)
            self.traverse_postorder(root.right)
            print(root.data)

def main():
    tree = TreeNode()

    root = tree.createNode(5)
    print(root.data)
    tree.insert(root,10)
    tree.insert(root,1)
    tree.insert(root,12)
    tree.insert(root,3)
    tree.insert(root,2)
    tree.insert(root,7)
    tree.insert(root,9)
    tree.insert(root,8)
    tree.insert(root,0)

    # will try to do in order traversal, pre order traversal, post order traversal

    print("in order traverse--> ")
    tree.traverse_inorder(root)

    print("in pre traverse--> ")
    tree.traverse_preorder(root)

    print("in post traverse--> ")
    tree.traverse_postorder(root)

if __name__ == "__main__":
    main()