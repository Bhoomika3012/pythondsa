class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class stacklist:
    def __init__(self):
        self.top=None

    def push(self,data):
        new_node=Node(data)
        if self.top==None:
            self.top=new_node
        else:
            new_node.next=self.top
            self.top=new_node

    def pop(self):
        if self.top==None:
            print("stack is empty")
        else:
            temp=self.top.next
            self.top=temp
            temp=None

    def stacktop(self):
        if self.top==None:
            print("stack is empty")
        else:
            print("[",self.top.data,"]")

    def display(self):
        p=self.top
        while p!=None:
            print(p.data)
            p=p.next

sl=stacklist()
sl.push(10)
sl.push(20)
sl.push(30)
sl.display()
sl.pop()
sl.display()
sl.stacktop()
