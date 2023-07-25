import numpy
for num in range(1,10):
  x = int(num * "1")
  for i in range(2,11):
    x += int (numpy.base_repr(num, base=i))
  print(x)
