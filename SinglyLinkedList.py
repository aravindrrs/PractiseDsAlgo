

class Node:

      def __init__(self,value):
          self.value= value
          self.nextnode=None

a= Node(1)
b= Node (2)
c=Node('C')

a.nextnode = b  #pointer, you are assigning a class instance,b, as the value to this variable self.nextnode or a.nextnode
b.nextnode =c   #pointer

print (a.value)
print (a.nextnode)
print (a.nextnode.value)
print (b.nextnode.value)
