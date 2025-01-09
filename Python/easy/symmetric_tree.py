# https://leetcode.com/problems/symmetric-tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root: TreeNode) -> bool:
    def is_mirror(node1, node2):
        if not node1 and not node2:
            return True

        if not node1 or not node2:
            return False

        return (node1.val == node2.val and is_mirror(node1.right, node2.left)
                and is_mirror(node1.left, node2.right))

    return is_mirror(root.left, root.right)
