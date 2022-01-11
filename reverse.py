def reverse(s):
    counter = len(s)-1
    #print(s[counter])
    wordRev = ""
    for x in s:
        print(s[counter])
        wordRev += s[counter]
        counter = counter - 1
    print(wordRev)
reverse('tnerruc')

class Stack:
    data = []

    def Remove(self):
        return self.data.pop()
    
    def Add(self, data):
        self.data.append(data)

    def Print(self):
        for x in self.data:
            print(x)
            print(len(self.data))
    
    def Find(self, index):
        return self.data[index]

        # by appending then popping we are always adding to end of list, but equally always removing from end of list via pop

def StackTester():
    stack = Stack

    stack.Add(stack, "cool")
    stack.Add(stack, "second")
    stack.Print(stack)
    print(stack.Find(stack, 1))
    print('popping: ', stack.Remove(stack))
    stack.Print(stack)


StackTester()


class Queue:
    data = []

    def Add(self, data):
        self.data.append(data)

    def Remove(self):
        return self.data.pop(0)
    
    def Print(self):
        for x in self.data:
            print(x, 'at index', self.data.index(x))

def QueueTester():
    q = Queue
    q.Add(q, "first")
    q.Add(q, "2nd")
    q.Add(q, "third3333")
    q.Print(q)
    q.Remove(q)
    q.Print(q)

QueueTester()