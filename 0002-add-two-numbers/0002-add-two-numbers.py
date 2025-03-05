# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2= l2
        ans = ListNode(0)
        p3 = ans
        carry = 0
        while p1 or p2 or carry:
            p1Val = p1.val if p1 else 0
            p2Val = p2.val if p2 else 0
            total = p1Val + p2Val + carry
            carry = total//10
            newNode = ListNode(total % 10)
            p3.next =newNode
            p3 = newNode
            p1=p1.next if p1 else None
            p2 = p2.next if p2 else None
            
        
            
        return ans.next
        
            