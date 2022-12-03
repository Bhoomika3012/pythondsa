class queuearray:
    def __init__(self):
        self.data=[]

    def enqueue(self,v):
        self.data.append(v)

    def len(self):
        return len(self.data)

    def first(self):
        return (self.data[0])

    def deque(self):
        if len(self.data)==0:
            print("queue is empty")
        else:
            print(self.data.pop(0))

    def display(self):
        i=len(self.data)-1
        while i>=0:
            print(self.data[i])
            i-=1

a=queuearray()
a.enqueue(10)
a.enqueue(20)
a.enqueue(30)
a.display()
print("length of array","-->",a.len())
print("first element in array","-->",a.first())
a.deque()