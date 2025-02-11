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

    def palindrome(self):
        if not self.head or not self.head.next:
            return "Linked list is empty"

        slow=fast=self.head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        prev=None
        curr=slow

        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node

        first=self.head
        second=prev

        while second:
            if first.data != second.data:
                return "Not Palindrome"
            first=first.next
            second=second.next
        return "Is Palindrome"

    def palindrome1(self):
        if self.head is None:
            return "Empty list"

        else:
            cur=self.head
            l=[]
            while cur:
                l.append(cur.data)
                cur=cur.next
            
            if l == l[::-1]:
                return "Palindrome"
            
            else:
                return "Not Palindrome"
if __name__ == "__main__":
    ll=sll()
    ll.add(4)
    ll.add(4)
    ll.add(3)
    ll.add(4)
    ll.add(5)
    print(ll.palindrome1())
