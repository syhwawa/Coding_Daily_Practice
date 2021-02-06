"""
Input: ch = “geeksforgeeks”
Output: e
e is the first element that repeats

Input: str = “hello geeks”
Output: l
l is the first element that repeats
"""
def first_recurring_char(s):
    dic = {}
    for i in s:
        if i not in dic:
            dic[i] = 1
        else:
            return i
    return None
print(first_recurring_char("geeksforgeeks"))
print(first_recurring_char("hello geeks"))
print(first_recurring_char('qwertty'))
