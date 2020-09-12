Compression String
Given an input string of a certain length, design an algorithm that compresses the string. 

The string should be compressed such that consecutive duplicates of characters are replaced with the character and followed by the number of consecutive duplicates.

For example, if the input string is “wwwwaaadexxxxxx”, then the function should return “w4a3dex6”.

```Python

def compress(string):

    res = ""

    count = 1

    #Add in first character
    res += string[0]

    #Iterate through loop, skipping last one
    for i in range(len(string)-1):
        if(string[i] == string[i+1]):
            count+=1
        else:
            if(count > 1):
                #Ignore if no repeats
                res += str(count)
            res += string[i+1]
            count = 1
    #print last one
    if(count > 1):
        res += str(count)
    return res

compress('abaasass')
```

