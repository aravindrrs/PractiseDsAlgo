class Queue:

    def __init__(self):
        self.container=[]

    def isempty(self):
        return self.container == [] #put the condition that will return True or if you want you can put the condition that returns false. Basically return = default

    def enqueue (self,item):
        return self.container.insert(0,item)

    def dequeue (self):
        return self.container.pop()

q= Queue()

print  (q.isempty())
q.enqueue(1)
q.enqueue(100)
q.enqueue(200)
q.enqueue(1500)
q.enqueue('thousand')

print (q.container)

q.dequeue()

print (q.container)
