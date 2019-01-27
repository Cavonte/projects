# image
# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
#
# For example, given the following Node class
#
# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The following test should pass:
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'
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
        self.children = [x for x in self.children if x is not None]

    def __str__(self):
        result = self.value + self.left + self.right
        return result


node10 = Node('10', None, None)
node9 = Node('9', None, None)
node8 = Node('8', None, None)
node7 = Node('7', node10, None)
node6 = Node('6', None, None)
node5 = Node('5', None, None)
node4 = Node('4', node8, node9)
node2 = Node("2", node4, node5)
node3 = Node("3", node6, node7)
root = Node('1', node2, node3)


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
                tree_elements.append(child)
                    # print("adding:", child.value)
        iterator = iterator + 1
        if iterator >= len(tree_elements):
            break
        current_node = tree_elements[iterator]
    return tree_elements


def serialize_flattened_tree(arr):
    if not arr:
        print("Check Array")
        return False
    serialized = ""
    for element in arr:
        serialized = serialized + "," + str(len(element.children)) + "-" + element.value
        # print("," + str(len(element.children)) + "-" + element.value, end="", flush=True)
    return serialized[1:]
# inorderTraversal(root)
# preorder_traversal(root)


serialized_string = serialize_flattened_tree(iterative_bfs_traversal(root))
print(serialized_string)

split_string = serialized_string.split(',')
child_index = 1
newNodes = []
for entry in split_string:
    value = entry[2:]
    newNodes.append(Node(value, None, None))
#     needs to be done beforehand otherwise cant point to a node

node_iterator = 0
for entry in split_string:
    num_child = int(entry[0])
    if num_child == 1:
        newNodes[node_iterator].left = newNodes[child_index]
        children = [newNodes[node_iterator].left]
        children = [x for x in children if x is not None]
        newNodes[node_iterator].children = children
    elif num_child == 2:
        newNodes[node_iterator].left = newNodes[child_index]
        newNodes[node_iterator].right = newNodes[child_index + 1]
        children = [newNodes[node_iterator].left, newNodes[node_iterator].right]
        children = [x for x in children if x is not None]
        newNodes[node_iterator].children = children

    child_index = child_index + num_child
    node_iterator = node_iterator + 1

# print(newNodes)
for node in newNodes:
    print("node", node.value, end=" ")
    if node.left is not None:
        print(node.left.value, end=" ")
    if node.right is not None:
        print(node.right.value)

print()
serialized_string = serialize_flattened_tree(iterative_bfs_traversal(newNodes[0]))
print(serialized_string)


