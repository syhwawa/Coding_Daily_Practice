# Leetcode 234
Implement a function to check if a linked list is a palindrome.

Example 1:

Input:  1->2
Output:  false 
Example 2:

Input:  1->2->2->1
Output:  true 

# Solution 1, Extra space
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        res =  []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res == res[::-1]
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True

        # find middle of the LinkedList
        slow, fast = head, head
        while (fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next

        head_second_half = self.reverse(slow)  # reverse the second half
        # store the head of reversed part to revert back later
        copy_head_second_half = head_second_half

        # compare the first and the second half
        while (head is not None and head_second_half is not None):
            if head.val != head_second_half.val:
                break  # not a palindrome

            head = head.next
            head_second_half = head_second_half.next

        self.reverse(copy_head_second_half)  # revert the reverse of the second half

        if head is None or head_second_half is None:  # if both halves match
            return True

        return False

    def reverse(self, head):
        prev = None
        while (head is not None):
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev


#Time complexity #
#The above algorithm will have a time complexity of O(N) where ‘N’ is the number of nodes in the LinkedList.

#Space complexity #
#The algorithm runs in constant space O(1).
