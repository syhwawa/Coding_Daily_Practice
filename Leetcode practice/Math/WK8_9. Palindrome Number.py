Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Solution 1:
Change number as String
class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        for i in range(len(string)):
            if string[i] != string[len(string)-1-i]:
                return False
        return True

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        str_x = str(x)
        l, r = 0, len(str_x) - 1
        while r>l:
            if str_x[l] != str_x[r]:
                return False
            l += 1; r -= 1
        return True

Follow up: Do not use str

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
        
Solution2:
Get the Palindrome Number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        carry = 0
        num = x
        while num:
            carry = carry * 10 + num % 10 
            num = num // 10
            
        if carry != x:
            return False
        
        return True


