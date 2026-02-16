# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow
        while curr:
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next

        max_sum = 0
        head1, head2 = head, prev
        while head2:
            curr_sum = head1.val + head2.val
            max_sum = max(max_sum, curr_sum)

            head1, head2 = head1.next, head2.next
            
        return max_sum