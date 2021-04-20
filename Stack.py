#Stack Implementation

#pop, peek, return size, empty check , push

class Stack :
        def __init__(self):
            self.container = [] #initiating a list which is my stack holder

        def push (self, item):
            return self.container.append(item)

        def sizecheck(self):
            return len(self.container)

        def isempty(self):
            if self.sizecheck() == 0:
               return True
            return False

        def pop(self):

            if not self.isempty:
               raise Exception ("List is empty")

            return self.container.pop()

        def peek(self):

            if not self.isempty:
                raise Exception ("List is empty")

            return self.container[-1]

s=Stack()
print (s.isempty())
s.push(1)
s.push(100)
s.push(200)
s.push(1500)
s.push('thousand')
print (s.isempty())
print (s.container)
s.pop()
print (s.container)
print (s.peek())
print (s.sizecheck())
