class stacks:
    def __init__(self):
        self.stack = []
        #self.size = size
    
    def push(self,data):
        self.stack.append(data)
        return print(data,'is added to the stack')
    def pop(self):
        return print(self.stack.pop(),"is removed from the stack")
    def peek(self):
        return print(self.stack[-1],"is at the top of the stack")
    def length(self):
        return print(len(self.stack),"is the length of the stack")
    def isempty(self):
        return self.stack == []
    def getstack(self):
        return print(self.stack[::-1])
ob = stacks()
a= int(input("Enter the number of elements: "))
for i in range(a):
    ob.push(int(input()))
ob.getstack()
ob.pop()
ob.peek()
ob.getstack()
