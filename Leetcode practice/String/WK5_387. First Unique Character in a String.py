Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Solution1：
class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = collections.Counter(s)
        
        for i, time in enumerate(s):
            if n[time] == 1:
                return i
  
        return -1
        
              
Solution 2: Hashtable
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dicts={}
        for i in s:
            dicts[i]=dicts.get(i,0)+1
        for i in range(len(s)):
            if dicts[s[i]]==1:
                return i
        return -1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashtable = {}
        for i in s:
            if i not in hashtable:
                hashtable[i] = 1
            else:
                hashtable[i] += 1

        for idx, value in enumerate(s):
            if hashtable[value] == 1:
                return idx  
        return -1
        
