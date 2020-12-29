"""Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true
"""

import collections
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        c = collections.Counter(s)
        count = 0
        for i in c.values():
            if len(s) % 2 == 0:
                if i % 2 != 0:
                    return False
            else:
                if i % 2 != 0:
                    count += 1
        return count <= 1 
        
import collections
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        c = collections.Counter(s)
        count = 0
        for i in c.values():
            if i % 2 != 0:
                count += 1
        return count <= 1 
