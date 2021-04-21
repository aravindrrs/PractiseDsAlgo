# children index 2n, 2n+1 if the index starts at 1 or 2n+1, 2n+2 if the index starts at 0, parent index = floor(n/2)

class binHeap:
    def __init__(self):
        self.heapList=[0] #this is our list
        self.currentSize=0 #keep track of the list currentSize

#Insert method - heaps get inserted at the top of the heap, which is the last position in the LinkedList
    def insertItem(self,item):
        self.heapList.append(item)
        self.currentSize = self.currentSize+1
        percUp(self.currentSize)#logic to percolate up if necessary

    def percUp(self,i):  #this method is based on index ,not the actual element, so percUp is an operation on the element index
        while i//2 >0:
                if self.heapList[i] < self.heaplist[i//2]:
                    temp= self.heaplist[i//2]
                    self.heaplist[i//2]= self.heaplist[i]
                    self.heaplist[i] =temp
                i = i//2
#delete the min value from the heap and restructure the heap

    def  delMin(self):
       deletedValue= self.heaplist[1]
       self.heaplist[1] = self.heaplist[self.currentSize]
       self.heaplist.pop()
       self.currentSize = self.currentSize - 1
       self.percDown(1) #logic to percDown because you just replaced the first value in the list with the last value
       return deletedValue

    def percDown(self,i):
      while i*2 <= self.currentSize:
          m = self.minChild(i)
          if self.heapList[i] > self.heapList[m]:
              temp = self.heapList[i]
              self.heapList[i] = self.heapList[m]
              self.heapList[m] = temp
          i = m

    def minChild(self,i):
      #checking  a corner case where the tree has only one root and one child
      if i*2 + 1 >self.currentSize:
          return i*2

      elif self.heapList[2*i] < self.heapList[2*i+1]:
          return 2*i
      else:
          return 2*i+1


    def buildHeapfromList (self,givenList):
       self.currentSize = len(givenList)
       i = self.currentSize // 2
       self.heapList = [0]+givenList
       while i >0:
           self.percDown(i)
           i = i-1
       return self.heapList


l= [12,6,8,1,99,3,5,7]

bh = binHeap()
print (bh.buildHeapfromList(l))
