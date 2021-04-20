class newnode:
      def __init__(self,root):
          self.root=root
          self.leftchild=None
          self.rightchild=None

      def insertleft(self,leftvalue):
         if self.leftchild==None:
            self.leftchild = newnode(leftvalue)
         else:
            l=newnode(leftvalue)
            l.leftchild = self.leftchild
            self.leftchild=l


      def insertright(self,rightvalue):
          if self.rightchild==None:
             self.rightchild=newnode(rightvalue)

          else:
             r=newnode(rightvalue)
             r.rightvalue=self.rightchild
             self.rightchild=r


      def rootreplace(self,newroot):
           self.root = newroot
      def getroot(self):
           return self.root
      def getleftchild(self):
           return self.leftchild
      def getrightchild(self):
           return self.rightchild

n=newnode('a')
print(n.root)
n.insertleft('b')
n.insertright('c')
print (n.getleftchild().root)
print (n.getrightchild().root)
