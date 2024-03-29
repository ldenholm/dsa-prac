class Node:
    def __init__(self, k):
        self.left = None
        self.right = None
        self.val = k

def iterative_inorder(root):
    if not root:
        return None
    stack = []
    current = root
    while current is not None:
        stack.append(current)
        current = current.left
    while len(stack) > 0:
        curr = stack.pop()
        print(curr.val)
        curr = curr.right
        while curr is not None:
            stack.append(curr)
            curr = curr.left

tree = Node(10)
tree.left = Node(20)
tree.right = Node(30)
tree.right.right = Node(60)
tree.left.left = Node(40)
tree.left.right = Node(50)
tree.left.right.left = Node(70)
tree.left.right.right = Node(80)

iterative_inorder(tree)