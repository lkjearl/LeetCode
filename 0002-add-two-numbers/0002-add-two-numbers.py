# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current = head
        carryOver = 0
        
        while l1 or l2 or carryOver:
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0
            _sum = value1 + value2 + carryOver

            carryOver = _sum // 10
            current.next = ListNode(_sum % 10)

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            current = current.next

        return head.next