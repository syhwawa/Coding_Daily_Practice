# Implement an algorithm to find the kth to last element of a singly linked list.
Implement an algorithm to find the kth to last element of a singly linked list. Return the value of the element.

Note: This problem is slightly different from the original one in the book.

Example:

Input:  1->2->3->4->5 和 k = 2
Output:  4
Note:

k is always valid.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        prev = head
        cur = head
        for i in range(k):
            if not cur:
                return None
            cur = cur.next

        while cur:
            cur = cur.next
            prev = prev.next
        
        return prev.val
