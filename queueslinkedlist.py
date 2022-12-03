


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
       
class queuelinkedlist:
    def __init__(self):
        self.first=None
        self.last=None
        
    def enque(self,data):
        new_node=Node(data)
        if self.first==None:
            self.first=new_node
        else:
            self.last.next=new_node
        self.last=new_node 
        
    def deque(self):
        if self.first==None:
            print("queue is empty")
        else :
            e=self.first.data
            self.first=self.first.next
            return e
            
          
    def display(self):
        p=self.first
        while p:
            print(p.data)
            p=p.next
l=queuelinkedlist()
#l.enque(1)
#l.enque(2)
#l.enque(3)
#l.display()
print("deque element",l.deque())
l.display()
print("deque element",l.deque())
l.enque(4)
l.enque(5)
l.display()
print("deque element",l.deque())