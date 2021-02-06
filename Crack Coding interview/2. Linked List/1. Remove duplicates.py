#Write code to remove duplicates from an unsorted linked list.
#FOLLOW UP
#How would you solve this problem if a temporary buffer is not allowed?

# if Sorted linked list 83. Remove Duplicates from Sorted List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next   
        return head


# Using set to store 
  def removeDuplicates(self, head):
         
        # Base case of empty list or 
        # list with only one element
        if self.head is None or self.head.next is None:
            return head
             
        # Hash to store seen values 
        hash = set()  
 
        current = head
        hash.add(self.head.data)
 
        while current.next is not None:
 
            if current.next.data in hash:
                current.next = current.next.next
            else:
                hash.add(current.next.data)
                current = current.next
 
        return head
 # TC: O(n)
 # SC: O(1)
        

