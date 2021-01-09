Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.

 
Follow up:
Could you solve it using only O(1) extra space?

 
Example 1:

Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
 

Example 2:

Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.
 

Example 3:

Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.
 

Note:

All characters have an ASCII value in [35, 126].
1 <= len(chars) <= 1000.


Solution:
class Solution:
    def compress(self, s: List[str]) -> int:
        count = 1
        for i in range(len(s)-1, -1, -1):
            if i and s[i] == s[i-1]:
                s.pop(i)
                count += 1
        
            else:
                if count >1:
                    for j in str(count)[::-1]: # for case 3, otherwise output is ["a","b","1","2"]
                        s.insert(i+1, j)
                
                count = 1
                
 class Solution:
    def compress(self, chars: List[str]) -> int:
        left = i = 0
        length = len(chars)
        while i < length:
            count = 1
            char = chars[i]
            while (i < length - 1) and (char == chars[i+1]):
                count += 1
                i += 1
            chars[left] = char 
            if count > 1:
                len_str = str(count)
                chars[left + 1: left + 1 + len(len_str)] = len_str
                left += len(len_str)
            left, i = left + 1, i + 1
        return left
        
 https://leetcode.com/problems/string-compression/discuss/92568/Python-Two-Pointers-O(n)-time-O(1)-space

