Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
 

Constraints:

-231 <= x <= 231 - 1

```Python
class Solution:
    def reverse(self, x: int) -> int:
        y = int(str(x)[::-1]) if x>= 0 else -int(str(x)[:0:-1])
        return y if -2**31 < y < 2**31-1 else 0
```

```
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        m = -1 if x < 0 else 1
        x = x*m
        
        n = 0
        while x > 0:
            n = (n * 10) + (x % 10)
            x = x // 10
        
        if n > 0x7FFFFFFF:
            return 0

        return n*m
```

