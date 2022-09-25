class Node:
    def __init__(self, data = None, next=None): 
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):  
        self.head = None    
  
    def insert(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def InsertAnyposition(self, data, position):
        newNode = Node(data)
        if(self.head):
            count=1
            if count == position:
                temp= self.head
                self.head = newNode
                current=self.head
                current.next = temp
            else:
                current = self.head
            while(current.next):
                temp=current.next
                count+=1
                if count==position:
                    current.next = newNode
                    current.next.next=temp
                else:
                    current= temp
            if position > count:
                print('Position is out side the linklist')
        else:
            print('Linklist is Empty')

    def delete(self):
        if(self.head):
            current = self.head
            if current.next:
        
                while(current.next):
                    if current.next.next:
                        current=current.next
                    else:
                        current.next=None
            else:
                self.head = None
        else:
            print("linklist is already Empty")


  
    def printLL(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next
    
    def deleteFromAnyPosition(self,position):
        if(self.head):
            count = 1
            if count ==position:
                temp= self.head.next    
                self.head = None
                self.head = temp
                current = self.head
            else:
                current = self.head
            if current!= None:
                while(current.next):
                    count+=1
                    if count ==position:
                        temp = current.next.next
                        current.next = None
                        current.next = temp
                    else:
                        current = current.next
                if count < position:
                    print("Position is out of linklist")
        else:
            print("linklist is already Empty")



LL = LinkedList()
LL.insert(3)
LL.insert(4)
LL.insert(5)

LL.delete()
LL.InsertAnyposition(9,1)
LL.insert(7)
LL.InsertAnyposition(11,1)
LL.InsertAnyposition(23,3)
LL.delete()
LL.deleteFromAnyPosition(3)
LL.printLL()