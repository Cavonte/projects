# image
# https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
# Daily Coding Problem: Problem #3


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left
        self.children = []
        self.children.append(left)
        self.children.append(right)


node9 = Node('Node9', None, None)
node8 = Node('Node8', None, None)
node7 = Node('Node7', None, None)
node6 = Node('Node6', None, None)
node5 = Node('Node5', None, None)
node4 = Node('Node4', node8, node9)
node2 = Node("Node2", node4, node5)
node3 = Node("Node3", node6, node7)
root = Node('one', node2, node3)


def inorderTraversal(root):
    if root.right is None and root.left is None:
        print(root.value)
        return root.value

    #Inorder(left,root,right)
    inorderTraversal(root.left)
    print(root.value)
    inorderTraversal(root.right)


# Think ea, base of the game, then the nodes as dlc
def preorder_traversal(root):
    if root.right is None and root.left is None:
        print(root.value)
        return root.value

    print(root.value)
    preorder_traversal(root.left)
    preorder_traversal(root.right)

# PostOrder (left,right,root)
# BFS(left,right)


def iterative_bfs_traversal(given_root):
    tree_elements = []
    if root is None:
        print("invalid tree")
        return
    #add the current value
    tree_elements.append(given_root)
    iterator = 0
    current_node = tree_elements[iterator]
    while current_node is not None:
        #if has child append to the queue
        if current_node.children is not None:
            for child in current_node.children:
                if child is not None:
                    tree_elements.append(child)
                    # print("adding:", child.value)
        iterator = iterator + 1
        if iterator >= len(tree_elements):
            break
        current_node = tree_elements[iterator]

    for elements in tree_elements:
        print(elements.value)


# inorderTraversal(root)
# preorder_traversal(root)
iterative_bfs_traversal(root)

