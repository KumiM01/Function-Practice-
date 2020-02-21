def two_max(x,y):
  if x > y:
    return x
  else:
    return y
    
def three_max (x,y,z):
  return two_max (x,two_max (y,z))
  
print (three_max(10,50, 20))