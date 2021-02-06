Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        win_start, match = 0,0 
        res = []
        frequency = {}
        for i in p:
            if i not in frequency:
                frequency[i] = 1
            else:
                frequency[i] += 1
        
        for win_end in range(len(s)):
            right = s[win_end]
            if right in frequency:
                frequency[right] -= 1
                if frequency[right] == 0:
                    match += 1
            
            if len(frequency) == match:
                res.append(win_start)

            if win_end >= len(p) - 1:
                left = s[win_start]
                win_start += 1
                if left in frequency:
                    if frequency[left] == 0:
                        match -= 1
                    
                    frequency[left] += 1

        return res
