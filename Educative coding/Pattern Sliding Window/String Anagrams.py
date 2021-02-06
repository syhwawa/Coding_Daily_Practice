Given a string and a pattern, find all anagrams of the pattern in the given string.

Anagram is actually a Permutation of a string. For example, “abc” has the following six anagrams:

abc
acb
bac
bca
cab
cba
Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

Example 1:

Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".
Example 2:

Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".

Leetcode 438

def find_string_anagrams(s, pattern):
  result_indexes = []
  # TODO: Write your code here
  win_start, match = 0, 0
  dic = {}
  for i in pattern:
    if i not in dic:
      dic[i] = 1
    else:
      dic[i] += 1

  # Our goal is to match all the characters from the 'dic' with the current window
  # try to extend the range [window_start, window_end]
  for win_end in range(len(s)):
    right_char = s[win_end]
    if right_char in dic:
      # Decrement the frequency of matched character
      dic[right_char] -= 1
      if dic[right_char] == 0:
        match += 1
  
    if len(dic) == match:
      result_indexes.append(win_start)

    # If the window size is greater than the length of the pattern, shrink the window to make it equal to the pattern’s size. 
    # At the same time, if the character going out was part of the pattern, put it back in the HashMap.
    if win_end >= len(pattern) - 1:
      left_char = s[win_start]
      win_start += 1
      if left_char in dic:
        if dic[left_char] == 0:
          match -= 1 # Before putting the character back, decrement the matched count
        dic[left_char] += 1 # Put the character back
      
  return result_indexes
  
# Time Complexity #
The time complexity of the above algorithm will be O(N + M)O(N+M) where ‘N’ and ‘M’ are the number of characters in the input string and the pattern respectively.

# Space Complexity #
The space complexity of the algorithm is O(M)O(M) since in the worst case, the whole pattern can have distinct characters which will go into the HashMap
