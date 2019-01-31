# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
# Given the root to a binary tree, count the number of unival subtrees.
# For example, the following tree has 5 unival subtrees:
#     0(1)
#    /    \
#  1(2)  0(3)
#      /     \
#    1(4)   0(5
#    /   \
#  1(6)  1(7)

class Node:
    def __init__(self, value, children = []):
        self.value = value
        self.children = children



#should work even if not a binary tree
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


def recursiveanswer(root):
    #base case
    if not root.children:
        return True
    else:
        result = True
        for child in root.children:
            if root.value != child.value:
                return False
            result = result and recursiveanswer(child)
        return result


node7 = Node(1)
node6 = Node(1,[])
node5 = Node(0,[])
node4 = Node(1,[node6,node7])
node3 = Node(0,[node4,node5])
node2 = Node(1,[])
root = Node(0,[node2,node3])

print(recursiveanswer(node4))
print(recursiveanswer(root))
print(recursiveanswer(node7))



for node in iterative_bfs_traversal(root):
    print(node.value)