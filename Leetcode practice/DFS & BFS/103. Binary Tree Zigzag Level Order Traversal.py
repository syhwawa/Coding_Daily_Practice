Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        
        queue =deque()
        queue.append(root)
        # 用来标记当前层是偶数层还是奇数层
        left_to_right = True
        while queue:
            que_size = len(queue)
            current_level = deque()
            
            for _ in range(que_size):
              # 取出节点
                cur_node = queue.popleft()
                
                if left_to_right:
                    current_level.append(cur_node.val)
                else:
                    current_level.appendleft(cur_node.val)
                    
                if cur_node.left:
                    queue.append(cur_node.left)

                if cur_node.right:
                    queue.append(cur_node.right)
                    
            res.append(current_level)
            
            left_to_right = not left_to_right
        
        return res
        
  class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        #先层序遍历 再把偶数层的结果反转
        stack = [root]
        res = []
        while stack:
            level = []
            for _ in range(len(stack)):
                node = stack.pop(0)
                if not node:
                    continue
                level.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
            if level:
                res.append(level)
        for i in range(1,len(res),2):
                res[i] = res[i][::-1]
        return res


                
