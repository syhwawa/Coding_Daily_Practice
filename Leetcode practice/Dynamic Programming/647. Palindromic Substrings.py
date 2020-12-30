Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

#Solution 1: Expansion from centre
class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        
        ans = 0
        for middle in range(len(s)):
            # Expand from the center, two case 
            ans  += self.findPalindromic(s, middle, middle)
            ans  += self.findPalindromic(s, middle, middle + 1)
        
        return ans
    
    #find the palindromic string
    def findPalindromic(self, s, left, right):
        count = 0
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break
            count += 1
            left -= 1
            right += 1
        
        return count
    
    # Time Complexity : O(N**2)
    # Space Complexity : O(N**2)
    
