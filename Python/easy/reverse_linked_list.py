# https://leetcode.com/problems/merge-sorted-array

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node = None
        while head:
            temp = head.next
            head.next = node
            node = head
            head = temp

        return node
