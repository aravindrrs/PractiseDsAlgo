class DllNode:
    def __init__(self,value):
        self.value=value
        self.previousnode=None
        self.nextnode=None

a=DllNode(1)
b=DllNode(2)
c=DllNode(3)
d=DllNode(4)

b.previousnode =a
b.nextnode =c
print (b.value)
print (b.previousnode.value)
print (b.nextnode.value)
