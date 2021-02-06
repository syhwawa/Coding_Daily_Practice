"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return
        # find middle of the LinkedList   
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # slow is now pointing to the middle node   
        second_half = self.reverse(slow)# reverse the second half
        first_half = head

        # rearrange to produce the LinkedList in the required order
        while second_half and first_half:
            n1 = first_half.next
            n2 = second_half.next

            first_half.next = second_half
            first_half = n1

            second_half.next = first_half
            second_half = n2
        
        # set the next of the last node to 'None'
        if first_half is not None:
            first_half.next = None

    def reverse(self, head):
        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre
    #Time Complexity #
    #The above algorithm will have a time complexity of O(N)O(N) where ‘N’ is the number of nodes in the LinkedList.

    #Space Complexity #
    #The algorithm runs in constant space O(1)O(1).
