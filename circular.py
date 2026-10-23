# 
class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

class CQ:

    def __init__(self):
        self.front = None
        self.rear = None


    def isEmpty(self):
        if self.front == None and self.rear == None:
            return True


    def enque(self,data):

        node = Node(data)

        if self.front ==None:
            self.front = self.rear = node
            return

        self.rear.next = node
        self.rear = node
        self.rear.next = self.front


    def deque(self):
        if self.isEmpty():
            print("Queue is empty!")
            return

        if self.front == self.rear: # Updated of C Q
            t= self.front
            self.front = self.rear = None
            print("Queue is now empty!")
            t= None
            return
        t= self.front
        self.front = self.front.next
        self.rear.next = self.front
        if self.front == self.rear: # Updated of C Q
            self.front = self.rear = None
            print("Queue is now empty!")
        t = None

    def print(self):
        if self.isEmpty():
            print("Queue is empty!")
            return

        t = self.front
        print("Queue elements: ")
        while True:
            print(t.data,end=" -> ")
            t=t.next
            if t == self.front:
                break
        print("FRONT")



q = CQ()
print(q.isEmpty())
q.enque(10)
q.enque(20)
q.enque(30)
q.print()
q.enque(40)
q.print()
q.deque()
q.deque()
q.print()