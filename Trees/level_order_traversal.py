class Node:
    def __init__(self, k):
        self.left = None
        self.right = None
        self.val = k

def level_order_traversal_iterative(root):
    # the recursive solution is O(hn) but
    # using an iterative approach we can
    # achieve O(n)

    # let's use a queue to add all child nodes before
    # printing them.
    q = {root.val}

# build the tree
tree = Node(10)
tree.left = Node(20)
tree.right = Node(30)
tree.right.right = Node(60)
tree.left.left = Node(40)
tree.left.right = Node(50)
tree.left.right.left = Node(70)
tree.left.right.right = Node(80)