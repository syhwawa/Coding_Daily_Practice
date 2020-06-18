# Tree
树是一种非线性数据结构。

树结构的基本单位是节点。节点之间的链接，称为分支（branch）。节点与分支形成树状，结构的开端，称为根（root），或根结点。根节点之外的节点，称为子节点（child）。没有链接到其他子节点的节点，称为叶节点（Leaf）。

除此之外，关于“树”，还有三个比较相似的概念：高度（Height）、深度（Depth）、层（Level）。
高度：节点到叶子节点的最长路径（边数）
深度：根节点到这个节点所经历的边的个数
层数：深度+1
高度：根结点的高度

```Python
                          High      Lepth      Level
       j    <-- root      3           0          1
     /   \                
    f      k              2           1          2
  /   \   /  \
 a     h  a   z  leaves   1           2          3
/ \          /
c  d        g             0           3          4
```

## 二叉树的遍历
前序遍历是指，对于树中的任意节点来说，先打印这个节点，然后再打印它的左子树，最后打印它的右子树。
中序遍历是指，对于树中的任意节点来说，先打印它的左子树，然后再打印它本身，最后打印它的右子树。
后序遍历是指，对于树中的任意节点来说，先打印它的左子树，然后再打印它的右子树，最后打印这个节点本身。



### LC102-Binary Tree Level Order Traversal
### LC144-Binary Tree Preorder Traversal
### LC622-Design Circular Queue
### LC107-Binary Tree Level Order Traversal II
### LC637-Average of Levels in Binary Tree
### LC543-Diameter of Binary Tree
