"""
You are given an array of strings words and a string pref.

Return the number of strings in words that contain pref as a prefix.

A prefix of a string s is any leading contiguous substring of s.

 

Example 1:

Input: words = ["pay","attention","practice","attend"], pref = "at"
Output: 2
Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".
Example 2:

Input: words = ["leetcode","win","loops","success"], pref = "code"
Output: 0
Explanation: There are no strings that contain "code" as a prefix.

"""

def prefixCount(words, pref):
    count = 0
    for word in words:
        if len(pref) > len(word):
            pass
        elif pref == word[:len(pref)]:
            count +=1
        else:
            pass
    return count

words = ["pay","attention","practice","attend"]
pref = "at"

print(prefixCount(words, pref))

"""
def prefixCount(words, pref):
    	return sum([word.startswith(pref) for word in words])

"""