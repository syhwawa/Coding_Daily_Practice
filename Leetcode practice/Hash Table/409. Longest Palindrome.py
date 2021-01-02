Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Example 3:

Input: s = "bb"
Output: 2


import collections
class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = collections.Counter(s)
        count = 0
        for i in c.values():
            # if v occured i times, i // 2 * 2 is the longest palindrome string
            count += i // 2 * 2
            # put a odd name in the middle place for once
            if count % 2 == 0 and i % 2 == 1:
                count += 1
        return count
        
        # TC： O(N)
        # Space Complexity: O(1)O(1), the space for our count, as the alphabet size of s is fixed. We should also consider         #that in a bit complexity model, technically we need O(\log N)O(logN) bits to store the count values
