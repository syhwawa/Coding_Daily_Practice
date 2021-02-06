Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []

        def dfs(root, path):
            if root:
                path += str(root.val)
                if not root.right and not root.left:
                    res.append(path)

                else:
                    path += "->"
                    dfs(root.left, path)
                    dfs(root.right, path)
            
        dfs(root, "")
        return res
                
# TC:o(N**2)
# SC:o(N**2)
