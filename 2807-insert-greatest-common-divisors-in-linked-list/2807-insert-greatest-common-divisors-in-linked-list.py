# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left, right = head, head.next
        while right:
            gcd = math.gcd(left.val, right.val)

            gcd_node = ListNode(gcd)
            
            left.next = gcd_node
            gcd_node.next = right
            left = right
            right = right.next

        return head