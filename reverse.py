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

    def Pop(self):
        return self.data.pop()
    
    def Append(self, data):
        self.data.append(data)

    def Print(self):
        for x in self.data:
            print(x)
            print(len(self.data))
    
    def Find(self, index):
        return self.data[index]

def StackTester():
    stack = Stack

    stack.Append(stack, "cool")
    stack.Append(stack, "second")
    stack.Print(stack)
    print(stack.Find(stack, 1))
    print('popping: ', stack.Pop(stack))
    stack.Print(stack)


StackTester()