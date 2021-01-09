#Leecode 161
"""
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away
"""

def one_way(s, t):
    lens = len(s)
    lent = len(t)
    
    if abs(lent - lens) > 1:
        return False
    
    if lens > lent:
        return one_way(t, s)
    
    for i in range(len(s)):
        if s[i] != t[i]:
            if lens == lent:
                return s[i+1:] == t[i+1:]
            else:
                return s[i:] == t[i+1:]
            
    return lens + 1 == lent

print(one_way("pale", "ple"))
print(one_way("pales", "pale"))
print(one_way("pale", "bale"))
print(one_way("pale", "bake"))
