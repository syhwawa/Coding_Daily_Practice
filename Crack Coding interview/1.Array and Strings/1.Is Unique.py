"""
Determine if a string has all Unique Characters

Given a string, determine if the string has all unique characters. Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?

Examples :  
Input : abcd10jk
Output : true

Input : hutg9mnd!nk9
Output : false
"""

#Solution1:
# Python3 program to illustrate string
# with unique characters using
# brute force technique
def uniqueCharacters(st):
 
    # Using sorting
    sorted(st)
 
    for i in range(len(st)-1):
 
        # if at any time, 2 adjacent
        # elements become equal,
        # return false
        if (st[i] == st[i + 1]) :
            return False
             
    return True
# TC O(NlongN)

#Solution2:
def isunique(s):
    return len(set(s)) == len(s)

print(isunique('abcd10jk'))  
print(isunique('hutg9mnd!nk9'))  


def is_unique_chars_algorithmic(string):
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    # this is a pythonic and faster way to initialize an array with a fixed value.
    #  careful though it won't work for a doubly nested array
    char_set = [False] * 128
    for char in string:
        val = ord(char)
        if char_set[val]:
            # Char already found in string
            return False
        char_set[val] = True

    return True
