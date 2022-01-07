class Node:
    def __init__(self, k):
        self.left = None
        self.right = None
        self.key = k


def size_of_binary_tree(node):
    size = 0
    if node == None:
        return 0
    elif node.key != None:
        # recursively call left
        size += size_of_binary_tree(node.left)
        size += 1
        size += size_of_binary_tree(node.right)
    return size

def concise_size_of_binary_tree(node):
    if node == None:
        return 0
    else:
        leftsubtree = concise_size_of_binary_tree(node.left)
        rightsubtree = concise_size_of_binary_tree(node.right)
        return leftsubtree + rightsubtree + 1         

tree = Node(10)
tree.left = Node(5)
tree.left.left = Node(1)
tree.right = Node(20)
print(size_of_binary_tree(tree))

print(concise_size_of_binary_tree(tree))

def even_more_concise_size(node):
    if node == None:
        return 0
    else:
        return even_more_concise_size(node.left) + even_more_concise_size(node.right) + 1

print(even_more_concise_size(tree))


#    10
#   /  \
#  5   20
# /
#1