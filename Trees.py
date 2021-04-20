def root(r):
    return [r,[],[]]

def leftchild (root,newleftchild):
    leftnode = root[1]
    if leftnode ==[]:
       leftnode = [newleftchild,[],[]]
       root[1] = leftnode
       return root
    else:
      leftnode = [newleftchild,root[1],[]]
      root[1] = leftnode
      return root



def rightchild(root,newrightchild):
    rightnode = root[2]
    if rightnode == []:
        rightnode = [newrightchild,[],[]]
        root[2] = rightnode
        return root
    else:
      rightnode = [newrightchild,root[2],[]]
      root[2] = rightnode
      return root

def getroot(root):
    return root[0]
def setroot(root,newroot):
    root[0]=newroot
def getleftchild(root):
    return root[1]
def getrightchild(root):
    return root[2]

rootnode = root(3)
print(rootnode)



print(leftchild(rootnode,4))
print(leftchild(rootnode,5))
print (rightchild(rootnode,6))
print (rightchild(rootnode,7))
l=getleftchild(rootnode)
print (l)
setroot(l,9)

print(rootnode)
