Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the square of all of its digits, leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’.
Instead, they will be stuck in a cycle of numbers which does not include ‘1’.

Example 1:

Input: 23   
Output: true (23 is a happy number)  
Explanations: Here are the steps to find out that 23 is a happy number:

# Solution The process, defined above, to find out if a number is a happy number or not, always ends in a cycle. If the number is a happy number, 
# the process will be stuck in a cycle on number ‘1,’ and if the number is not a happy number then the process will be stuck in a cycle with a set of numbers

def find_happy_number(num):
  # TODO: Write your code here
  dic = set()
  while num != 1:
    dic.add(num)
    num = sum([int(i) ** 2 for i in str(num)])
    if num in dic:
      return False
    else:
      dic.add(num)
  return True


def main():
  print(find_happy_number(23))
  print(find_happy_number(12))

main()
# Time Complexity: O(N)
# Space Complexity: O(1)

#Solution 2:
def find_happy_number(num):
  slow, fast = num, num
  while True:
    slow = find_square_sum(slow)  # move one step
    fast = find_square_sum(find_square_sum(fast))  # move two steps
    if slow == fast:  # found the cycle
      break
  return slow == 1  # see if the cycle is stuck on the number '1'


def find_square_sum(num):
  _sum = 0
  while (num > 0):
    digit = num % 10
    _sum += digit * digit
    num //= 10
  return _sum


def main():
  print(find_happy_number(23))
  print(find_happy_number(12))


main()
