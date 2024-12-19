class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.head = None

    def push(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head == None:
            return None
        else:
            popped = self.head
            self.head = self.head.next
            return popped
        
    def is_empty(self):
        return self.head is None
        
    def print_stack(self):
        temp = self.head
        while temp:
            if temp.next != None:
                print(temp.get_judul(), end = ",")
                temp = temp.next
            else:
                print(temp.get_judul(), end = "")
                break
        print()