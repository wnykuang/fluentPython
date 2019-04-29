from array import array
from random import random

floats = array('d', (random() for i in range(10**7)))
#Create an array of double-precision floats with typecode 'd' from 
#any iterable object

print(floats[-1])

fp = open('floats.bin', 'wb')
floats.tofile(fp)
#save the array to a binary file
fp.close

floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
#read 10 m numbers from the binaty file
fp.close()


print(floats2[-1])

print(floats2 == floats)