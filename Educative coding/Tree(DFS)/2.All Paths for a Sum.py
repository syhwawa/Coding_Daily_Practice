Leetcode 113
Problem Statement #
Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def find_paths(root, sum):
  res = []
  # TODO: Write your code here

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

def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  sum = 23
  print("Tree paths with sum " + str(sum) +
        ": " + str(find_paths(root, sum)))

main()



