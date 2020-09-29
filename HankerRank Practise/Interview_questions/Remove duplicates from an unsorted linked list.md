Write a removeDuplicates() function which takes a list and deletes any duplicate nodes from the list. The list is not sorted. 
For example if the linked list is 12->11->12->21->41->43->21 then removeDuplicates() should convert the list to 12->11->21->41->43. 

```Python
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        curr = head
        while curr is not None:
            inner = curr
            while inner.next is not None:
                if inner.next.val == curr.val:
                    inner.next = inner.next.next
                else:
                    inner = inner.next
            curr = curr.next

        return head
        
```

```Python
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:    
        if not head.val:
            return None
            
        p = head.next
        s = {head.val}  # 第一个
        prev = head
        while p is not None:
            if p.val in s:
                prev.next = p.next
            else:
                s.add(p.val)
                prev = p
            p = p.next
            
        return head

```
