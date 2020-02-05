# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def check(self, root, n):
        if not root:
            return 0
        c = self.check(root.left, n) + root.val + self.check(root.right, n)
        self.res = max(self.res, (n-c)*c)
        return c
    def maxProduct(self, root: TreeNode) -> int:
        p = 1000000007
        def count(root):
            if not root:
                return 0
            return count(root.left) + count(root.right) + root.val
        n = count(root)
        self.res = 0
        _ = self.check(root, n)
        return self.res % p
