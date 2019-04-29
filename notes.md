### Augmented Assignment with Sequences

+= is impelmented by __iadd__ which stands for inplace addition.
*= is impelmented by __imul__ which stands for inplace multiplication.
 
Dangeras case
```python
t = (1,2, [30, 40])
t[2] += [50,60]
#it will raise a exception and the result will be 
#t == (1,2,[30,40,50,60])
```

- *Don't* putting mutable items in tuples.
- Augmented assignment is not an atomic operation - we just saw it throwing an exception after doing part of its job.

### list.sort and the sorted Built-In function
- list.sort method sorts a list in place.
- Functions or methods that change an object in-place should return __None__ to make it clear to the caller that the object itself was changed, and no new object was created.

## Managing Ordered Sequences with bisect

### Difference between bisect and bisect_left:
   bisect_right returns an insertion point after the exiting item.
bisect_left returns the position of the existing item.

### Inserting with bisect.insort
insort(seq, item) inserts item into seq so as to keep seq in ascending order.
   
There is also insort_left uses bisect_left.

### When a List Is Not the Answer

If you need to store 10 million floating-point values, an array is much more efficient bacause an arrayy does not acutally hold full-fledged float objects, but only the packed bytes representing their machine values - just like an array in the C language.   
On the other hand, if you are constantly adding and removing items from the ends of a list as a FIFO or LIFO data structure, a deque (double-ended queue) works faster.

#### Arrays
If the list will only contain numbers, an ```array.array``` is more efficient than a ```list```: it supports all mutable sequence operations, and additional methods for fast loading and saving such as ```.frombytes``` and ```.tofile```.   
detail example in example220.py

##### Memory Views
Using notation similar to the ```array``` module, the ```memoryview.cast``` method lets you change the way multiple bytes are read or written as units without moving bits around(just like the C cast operator).memoryview.cast returns yet another memoryview object, always sharing the same memory.

#### Deques and other queues
The ```list.pop(0)``` is an O(n) operation since the entire list must be shifted.    
The class ```collections.deque``` is a thread-safe double-ended queue deisigned for fast inserting and removing from both ends.    
