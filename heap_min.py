import unittest
# This class is a example of a objetc that can be storage in the heap
# it can be expanded to include more attributes and methods 
class Node:

  def __init__(self, value): #constructor
    self.value = value
  
  def get_value(self): #method to retun the value
    return self.value

# This class implements all methods of a min heap
# The attribute value of the node class is the key of the heap 

class Heap_min:

  def __init__(self): #constructor
    self.heap = [] #creating a list that will storage the nodes

  def insert(self,node): #method to insert a node in the heap
    self.heap.append(node)
    self.heapifyup(len(self.heap)-1)
    return True
  
  def extract(self): #method to extract a node in the heap
    if(len(self.heap) > 0):
      node = self.heap.pop(0)
      if(len(self.heap) > 0):
        self.heap[0] = self.heap[len(self.heap) - 1];
        self.heapifydown(0)
      return node
    else:
      raise IndexError("There's no more elements in the heap")

  def top(self): #method to return the node in the heap's top
    if(len(self.heap) > 0):
      return self.heap[0]
    else:
      raise IndexError("There's no more elements in the heap")
 

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
    while ((self.left(index) < len(self.heap) and self.heap[index].get_value() > self.heap[self.left(index)].get_value) or (self.right(index) < len(self.heap) and self.heap[index].get_value() > self.heap[self.right(index)].get_value())):
      if (self.right(index) < len(self.heap) and self.heap[self.right(index)].get_value() < self.heap[self.left(index)].get_value):
        self.heap[index] , self.heap[self.rigth(index)] = (self.heap[self.rigth(index)], self.heap[index]) 
        index = self.right(index)
      else:
        self.heap[index] , self.heap[self.left(index)] = (self.heap[self.left(index)], self.heap[index])
        index = self.left(index);

class Heap_min_test(unittest.TestCase):
  def test_node(self): #tesing Heap_min class

    node1 = Node(2) #creating a node
    node2 = Node(3) #creating a node

    self.assertEqual(node1.get_value(), 2) #check get_value method
    self.assertEqual(node2.get_value(), 3) #check get_value method

  def test_heap(self):  #tesing node class
    
    node1 = Node(2) #creating a node
    node2 = Node(3) #creating a node

    h =  Heap_min()  # creating a instance of heap
    
    self.assertTrue(h.insert(node1)) #check insert method
    self.assertTrue(h.insert(node2)) #check insert method

    self.assertEqual(h.top().get_value(),2) #check top method
    self.assertEqual(h.extract().get_value(),2) #check extract method

    self.assertEqual(h.top().get_value(),3) #check top method
    self.assertEqual(h.extract().get_value(),3) #check extract method

    with self.assertRaises(IndexError) as ie: 
       h.top() #check top method raise

    with self.assertRaises(IndexError): 
      h.extract() #check extract method raise


if (__name__ == "__main__"):
  unittest.main()