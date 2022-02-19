"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
  if(x<=1):
      return x
  else:
      return foo(x-1) + foo(x-2)
print(foo(10))
print(foo(0))
print(foo(1))

   

def longest_run(mylist, key):
  
  prev = None
  size = 0
  max_size = 0
  for i in mylist:
    if i == prev and prev == key:
      size += 1
      if size > max_size:
        max_size = size 
    else:
      size = 0
      prev = i
      
  return max_size+1

      

class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
  right = None
  left = None
  length = len(mylist)//2
  prev = None
  left_size = 0
  right_size = 0
  longest_size = left_size + right_size
  if len(mylist) = 1 and mylist[0] = key:
    return mylist[0]
  else:
    for i in mylist:
      left = mylist[:length]
      right = mylist[length:]
      for i in left:
        if i = prev and prev = key:
          left_size+=1
      for i in right:
        if i = prev and prev = key:
          right_size+=1
  return longest_size 

    




## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3


