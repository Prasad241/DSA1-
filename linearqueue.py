# #Linear Queue Using Linked List
# class Node:
#     def __init__(self, value):
#         self.data=value
#         self.next=None

# class LQueue:
#     def __init__(self):
#         self.front=self.rear=None

#     def enqueue(self, new_node):
#         if self.rear:
#             self.rear.next=new_node
#             self.rear=new_node
#         else:
#             self.front=self.rear=new_node
    
#     def dequeue(self):
#         if self.front:
#             temp=self.front
#             self.front=self.front.next
            
#             if  self.front==None:
            
#                 self.rear=None
#             temp=None   
#         else:
#             print("Queue is empty!")
    
#     def print(self):
#         temp=self.front
        
#         while temp:
#             print(temp.data,"->")
#             temp=temp.next
#         print()
# que=LQueue()
# que.enqueue(Node(10))
# que.enqueue(Node(20))
# que.enqueue(Node(55))
# que.enqueue(Node(101))
# que.enqueue(Node(88))
# que.print()
# que.dequeue()
# que.print()
# que.dequeue()
# que.dequeue()
# que.dequeue()
# que.dequeue()
# que.print()
# que.dequeue()
# que.enqueue(Node(23))
# que.enqueue(Node(45))
# que.print()
class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None


    def isEmpty(self):
        if self.front == None:
            return True


    def enque(self,data):

        node = Node(data)

        if self.front ==None:
            self.front = self.rear = node
            return

        self.rear.next = node
        self.rear = node


    def deque(self):
        if self.isEmpty():
            print("Queue is empty!")
            return

        t= self.front
        self.front = self.front.next
        if self.front == None:
            self.rear = None
            print("Queue is now empty!")
        t = None

    def print(self):
        if self.isEmpty():
            print("Queue is empty!")
            return

        t = self.front
        print("Queue elements: ")
        while t:
            print(t.data,end=" ")
            t=t.next
        print()



q = Queue()
print(q.isEmpty())
q.enque(10)
q.enque(20)
q.enque(30)
q.print()
q.enque(40)
q.print()
q.deque()
q.print()
q.deque()
q.print()
q.deque()
q.print()
q.deque()