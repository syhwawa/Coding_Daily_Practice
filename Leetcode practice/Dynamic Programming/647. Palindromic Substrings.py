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
    # Space Complexity : O(1)
 

class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        dp = [[0] * len(s) for _ in range(len(s))]
        """
        属于动态规划的解法，令dp[j][i]表示子串s[j,i]是否是回文串，状态转移如下：

        当i=j时，单个字符肯定是回文串，可以看成奇数回文串的起点
        当s[i]=s[j]且i-j=1，则dp[j][i]是回文串，可以看成偶数回文串的起点
        当s[i]=s[j]且dp[j+1][i-1]是回文串，则dp[j][i]也是回文串
        其他情形都不是回文串
        其中条件1、2、3是可以合并的：

        当s[i]=s[j]时，dp[j+1][i-1]是回文串或i-j<2，则dp[j][i]也是回文串

        """
        
        for i in range(len(s)):
            for j in range(i + 1):
                if s[i] == s[j] and (i - j < 2 or dp[j+1][i-1]):
                    dp[j][i] = 1

                count += dp[j][i]
        return count
        # TC: O(N**2)
        # SC: O(N**2)
