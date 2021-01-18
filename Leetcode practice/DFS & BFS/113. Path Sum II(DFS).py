https://leetcode-cn.com/problems/path-sum-ii/solution/tao-mo-ban-er-cha-shu-wen-ti-de-dfs-he-bfs-jie-fa-/

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]

Solution 1: DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []

        def dfs(root, sum, res, path):
            if not root:
                return 

            if not root.left and not root.right:
                if root.val == sum:
                    res.append(path + [root.val])
            dfs(root.left, sum - root.val, res, path + [root.val])
            dfs(root.right, sum - root.val, res, path + [root.val])
        
        dfs(root, sum, res, [])
        return res
    # TC:O(N)
    # SC:O(N)
    
        
        
        
Solution 2: BFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        que = deque()
        que.append((root, [], 0)) # 将要处理的节点，路径，路径和
        while que:
            node, path, pathSum = que.popleft()
            if not node: # 如果是空节点，不处理
                continue
            if not node.left and not node.right: # 如果是叶子节点
                if node.val + pathSum == sum: # 加上叶子节点后，路径和等于sum
                    res.append(path + [node.val]) # 保存路径
            # 处理左子树
            que.append((node.left, path + [node.val], pathSum + node.val))
            # 处理右子树
            que.append((node.right, path + [node.val], pathSum + node.val))
        return res
