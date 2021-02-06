Leetcode 437
Given a binary tree and a number ‘S’, find all paths in the tree such that the sum of all the node values of each path equals ‘S’. 

Please note that the paths can start or end at any node but all paths must follow direction from parent to child (top to bottom)

S: 12Output: 3Explanation: There are three paths with sum '12':7 -> 5, 1 -> 9 -> 2, and 9 -> 3

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def count_paths(root, sum):
  # TODO: Write your code here
  def dfs(root, sumlist):
    if not root:
        return 0
    
    sumlist = [num + root.val for num in sumlist]
    sumlist.append(root.val)
    
    count = 0
    for num in sumlist:
        if num == sum:
            count += 1
    # count = sumlist.count(sum)
    
    return count + dfs(root.left, sumlist) + dfs(root.right, sumlist)
  return dfs(root, [])


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has paths: " + str(count_paths(root, 11)))


main()
