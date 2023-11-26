class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length ==0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length +=1

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head

        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -=1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self , value):
        new_node = Node(value)
        if self.length ==0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        else:
            if self.length ==1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.next = None

            self.length -=1
            return True

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
        
    def insert_anyposition(self, value, index):
        if self.length < index:
            print("Index is out of linked list")

        else:
            new_node = Node(value)
            temp = self.head
            while(temp.next):
                temp =  temp.next
                index -=1
                if index ==1:
                    temp_next = temp.next 
                    temp = new_node
                    temp.next = temp_next
                    
    def set_value(self, index, value):
        temp = self.get(index)
        print(temp)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0  and  index > self.length:
            return None
        if index ==0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)

        temp = self.get(index -1)
        new_node.next = temp.next
        temp.next = new_node
        self.length +=1
        return True
    
    def remove(self, index):
        if index < 0  and  index > self.length:
            return None
        if index ==0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        
        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -=1
        return temp 
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


    def middle(self):
        mid = self.length//2
        result =self.get(mid)
        print("middle",result.value)

    





        

        
        

        
        

        
        


my_link_list = LinkedList(1)
my_link_list.append(4)
my_link_list.append(4)
my_link_list.append(5)
# my_link_list.pop()
# my_link_list.pop()
# my_link_list.append(4)
# my_link_list.prepend(8)
# my_link_list.pop_first()
# print(my_link_list.get(3))
my_link_list.set_value(1,8)
my_link_list.insert(0,12)
my_link_list.print_list()
# my_link_list.remove()

my_link_list.print_list()
my_link_list.reverse()
# print("/n")
# my_link_list.print_list()
my_link_list.middle()

