""" Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

Example 1:

Input: s1 = "ab" s2 = "eidbaooo" Output: True Explanation: s2 contains one permutation of s1 ("ba"). Example 2:

Input:s1= "ab" s2 = "eidboaoo" Output: False
Solution # This problem follows the Sliding Window pattern, and we can use a similar sliding window strategy as discussed in Longest Substring with K Distinct Characters. We can use a HashMap to remember the frequencies of all characters in the given pattern. Our goal will be to match all the characters from this HashMap with a sliding window in the given string. Here are the steps of our algorithm:

Create a HashMap to calculate the frequencies of all characters in the pattern. 
Iterate through the string, adding one character at a time in the sliding window. 
If the character being added matches a character in the HashMap, decrement its frequency in the map. 
If the character frequency becomes zero, we got a complete match. 
If at any time, the number of characters matched is equal to the number of distinct characters in the pattern (i.e., total characters in the HashMap), 
we have gotten our required permutation. If the window size is greater than the length of the pattern, shrink the window to make it equal to the pattern’s size. 
At the same time, if the character going out was part of the pattern, put it back in the frequency HashMap 
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        win_start, match = 0, 0

        hashtable = {}
        for i in s1:
            if i not in hashtable:
                hashtable[i] = 1
            else:
                hashtable[i] += 1
        # our goal is to match all the characters from the 'hashtable' with the current window
        # try to extend the range [window_start, window_end]
        for win_end in range(len(s2)):
            right_char = s2[win_end]
            if right_char in hashtable:
                hashtable[right_char] -= 1
                if hashtable[right_char] == 0:
                    match += 1
            
            if len(hashtable) == match:
                return True
                
            # shrink the window by one character           
            if win_end >= len(s1) - 1:
                left_char = s2[win_start]
                win_start += 1
                if left_char in hashtable:
                    if hashtable[left_char] == 0:
                        match -= 1
                    hashtable[left_char] += 1

        return False



        

