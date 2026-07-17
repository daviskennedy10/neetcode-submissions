# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node, res):
            if not node:
                return
            dfs(node.left, res)
            res.append(node.val)
            dfs(node.right, res)
        res = []
        if k == 0:
            return root
        dfs(root,res) 
        ans = 0
        for i in range(k):
            ans = res[i]
        return ans