# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def findHeight(node):

            if(not node):
                return 0

            lh = findHeight(node.left)
            rh = findHeight(node.right)

            return 1 + max(lh,rh)

        def dfs(root):
            nonlocal maxi

            if(not root):
                return 

            lh = findHeight(root.left)
            rh = findHeight(root.right)

            maxi = max(maxi,lh+rh)

            dfs(root.left)
            dfs(root.right)

            return 

        maxi = 0

        dfs(root)   

        return maxi 

                       