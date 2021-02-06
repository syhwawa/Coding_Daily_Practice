Leetcode 70
A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs. The result may be large, so return it modulo 1000000007.

Example1:

 Input: n = 3 
 Output: 4
Example2:

 Input: n = 5
 Output: 13
class Solution:
    def waysToStep(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [None for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            """
            取模，对两个较大的数之和取模再对整体取模，防止越界（这里也是有讲究的）
            假如对三个dp[i-n]都 % 1000000007，那么也是会出现越界情况（导致溢出变为负数的问题）
            因为如果本来三个dp[i-n]都接近 1000000007 那么取模后仍然不变，但三个相加则溢出
            但对两个较大的dp[i-n]:dp[i-2],dp[i-3]之和mod 1000000007，那么这两个较大的数相加大于 1000000007但又不溢出
            取模后变成一个很小的数，与dp[i-1]相加也不溢出
            所以取模操作也需要仔细分析
            """

            dp[i] = (dp[i-3] + dp[i-2] + dp[i-1] % 1000000007) % 1000000007
        
        return dp[-1]
