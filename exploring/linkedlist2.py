
class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

class slinkedlist:
    def __init__(self):
        #the head node is used as a placeholder
        self.head = Node()

    def append(self,node):
        new_node = Node(node)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def getlength(self):
        cur = self.head
        length = 0
        while cur.next != None:
            cur = cur.next
            length += 1
        return length
    
    def display(self):
        elem = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elem.append(cur.value)
        print(elem)

    def get(self,index):
        if index > self.getlength():
            print("ERROR")
            return None
        cur_id = 0
        cur = self.head

        while True:
            cur = cur.next
            if cur_id == index:
                return cur.value
            else:
                cur_id += 1
        
    def erase(self,index):
        if index > self.getlength():
            print("ERROR")
            return None
        
        cur_id = 0
        cur = self.head

        while True:
            last_node = cur # previous node 
            cur = cur.next # current node
            cur1 = cur.next # next node 

            if cur_id == index:
                last_node.next = cur1 #joins the previous node with the next node, skip the current node 
                return
            cur_id += 1

def main():
    my_list = slinkedlist()
    my_list.display()
    my_list.append(1)
    my_list.append(0)
    my_list.append(4)
    my_list.append(10)
    my_list.display()
    print("length is ----->", my_list.getlength())

    print("value at index 3 ----->", my_list.get(3))

    print("erasing value at index 3...")
    my_list.erase(3)
    my_list.display()

if __name__ == "__main__":
    main()