# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        temp = root.left
        root.left = root.right
        root.right = temp

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left,right) + 1
