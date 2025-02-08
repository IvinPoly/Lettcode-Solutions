class queue:
    def __init__(self):
        self.queue=[]

    def enqueue(self,data):
        self.queue.append(data)
        print(data," is added to queue")
    def dequeue(self):
        print(self.queue.pop(0)," is removed from the queue")
    def display(self):
        for i in self.queue:
            print(i,end=' ')
        print()
    def size(self):
        print(len(self.queue)," is the length of the queue")

ob = queue()
a=int(input("Enter the number of elements: "))
for i in range(a):
    ob.enqueue(int(input()))

ob.dequeue()
ob.display()
ob.size()
