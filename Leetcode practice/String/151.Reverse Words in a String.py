# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 15:48:09 2020

@author: syhwawa
"""

"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
Example 4:

Input: s = "  Bob    Loves  Alice   "
Output: "Alice Loves Bob"
Example 5:

Input: s = "Alice does not even like bob"
Output: "bob like even not does Alice"
"""


def reverseWords(s) :
    s1 = s.split()
    res = []
    for i in reversed(s1):
        res += ''.join(i)
        res += " "
    return res


s = "Alice does not even like bob"
reverseWords(s)

"""
Follow up
Example 1:
Input: "The cat in the hat"
Output: "ehT tac ni eht tah"
"""


s1 = s.split()
res = ""
for i in s1:
    res += ''.join(reversed(i))
    res += " "
res