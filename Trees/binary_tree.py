class Node:
    def __init__(self, k):
        self.left = None
        self.right = None
        self.key = k


# Visualization

#    30
#   /  \
#  40  50
# /    / \
#70   60  80


# How it looks with our Node struct

root = Node(30)
root.left = Node(40)
root.right = Node(50)
root.left.left = Node(70)
root.right.left = Node(60)
root.right.right = Node(80)
#print(root.key)

def in_order_traversal(root):
    if root != None:
        in_order_traversal(root.left)
        print(root.key)
        in_order_traversal(root.right)
in_order_traversal(root)