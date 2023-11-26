class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.height = 1

    def print_queue(self):
        temp = self.first
        while(temp):
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.height ==0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.height +=1

    def dequeue(self):
        if self.height == 0:
            return None
        temp = self.first
        if self.height ==1:
            self.first = None
            self.last = None
        else:    
            self.first = self.first.next
            temp.next = None
        self.height -= 1
        return True


my_queue = Queue(5)

my_queue.dequeue()
my_queue.print_queue()

