
"""
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True
"""
class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []          #save the index for (
        star_stack = []     #save the index for *
        for char in range(len(s)):
            if s[char] == '(':
                stack.append(char)
            elif s[char] == "*":
                star_stack.append(char)
            else: # when char == ")"
                if not stack and not star_stack: 
                    return False
                if stack:
                    stack.pop()  # use open parenthesis as pair first
                elif star_stack: # secondly, use *
                    star_stack.pop()
            
        while stack and star_stack: 
            if stack.pop() > star_stack.pop(): # if index stack > index star_stack to ensure if the string is valid
                return False
        
        return not stack
        # Time Complexity: O(N)
        # Space Complexity: O(N)
        
