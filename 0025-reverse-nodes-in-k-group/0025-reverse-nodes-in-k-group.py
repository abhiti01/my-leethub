# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def reverse (self, a, b):
    #     pre = None
    #     cur = a
    #     nxt = a
    #     while cur != b:
    #         nxt = cur.next
    #         cur.next = pre
    #         pre = cur
    #         cur = nxt
    #     return pre

    # def reverseKGroup(self, head, k):
    #     if head == None:
    #         return None
    #     a = b = head
    #     for i in range(k):
    #         if b == None:
    #             return head
    #         b = b.next
    #     newHead = self.reverse(a,b)
    #     a.next = self.reverseKGroup(b,k)
    #     return newHead

        #O(1) space solution (non-recursive)

    # """
    #  None <-1  <-2  3 
                
            
    #             prev
    #                   curr
    # """
        def reverseList(self, head, k):
            prev = None
            curr = head
            
            for _ in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            
            return prev, curr

        def reverseKGroup(self, head, k):
            dummy = ListNode(0)
            dummy.next = head
            ptr = dummy
            
            while ptr is not None:
                tracker = ptr
                
                # Check if there are k nodes to reverse
                for _ in range(k):
                    tracker = tracker.next
                    if tracker is None:
                        return dummy.next # If fewer than k nodes, return result
                
                # Reverse k nodes
                prev, curr = self.reverseList(ptr.next, k)
                
                last_node_of_reversed_group = ptr.next # to link to next group
                last_node_of_reversed_group.next = curr # link to next group
                ptr.next = prev # point ptr to prev, the new head
                
                ptr = last_node_of_reversed_group # Move ptr forward
            
            return dummy.next


        

