from node import Node

# Michael / C14230113
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
        index = -1
        temp = self.head
        print(f"{index}. {temp.get_judul()} ({temp.get_genre()}) by {temp.get_artist()}")
        temp = temp.next
        while temp:
            index -= 1
            print(f"{index}. {temp.get_judul()} ({temp.get_genre()}) by {temp.get_artist()}")
            if temp.next == None:
                break
            else:
                temp = temp.next