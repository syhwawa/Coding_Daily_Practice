Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.

Implement the TwoSum class:

TwoSum() Initializes the TwoSum object, with an empty array initially.
void add(int number) Adds number to the data structure.
boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value, otherwise, it returns false.
 

Example 1:

Input
["TwoSum", "add", "add", "add", "find", "find"]
[[], [1], [3], [5], [4], [7]]
Output
[null, null, null, null, true, false]

Explanation
TwoSum twoSum = new TwoSum();
twoSum.add(1);   // [] --> [1]
twoSum.add(3);   // [1] --> [1,3]
twoSum.add(5);   // [1,3] --> [1,3,5]
twoSum.find(4);  // 1 + 3 = 4, return true
twoSum.find(7);  // No two integers sum up to 7, return false

class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashtable = {}


    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number in self.hashtable:
            self.hashtable[number] += 1
        else:
            self.hashtable[number] = 1


    def find(self, target: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for key1 in self.hashtable.keys():
            key2 = target - key1
            if key2 in self.hashtable:
                if self.hashtable[key2] >= 1 and key1 != key2:
                    return True
                if self.hashtable[key2] > 1 and key1 == key2:
                    return True
        return False



# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
