
#this class will receive the head of a list 
#reverse the starting from the beginning 
class ReverseLinkedList:
    def __init__(self):
        pass
    def reverse(self,head):
        # print("memory address of node is at -->", head)
        #points to the address of the next value 
        curr = head.next
        previous = None
        while True:
            temp_curr = curr.next
            curr.next = previous
            previous = curr
            if not temp_curr:
                break
            curr = temp_curr

        print(curr.value)
        return curr
        #print the reverse linklist 
        # elem = []
        
        # while curr != None:
        #     elem.append(curr.value)
        #     curr = curr.next
        # print(elem)


class Node:
    def __init__(self, Value = None):
        self.value = Value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()
    def append(self, node):
        new_node = Node(node)
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node
    def display(self):
        elem = []
        curr = self.head
        while curr.next != None:
            curr = curr.next
            elem.append(curr.value)
        print(elem)

    def display_reversed(self,node):
        elem = []
        
        while node != None:
            elem.append(node.value)
            node = node.next
        print(elem)

def main():
    # user gives input 1 2 3 4 5 6 etc 
    li = input()
    inp_nodes = li.split(" ")

    linklist = LinkedList()
    for i in inp_nodes:
        linklist.append(i)
    reverse_list = ReverseLinkedList()
    head = reverse_list.reverse(linklist.head)
    linklist.display_reversed(head)

if __name__ == "__main__":
    main()