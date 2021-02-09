Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {"(": ")", "[": "]", "{": "}"}
        for i in s:
            if i in dic:
            # If the input string contains an opening parenthesis,
            # push in on to the stack.
                stack.append(dic[i])
            else:
                # if the input string contains closing parenthesis, pop the corrpesponding opening one 
                if len(stack) == 0:
                    return False
                if stack.pop() != i:
                    return False
        
        return len(stack) == 0
        
        
