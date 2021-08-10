#singly linked list 

class Node:
    def __init__(self,curr):
        self.next = None
        self.curr = curr
    
class SLinkedlist:
    def __init__(self):
        self.headval = None

    def printlist(self):
        printvalue = self.headval
        while printvalue is not None:
            print(printvalue.curr)
            printvalue = printvalue.next

    def insertEnd(self,value):
        newNode = Node(value)
        if self.headval is None:
            self.headval = newNode
            return
        last = self.headval
        while last.next:
            last = last.next
        last.next = newNode
    
    def insertHead(self, value):
        newnode = Node(value)

        newnode.next = self.headval
        self.headval = newnode
    
    def insertBetween(self, value, prev, next):
        pass
    def remove(self, value):
        pass

def main():
    print("creating a linked list...")
    slist = SLinkedlist()

    slist.insertEnd(5)
    slist.insertEnd(2)
    slist.insertEnd(1)
    slist.insertEnd(3)

    slist.printlist()

if __name__ == "__main__":
    main()