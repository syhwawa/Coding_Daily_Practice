# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 02:41:49 2020

@author: syhwawa

We need to wrap the end time of interval as one room and append it to rooms. First we sort the interval. 
Then we iterate the given interval, if the current interval’s start time is bigger or equal than any room’s end time in rooms,
 we will append the current interval’s end time to this room; 
 if the current interval’s start time is not bigger or not equal than any room’s end time in rooms, 
 we will wrap this end time of the current interval as one room and append it to rooms. 
 Finally, the result will be the size of the rooms.
"""
def meetingroom(intervals):
    size = len(intervals)
    if size<=1: return size
    sorted_intervals = sorted(intervals)
    rooms=[[sorted_intervals[0][1]]]
    for i in range(1,size):
        booked = False
        for room in rooms:
            if sorted_intervals[i][0]>=room[-1]:
                room.append(sorted_intervals[i][1])
                booked = True
                break
        if not booked:
            rooms.append([sorted_intervals[i][1]])
    return len(rooms)

intervals = [[1,4], [2,5], [7,9]]
print(meetingroom(intervals))

#Time complexity : O($n^2$) where n is the size of input.

#Solution 2
"""
题目就是要统计同一时刻进行的最大会议的数量
我们可以把所有的开始时间和结束时间放在一起排序，
用cur表示当前进行的会议数量，遍历排序后的时间数组
如果是开始时间，cur加1，如果是结束时间，cur减一
在遍历的过程中，cur出现的最大值就是需要的房间数
"""
def minMeetingRooms(intervals):
    new_tuple = []
    for i in range(len(intervals)):
         new_tuple.append((intervals[i][0], 1))
         new_tuple.append((intervals[i][1], -1))
    new_tuple.sort()
    #print(new_tuple)
    res, tmp = 0, 0
    for k in range(len(new_tuple)):
         tmp += new_tuple[k][1]
         res = max(tmp, res)
    return res
intervals = [[0, 30],[5, 10],[15, 20]]
print(minMeetingRooms(intervals))

#Solution 3
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0

        # The heap initialization
        free_rooms = []

        # Sort the meetings in increasing order of their start time.
        intervals.sort(key= lambda x: x[0])

        # Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(free_rooms, intervals[0][1])

        # For all the remaining meeting rooms
        for i in intervals[1:]:

            # If the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)

            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(free_rooms, i[1])

        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_rooms)
