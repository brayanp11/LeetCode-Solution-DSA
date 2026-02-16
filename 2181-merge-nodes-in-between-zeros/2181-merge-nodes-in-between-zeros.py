# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        curr, nxt = head, head.next
        curr_sum = 0
        while nxt:
            if nxt.val != 0:
                curr_sum += nxt.val
            else:
                curr = curr.next
                curr.val = curr_sum
                curr_sum = 0

            nxt = nxt.next

        curr.next = None

        return head.next