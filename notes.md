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

Difference between bisect and bisect_left:
   bisect_right returns an insertion point after the exiting item.
bisect_left returns the position of the existing item.