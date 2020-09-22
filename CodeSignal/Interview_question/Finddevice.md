input: data = ['iqttt, 0077',
       'obvhd, 0093',
       'flohd, 0075']
output = 'obvhd'
```
def getdevicemodel(data):
    res = []
    for i in data:
        for j in i.split(','):
            res.append(j)

    num = []
    
    for c in range(len(res)):
        if c % 2 == 1:
            num.append(res[c])
    max_n = str(max(num))
    
    for idx, value in enumerate(res):
        if value == max_n:
            return res[idx - 1]
```
