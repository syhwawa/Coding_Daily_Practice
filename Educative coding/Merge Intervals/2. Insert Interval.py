# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 15:13:37 2020

@author: syhwawa
"""
"""
Example 1:

Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
Output: [[1,3], [4,7], [8,12]]
Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].
Example 2:

Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
Output: [[1,3], [4,12]]
Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].
Example 3:

Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
Output: [[1,4], [5,7]]
Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them int

"""


def insert(intervals, new_interval):
  intervals.append(new_interval)

  intervals.sort(key = lambda x : x[0])
  res = [intervals[0]]

  for x, y in intervals[1:]:
      if x > res[-1][1]:
          res.append([x, y])
      else:
          res[-1][1] = max(y, res[-1][1])
  return res


def main():
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
  print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))

main()

#Time Complexity O(N*LOG(N))

#Solution 2:
def insert(intervals, new_interval):
  merged = []
  i, start, end = 0, 0, 1

  # skip (and add to output) all intervals that come before the 'new_interval'
  while i < len(intervals) and intervals[i][end] < new_interval[start]:
    merged.append(intervals[i])
    i += 1

  # merge all intervals that overlap with 'new_interval'
  while i < len(intervals) and intervals[i][start] <= new_interval[end]:
    new_interval[start] = min(intervals[i][start], new_interval[start])
    new_interval[end] = max(intervals[i][end], new_interval[end])
    i += 1

  # insert the new_interval
  merged.append(new_interval)

  # add all the remaining intervals to the output
  while i < len(intervals):
    merged.append(intervals[i])
    i += 1
  return merged


def main():
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
  print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))

main()

