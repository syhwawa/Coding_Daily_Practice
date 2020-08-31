## Problem Statement
Given a string, find the length of the __longest substring__ in it with no more than K distinct characters.

Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".


```Python
def longest_substring_with_k_distinct(string, k):
  # TODO: Write your code here
  p1 = 0
  max_length = 0
  hashmap = {}

  for p2 in range(len(string)):
      if string[p2] not in hashmap:
          hashmap[string[p2]] = 1
      else:
          hashmap[string[p2]] += 1

      while len(hashmap) > k:
          hashmap[string[p1]] -= 1
          
          if hashmap[string[p1]] == 0:
              del hashmap[string[p1]]
          p1 += 1
      max_length = max(max_length, (p2 - p1 + 1)) 

  return max_length
```
Time Complexity O(N)

Space Complexity O(K)
