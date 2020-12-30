"""
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
 

Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
"""

#对于任意字符串，如果头尾字符相同，那么字符串的最长子序列等于去掉首尾的字符串的最长子序列加上首尾；
#如果首尾字符不同，则最长子序列等于去掉头的字符串的最长子序列和去掉尾的字符串的最长子序列的较大者

#Assume dp[i][j] is the longest length of palindromic str between str i to str j 
the transformation function is 
dp[i][j] = dp[i+1][j-1] + 2 if (s[i] == s[j])
dp[i][j] = max(dp[i+1][j], dp[i][j-1]) if (s[i]!=s[j])

dp[i][j] 表示 第 i 个字符到 第 j 个字符之间最长的回文子序列长度
当 s[i] == s[j] 时，考虑 i 和 j 中间序列的奇偶个数， dp[i][j] = dp[i+1][j-1] + 2
对上述 dp[i][j] =  dp[i+1][j-1] + 2 的解释：
当序列为 b aa b 时， i = 0, j = 3，则 dp[0][3] = dp[1][2] + 2 = 4
当序列为 b a b 时，i = 0, j = 2，则 dp[0][2] = dp[1][1] + 2 = 3 
当序列为 b b 时， i = 0, j = 1，则 dp[0][1] = dp[1][0] = 0 + 2 = 2 (dp[1][0] 默认值为 0)
该式子同时考虑到了奇偶
2、当 s[i] != s[j] ，那么 dp[i][j] = Math.max(dp[i+1][j],dp[i][j-1])
对上述 dp[i][j] 式子的解释：
假如序列为 d c b c c（index：0-4），s[0] != s[4] ，则 dp[0][4] = Math.max(dp[0][3],dp[1,4]) = Math.max(2,3) = 3

"""

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        length = len(s)
        if length <= 1:
            return length
        #dp[i][j] is the longest Palindrome subsuquence
        dp = [[0] * length for _ in range(length)]
        # Iterate the string from the end to start
        for i in range(length-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, length):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return dp[0][length-1]
        # Time complexity: O(N**2)
        # Space complexity O(N**2)
