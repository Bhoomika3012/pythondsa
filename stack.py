class stack_array:
    def __init__(self):
        self.data=[]

    def push(self,e):
        self.data.append(e)

    def len(self):
        return len(self.data)

    def isempty(self):
        return len(self.data)==0

    def pop(self):
        if self.isempty():
            print("stack is empty")
            return
        return self.data.pop()
    def top(self):
        if len(self.data)==0:
            print("list is emety")
        return self.data[-1]

    def display(self):
        i=len(self.data)-1
        while i>=0:
            print(self.data[i])
            i-=1
    
s=stack_array()
s.push(10)
s.push(20)
s.push(30)
s.display()
print("length of the stack",s.len()) 
print("stack is empty r not","-->",s.isempty())
print("returns pop ele","-->",s.pop())
s.display()
print(s.top())
s.display()