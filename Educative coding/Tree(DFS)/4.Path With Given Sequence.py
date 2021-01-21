Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.

Example 1:

Sequence: [1, 9, 9]Output: true Explanation: The tree has a path 1 -> 9 -> 9.
Example 2:

Sequence: [1, 0, 7]Output: false Explanation: The tree does not have a path 1 -> 0 -> 7.Sequence: [1, 1, 6]Output: true Explanation: The tree has a path 1 -> 1 -> 6.

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_path(root, sequence):
  # TODO: Write your code here
  res = []
  def dfs(root, res, path):
    if not root:
      return 
    if not root.left and not root.right:
      res.append(path +[root.val])
    
    dfs(root.left, res, path + [root.val])
    dfs(root.right, res, path + [root.val])
  
  dfs(root, res, [])

  return sequence in res

def main():

  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)

  print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
  print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))

main()

#The time complexity of the above algorithm is O(N)O(N), where ‘N’ is the total number of nodes in the tree. This is due to the fact that we traverse each node once.
#The space complexity of the above algorithm will be O(N)O(N) in the worst case. This space will be used to store the recursion stack. The worst case will happen when the given tree is a linked list (i.e., every node has only one child).

