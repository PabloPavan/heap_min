import unittest

def sum(x,y):
    return x + y

def multiply(x, y):
  return x * y

def divide(x, y):
  if (y == 0):
    raise ValueError("Can not divide by zero!")
  return x / y

class MyTest(unittest.TestCase):
    def test_sum (self):
      self.assertEqual(sum(3,3), 6) #this is inline test
    def test_multiply(self): 
      result = multiply(3,3) # this is using one variable to gather the result and then test
      self.assertEqual(result, 9)
    def test_divide(self):
      self.assertEqual(divide(3,3), 1) #this is inline test
      #testing Raises
      self.assertRaises(ValueError, divide, 3, 0) #this is inline test
      with self.assertRaises(ValueError): # this is using context
        divide(3,0)

if (__name__ == "__main__"):
  unittest.main()