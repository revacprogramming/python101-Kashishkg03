class Menu():
  """fill in class definition here"""
  def __init__(self,item,rate):
    self.item=item
    self.rate=rate
  
  def __add__(self,other):
    return (self.item +str(self.rate), other.item+str(other.rate))

m = Menu("idly", 10)
n = Menu("vada", 20) # Hint: operator overloading special methods (__add__, __sub__, etc.)
sum =m+n

print(m )  # should print the menu properly
for i in sum:
  print(i)
