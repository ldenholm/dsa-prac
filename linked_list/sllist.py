class Node:
    def __init__(self, val = None):
        self.data = val
        self.next = None

class SLList:
    def __init__(self):
        self.head = None

    def Append(self, val):
        new = Node(val)
        current = self.head
        while current.next != None:
            current = current.next
        print('Appending ' + new.data)
        current.next = new
    def Print(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next


l = SLList()
l.head = Node('head')
l.Append('test')
l.Append('second')
l.Print()

l.Append('fourth')
l.Print()
#l.AddAtHead('second test')