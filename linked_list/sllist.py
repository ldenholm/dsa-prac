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
    
    def AddAtHead(self, val):
        node = Node(val)
        current = self.head
        if self.head is None:
            self.head = node
        else:
            node.next = current
            self.head = node
    
    def GetAtIndex(self, index):
        i = 0
        current = self.head
        while current is not None:
            if i == index:
                return current.data
            current = current.next
            i = i + 1


l = SLList()
l.head = Node('head')
l.Append('test')
l.Append('second')
l.Print()

l.AddAtHead('fourth')
l.Print()
print('getting index 2: ', l.GetAtIndex(2))
#l.AddAtHead('second test')