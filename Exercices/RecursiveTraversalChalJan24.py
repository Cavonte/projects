# image
# https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
# Daily Coding Problem: Problem #3
class Node:
    def __init__(self,value,left = None, right= None):
        self.value = value
        self.right = right
        self.left = left

node5 = Node('Node5',None,None)
node4 = Node('Node4',None,None)
node2 = Node("Node2",node4,node5)
node3 = Node("Node3",None,None)
root = Node('one',node2,node3)

def inorderTraversal(root):
    if root.right == None and root.left == None:
        print(root.value)
        return root.value

    #Inorder(left,root,right)
    inorderTraversal(root.left)
    print(root.value)
    inorderTraversal(root.right)


# Think ea, base of the game, then the nodes as dlc
def preoderTraversal(root):
    if root.right == None and root.left == None:
        print(root.value)
        return root.value

    print(root.value)
    preoderTraversal(root.left)
    preoderTraversal(root.right)

# PostOrder (left,right,root)
# BFS(left,right)

# inorderTraversal(root)
preoderTraversal(root)


