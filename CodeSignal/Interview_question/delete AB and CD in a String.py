# Output the string by delete the AB and CD in the string.
eg. 
ABC -> C
CDACD -> A
ACBADA - >ACBADA


def solution(s):
  res = []
  for ch in s:
    if len(res) == 0:
      res.append(ch)
    elif res[-1] == 'A' and ch == 'B':
      res.pop()
    elif res[-1] == 'B' and ch == 'A':
      res.pop()
    elif res[-1] == 'C' and ch == 'D':
      res.pop()
    elif res[-1] == 'D' and ch == 'C':
      res.pop()
    else:
      res.append(ch)
  return ''.join(res)

print(solution('CBACD'))
print(solution('CABABD'))
print(solution('ACBDACBD'))
