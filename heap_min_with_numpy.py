import numpy as np
# This class is a example of a objetc that can be storage in the heap
# it can be expanded to include more attributes and methods 
class Node:

  def __init__(self, value): #constructor
    self.value = value 
  
  def get_value(self): #method to retun the value
    return self.value

#This class implements all methods of a min heap
#The attribute value of the node class is the key of the heap 

class Heap_min:

  def __init__(self): #constructor
    self.max  = 100
    self.heap = np.zeros([self.max], dtype='O') #creating a ndarray that will storage the nodes
    self.size = 0

  def insert(self,node): #method to insert a node in the heap
    if (self.size < self.max):
        self.heap[self.size] = node;
        self.heapifyup(self.size);
        self.size +=1;
        return True
    print("ERROR - The heap is full ")
    exit(1)
  
  def extract(self): #method to extract a node in the heap
    if (self.size > 0):
      node = self.heap[0]
      self.heap[0] = self.heap[self.size - 1];
      self.size -= 1
      self.heapifydown(0)
      return node
    print("ERROR - There's no more elements in the heap")
    exit(1)

  def top(self): #method to return the node in the heap's top
    if (self.size != 0):  
      return self.heap[0]
    else:
      print("ERROR - There's no more elements in the heap")
      exit(1)

  def parent(self, index): #method to return the index of the parent node
    return (index-1)//2
  
  def left(self, index): #method to return the index of the left node
    return 2 * index + 1
  
  def right(self, index): #method to return the index of the right node
    return 2 * index + 2

  def heapifyup(self,index): #method to heapify the tree when a node is inserted
   while(index > 0 and self.heap[index].get_value() < self.heap[self.parent(index)].get_value()):
      self.heap[index] , self.heap[self.parent(index)] = (self.heap[self.parent(index)], self.heap[index]) 
      index = self.parent(index)
    
  def heapifydown(self, index): #method to heapify the tree when a node is extracted
    while ((self.left(index) < self.size and self.heap[index].get_value() > self.heap[self.left(index)].get_value) or (self.right(index) < self.size and self.heap[index].get_value() > self.heap[self.right(index)].get_value())):
      if (self.right(index) < self.size and self.heap[self.right(index)].get_value() < self.heap[self.left(index)].get_value):
        self.heap[index] , self.heap[self.rigth(index)] = (self.heap[self.rigth(index)], self.heap[index]) 
        index = self.right(index)
      else:
        self.heap[index] , self.heap[self.left(index)] = (self.heap[self.left(index)], self.heap[index])
        index = self.left(index);

def main():
  #creating two nodes
  n = Node(2)
  nn = Node(3)

  # creating a instance of heap
  h =  Heap_min() 

  # #testeting the three main functions of the heap
  h.insert(n)
  h.insert(nn)
  print("top of the heap", h.top())
  print("extracting the top", h.extract().get_value())
  print("extracting the top", h.extract().get_value())

  ## testing the try catch
  print("extracting the top", h.extract())
  print("topo da pilha", h.top())

if (__name__ == "__main__"):
  main()

