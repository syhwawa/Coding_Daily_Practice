一棵深度为k，且有2^k-1个节点的树是满二叉树。

另一种定义：除了叶结点外每一个结点都有左右子叶且叶子结点都处在最底层的二叉树。


性质：

1)        如果一颗树深度为h，最大层数为k，且深度与最大层数相同，即k=h;

2)        它的叶子数是： 2^(h-1)

3)        第k层的结点数是： 2^(k-1)

4)        总结点数是： 2^k-1 (2的k次方减一)

5)        总节点数一定是奇数。

6)        树高：h=log2(n+1)。

```Python
import math
 
While True:
  i = input()
  if len(i) == 0:
    break
  n = int(i)
  print(2**(int(math.log2(n + 1))) - 1)
  
  ```
  Leetcode 252
  
  给定一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi] ，请你判断一个人是否能够参加这里面的全部会议。


示例 1：

输入：intervals = [[0,30],[5,10],[15,20]]
输出：false
示例 2：

输入：intervals = [[7,10],[2,4]]
输出：true

```Python
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True

```

