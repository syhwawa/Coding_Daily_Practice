```
For ids = [529665, 909767, 644200] and k = 3, the output should be
isTestSolvable(ids, k) = true.

(5 + 2 + 9 + 6 + 6 + 5) + (9 + 0 + 9 + 7 + 6 + 7) + (6 + 4 + 4 + 2 + 0 + 0) = 87

def isTestSolvable(ids, k):
    digitSum = lambda x: (x%10) + digitSum(x//10) if x != 0 else 0
    sm = 0
    for questionId in ids:
        sm += digitSum(questionId)
    return sm % k == 0
```
