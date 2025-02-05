class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
    
    def segregate_and_print(self):
        negatives = []
        positives = []
        temp = self.head
        
        while temp:
            if temp.data < 0:
                negatives.append(temp.data)
            else:
                positives.append(temp.data)
            temp = temp.next
        
        #negatives.sort()
        result = negatives + positives 
        print(result)
        print("Sorted Negatives:", *negatives)
        print("Unsorted Positives:", *positives)

ll = LinkedList()
n = int(input("Enter number of elements: "))
for _ in range(n):
    ll.insert(int(input()))

ll.segregate_and_print()
