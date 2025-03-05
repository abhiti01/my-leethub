# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        return prev

        # another way of reversing a list - traverse and insert each node at the head


        # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #     curr = head
        #     prev = None
        #     while curr:

        #         # Keep track of the next node to process in the
        #         # original list
        #         next_node = curr.next

        #         # Insert the node pointed to by "curr"
        #         # at the beginning of the reversed list
        #         curr.next = prev
        #         prev = curr

        #         # Move on to the next node
        #         curr = next_node

        #     # Return the head of the reversed list
        #     return prev