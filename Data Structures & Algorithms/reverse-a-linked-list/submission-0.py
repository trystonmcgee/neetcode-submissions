# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        
        res.reverse()
    
        dummy = ListNode()
        curr = dummy
        for num in res:
            curr.next = ListNode(num)
            curr = curr.next
        
        return dummy.next

            