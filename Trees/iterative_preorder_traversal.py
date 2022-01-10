from typing import Deque


class Node:
    def __init__(self, k):
        self.left = None
        self.right = None
        self.val = k

def iterative_preorder_traversal(tree):
    if not tree:
        return None
    stack = []
    current = tree
    while current:
        stack.append(current)
        current = current.left
    while len(stack) > 0:
        # all we need to do is pass 0 as pop parameter,
        # this wil change the stack to pop from the start
        # so if we think about it we are now popping the root
        # before left/right in the stack
        current = stack.pop(0)
        print(current.val)
        current = current.right
        while current:
            stack.append(current)
            current = current.left

tree = Node(10)
tree.left = Node(8)
tree.left.left = Node(6)
tree.left.right = Node(9)

iterative_preorder_traversal(tree)

# def pre_order_traversal(root):
#     # preorder = root, left, right
#     if root != None:
#         print(root.val)
#         pre_order_traversal(root.left)
#         pre_order_traversal(root.right)
# pre_order_traversal(tree)