Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
    P(i,i) = True
    P(i, i+1) = Si = Si+1
    P(i, j) = P(i+1, j-1)^ Si == Sj
边界情况即为子串长度为 1 或 2 的情况。我们枚举每一种边界情况，并从对应的子串开始不断地向两边扩展。如果两边的字母相同，我们就可以继续扩展，

例如从 P(i+1,j-1)P(i+1,j−1) 扩展到 P(i,j)P(i,j)；如果两边的字母不同，我们就可以停止扩展，因为在这之后的子串都不能是回文串了。

聪明的读者此时应该可以发现，「边界情况」对应的子串实际上就是我们「扩展」出的回文串的「回文中心」。

方法二的本质即为：我们枚举所有的「回文中心」并尝试「扩展」，直到无法扩展为止，此时的回文串长度即为此「回文中心」下的最长回文串长度。我们对所有的长度求出最大值，即可得到最终的答


Solution 1: Method based on center line enumeration

class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        if not s:
            return ""
            
        longest = ""
        for middle in range(len(s)):
            
            odd = self.find_palindrome_from(s, middle, middle)
            even = self.find_palindrome_from(s, middle, middle + 1)
            longest = max(longest, odd, even, key = len)
            
        return longest
                
    def find_palindrome_from(self, string, left, right):
        while left >= 0 and right < len(string) and string[left] == string[right]:
            left -= 1
            right += 1
            
        return string[left + 1:right]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Check if s is None or ""
        if not s:
            return ""
        
        longest = ""
        for middle in range(len(s)):
            # Expand from the center, two case 
            odd = self.findPalindrome(s, middle, middle)
            if len(odd) > len(longest):
                longest = odd
            even = self.findPalindrome(s, middle, middle + 1)
            if len(even) > len(longest):
                longest = even
            #longest = max(longest, odd, even, key=len)
        return longest
    
    def findPalindrome(self, s, left, right):
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break
            left -= 1
            right += 1
        
        return s[left+1:right]
        
  # TC: o(N**2), the length of string is 1 and 2 which has n and n - 1. Each centre will expand O(N) times
  # SC: O(1)
  
 Solution 2:
class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        max_length = 1
        start = 0
        
        dp = [[False] * length for _ in range(length)]
        
        for i in range(length):
            dp[i][i] = True
            
        for i in range(length-1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                max_length = 2
                start = i
    
        for new_len in range(3, length + 1):
            for left in range(length - new_len + 1):
                right = left + new_len - 1
                
                if dp[left + 1][right - 1] and s[left] == s[right]:
                    dp[left][right] = True
                    # 更新答案
                    if max_length < new_len:
                        max_length = new_len
                        start = left
                        
        return s[start: start + max_length]
