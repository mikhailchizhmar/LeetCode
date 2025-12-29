# https://leetcode.com/problems/linked-list-cycle

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def has_cycle(head) -> bool:
    counter = {}
    curr = head.next if head else None
    while curr:
        counter[curr] = counter.get(curr, 0) + 1
        if counter[curr] > 1 or head in counter.keys():
            return True
        curr = curr.next
    return False


def has_cycle1(head) -> bool:
    visited_nodes = set()
    current_node = head
    while current_node:
        if current_node in visited_nodes:
            return True
        visited_nodes.add(current_node)
        current_node = current_node.next
    return False


def has_cycle2(head) -> bool:
    fast = head
    slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            return True
    return False
