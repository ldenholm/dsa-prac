class Node:
    def __init__(self, k):
        self.left = None
        self.right = None
        self.val = k

def search_tree(root, searchval):
    # return T/F for existence of node in tree
    if not root:
        return False
    elif root.val == searchval:
        return True
    else:
        #exists_left = search_tree(root.left, searchval)
        #exists_right = search_tree(root.right, searchval)
        return search_tree(root.left, searchval) or search_tree(root.right, searchval)
    
tree = Node(60)
tree.left = Node(40)
tree.left.left = Node(2)
tree.left.right = Node(16)
tree.right = Node(80)
tree.right.left = Node(64)
tree.right.right = Node(84)

print(search_tree(tree, 99))
print(search_tree(tree, 2))
print(search_tree(tree, 84))
print(search_tree(tree, 82))