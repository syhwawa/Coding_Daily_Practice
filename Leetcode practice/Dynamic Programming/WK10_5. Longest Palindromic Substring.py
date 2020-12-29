Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"


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
       
   
