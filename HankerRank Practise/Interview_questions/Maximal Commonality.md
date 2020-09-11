```
class Solution:
    def maxCommon(self, s):
        left = {}
        right = {}
        ans = 0
        
        for index,char in enumerate(s):
            left[char] += 1
            right[char] -= 1
            
            ans = max(ans, sum((left & right).values()))
        
        return ans

s = Solution()
print(s.maxCommon('abcdedeara'))
```
