# https://leetcode.com/problems/find-largest-value-in-each-tree-row

# Было на собеседовании
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def largest_values(root: TreeNode) -> list[int]:
    level = 0
    if not root:
        return []
    q = [(root, level)]
    max_on_level = [root.val]
    top = 0
    while top < len(q):
        level = q[top][1] + 1
        if len(max_on_level) - 1 != level and (q[top][0].left or q[top][0].right):
            el = q[top][0].left.val if q[top][0].left else q[top][0].right.val
            max_on_level.append(el)
        if q[top][0].left:
            q.append((q[top][0].left, level))
            max_on_level[level] = max(max_on_level[level], q[top][0].left.val)
        if q[top][0].right:
            q.append((q[top][0].right, level))
            max_on_level[level] = max(max_on_level[level], q[top][0].right.val)
        top += 1

    return max_on_level


left = TreeNode(3, TreeNode(5), TreeNode(3))
right = TreeNode(2, right=TreeNode(9))
tree1 = TreeNode(1, left, right)

assert largest_values(tree1) == [1, 3, 9]
