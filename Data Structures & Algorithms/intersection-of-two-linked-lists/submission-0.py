# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A = set()
        currA = headA
        while currA:
            A.add(currA)
            currA = currA.next

        currB = headB
        while currB:
            if currB in A:
                return currB
            currB = currB.next
        
        return None
