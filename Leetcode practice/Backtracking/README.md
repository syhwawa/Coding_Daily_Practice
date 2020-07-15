## Backtrack回溯

1. [回溯算法详解》的进阶版](https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-xiang-jie-by-labuladong-2/)
2. [Leetcode题目答案](https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-by-powcai-2/)


result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return
    
    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择

