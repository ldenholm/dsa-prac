class Node:
    def __init__(self, val = None):
        self.data = val
        self.next = None

class SLList:
    def __init__(self):
        self.head = Node()
    
    def AddAtHead(self, val):
        new = Node(val)
        current = self.head
        self.head = new
        new.next = current
    def printer(self):
        l = []
        current = self.head
        while current.next:
            l.append(current.data)
            current = current.next
        for x in l:
            print(x)
            
n = Node('first node')
l = SLList()
second = Node('test')
print(l.head.data)
l.AddAtHead('second test')
print(l.head.data)
l.printer()