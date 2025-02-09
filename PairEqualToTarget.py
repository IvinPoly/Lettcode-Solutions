class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class sll:
    def __init__(self):
        self.head=None

    def add(self,data):
        new_node=node(data)

        if self.head is None:
            self.head=new_node
            return

        current=self.head
        while current.next:
            current=current.next
        current.next = new_node

    def two_sum(self, target):
        seen = {}
        current = self.head
        while current:
            complement = target - current.data
            if complement in seen:
                return (seen[complement], current.data)
            seen[current.data] = current.data
            current = current.next
        return None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')

ob=sll()
a=int(input("Enter no of elements: "))
for i in range (a):
    ob.add(int(input()))
ob.display()
print(ob.two_sum(10))
