```Python
def entryTime(s, keypad):
    dic = {}
    for i in range(3):
        for j in range(3):
            dic[int(keypad[i*3+j])] = (i, j)
            # dic[i*3+j] = (i, j) <--- Wrong
            
    if len(s) < 2:
        return 0
    
    res = 0
    for k in range(1, len(s)):
        pre_x, pre_y = dic[int(s[k-1])][0], dic[int(s[k-1])][1]
        x, y = dic[int(s[k])][0], dic[int(s[k])][1]
        if abs(x - pre_x) > 1 or abs(y - pre_y) > 1:
            res += 2
        elif abs(x - pre_x) == 0 and abs(y - pre_y) == 0:
            pass
        else:
            res += 1    
    return res
```

```Python
s = "5112"
keypad = "752961348"
print(entryTime(s, keypad))
```
