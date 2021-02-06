Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        
        while queue:
            queue_size = len(queue)
            current_level = []
            for i in range(queue_size):
                current_node = queue.popleft()
                # add the node to the current level
                current_level.append(current_node.val)
                # insert the children of current node in the queue
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
                
            res.append(current_level)
            
        return res
        
        
    # O(N)
    # O(N)
        
