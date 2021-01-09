Given an input string of a certain length, design an algorithm that compresses the string. 

The string should be compressed such that consecutive duplicates of characters are replaced with the character and followed by the number of consecutive duplicates.

For example, if the input string is “wwwwaaadexxxxxx”, then the function should return “w4a3dex6”


def string_compression(s):
    length = len(s)
    compress_string = ""
    i = 0
    while i < length:
        count = 1
        while (i < length -1) and (s[i] == s[i+1]):
            count += 1 
            i += 1
        
        if count == 1:
            compress_string += str(s[i]) + str(1)
        else:
            compress_string += str(s[i]) + str(count)
        i += 1
        
    return compress_string

print(string_compression("aabcccccaaa"))
print(string_compression("wwwwaaadexxxxxx"))
