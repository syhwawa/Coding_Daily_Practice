Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = deque()
        if not root:
            return res
        
        queue = deque()
        queue.append(root)
        
        while queue:
            current_level = []
            queue_size = len(queue)
            
            for _ in range(queue_size):
                curr_node = queue.popleft()
                current_level.append(curr_node.val)
                
                if curr_node.left:
                    queue.append(curr_node.left)
                    
                if curr_node.right:
                    queue.append(curr_node.right)
                    
            res.appendleft(current_level)
            
        return res
