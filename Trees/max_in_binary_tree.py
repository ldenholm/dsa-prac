class Node:
    def __init__(self, k):
        self.left = None
        self.right = None
        self.val = k

def max_in_binary_tree(node):
    if node == None:
        return 0
    return max(max_in_binary_tree(node.left), max_in_binary_tree(node.right), node.val)

tree = Node(10)
tree.left = Node(4)
tree.left.left = Node(1)
tree.right = Node(20)
tree.right.right = Node(40)

print(max_in_binary_tree(tree))