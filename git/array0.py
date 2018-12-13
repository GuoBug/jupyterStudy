import numpy as np

a = np.array([[1,2,3],
             [2,3,4]])

print (a)
a.shape = (1,6)
print (a)

b = np.zeros((3,4),dtype = np.int16)

print (b)
print (b.ndim)
print (b.shape)
print ('size:',b.size)

b.shape = (2,6)
print (b)

dt = np.dtype(np.uint64)
print(dt)

x = np.linspace(1,10,10,dtype=int)
print (x)
