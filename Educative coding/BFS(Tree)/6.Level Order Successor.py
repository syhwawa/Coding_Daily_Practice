Given a binary tree and a node, find the level order successor of the given node in the tree. 
The level order successor is the node that appears right after the given node in the level order traversal.

from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_successor(root, key):
  # TODO: Write your code here
  return None
  res = []

  d = deque()
  d.append(root)

  while d:
    dsize =len(d)
    for i in range(dsize):
      cur_node = d.popleft()
      res.append(cur_node.val)
      if cur_node.left:
        res.append(cur_node.left)
        d.append(cur_node.left)
      if cur_node.right:
        res.append(cur_node.right)
        d.append(cur_node.right)

  for i in range(len(res)):
    if res[i] == key:
      return res[i+1]
      
#Solution 2:

  queue = deque()
  queue.append(root)
  while queue:
    currentNode = queue.popleft()
    # insert the children of current node in the queue
    if currentNode.left:
      queue.append(currentNode.left)
    if currentNode.right:
      queue.append(currentNode.right)

    # break if we have found the key
    if currentNode.val == key:
      break

  return queue[0] if queue else None
  

