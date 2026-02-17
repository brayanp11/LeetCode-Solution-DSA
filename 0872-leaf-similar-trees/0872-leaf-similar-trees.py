# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaf(node):
            if node is None:
                return []

            if node.left is None and node.right is None:
                return [node.val]

            list_left = get_leaf(node.left)
            list_right = get_leaf(node.right)

            return list_left + list_right

        leaf1 = get_leaf(root1)
        leaf2 = get_leaf(root2)

        return leaf1 == leaf2