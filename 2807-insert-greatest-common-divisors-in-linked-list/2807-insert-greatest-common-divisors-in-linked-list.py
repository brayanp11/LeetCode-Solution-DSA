# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        curr, nxt = head, head.next
        while nxt:
            gcd = math.gcd(curr.val, nxt.val)

            gcd_node = ListNode(gcd)

            curr.next = gcd_node
            gcd_node.next = nxt
            curr = nxt
            nxt = nxt.next

        return head