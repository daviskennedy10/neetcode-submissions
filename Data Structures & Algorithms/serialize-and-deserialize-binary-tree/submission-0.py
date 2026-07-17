# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.res = []
        def dfs(root):
            if not root:
                self.res.append("#")
                return
            self.res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return ",".join(self.res)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.tokens = iter(data.split(','))
        def build():
            val = next(self.tokens)
            if val == "#":
                return None
            number = TreeNode(int(val))
            number.left = build()
            number.right = build()
            return number

        return build()

        
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))