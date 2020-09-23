Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.

Example
```
For sequence = [1, 3, 2, 1], the output should be
almostIncreasingSequence(sequence) = false.

There is no one element in this array that can be removed in order to get a strictly increasing sequence.

For sequence = [1, 3, 2], the output should be
almostIncreasingSequence(sequence) = true.
```
You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].

https://app.codesignal.com/arcade/intro/level-2/2mxbGwLzvkTCKAJMG/solutions

```Python
def almostIncreasingSequence(sequence):
    count1 = 0
    count2 = 0
    for i in range(len(sequence) - 1):
        if sequence[i+1] <= sequence[i]:
            count1 += 1
            
    for i in range(len(sequence) - 2):
        if sequence[i+2] <= sequence[i]:
            count2 += 1
            
    return( (count1 <= 1) & (count2 <= 1) )

```
