# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        money = 0
        memo = {}
        def dfs(node):
            if not node:
                return 0
            if node in memo:
                return memo[node]
            left,right = 0,0

            if node.left:
                left = dfs(node.left.left) + dfs(node.left.right)
            if node.right:
                right = dfs(node.right.left) + dfs(node.right.right)

            pick = node.val + left + right
            skip = dfs(node.left) + dfs(node.right)
            memo[node] = max(pick,skip)
            return memo[node]

        return dfs(root)
        