# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 17:26:57 2020

@author: syhwawa

"""

"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Example 3:

Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]
Example 4:

Input: intervals = [[1,5]], newInterval = [2,3]
Output: [[1,5]]
Example 5:

Input: intervals = [[1,5]], newInterval = [2,7]
Output: [[1,7]]
 
"""
#Solution 1
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x: x[0])
        res = [intervals[0]]
        
        for x, y in intervals[1:]:
            if x > res[-1][1]:
                res.append([x, y])
            else:
                res[-1][1] = max(y, res[-1][1])
                
        return res

#Solution 2
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i, start, end = 0, 0, 1
        
        # skip (and add to output) all intervals that come before the 'new_interval'
        while i < len(intervals) and intervals[i][end] < newInterval[start]:
            res.append(intervals[i])
            i += 1
            
        # merge all intervals that overlap with 'new_interval' 
        while i < len(intervals) and intervals[i][start] <= newInterval[end]:
            newInterval[start] = min(intervals[i][start], newInterval[start])
            newInterval[end] = max(intervals[i][end], newInterval[end])
            i += 1
            
        res.append(newInterval)
        
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        return res
        
# TC: O(N)

