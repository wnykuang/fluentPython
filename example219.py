import bisect
import random

SIZE = 7

random.seed(1729)

myList = []
for i in range(SIZE):
    newItem = random.randrange(SIZE * 2)
    bisect.insort(myList, newItem)
    print("{} -> {}".format(newItem, myList))