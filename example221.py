import array

numbers = array.array('h', [-2, -1, 0, 1, 2])
#'h' stands for short number
memv = memoryview(numbers)
print(len(memv))
print(memv[0])
print(memv)#will print out the address of the array, wow.
memvOct = memv.cast('B')
#Create memvOct by casting the elements of memv to typecode 'B'
#(unsigned char)
print(memvOct.tolist())
memvOct[5] = 4
print(numbers)