#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
O(n), The loop runs n number of times.

b)
O(n log n), The outer loop runs n number of times and the inner loop runs (i+1) number of times.

c)
O(n), tThis is recursive, so repeats on itself until bunnies is 0 that means it performs the operation as many times as the number of bunnies and returns one number
## Exercise II
By using O(log n), we begin in the middle of the floors (range of n) while drop an egg & if egg breaks, we go down a floor. By skipping the floors that above and below that breaking the egg.

```
for f in range(0, len(n) // 2):
    if egg_breaks(f):
        return f
```

