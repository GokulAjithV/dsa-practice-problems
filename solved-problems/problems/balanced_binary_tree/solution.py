# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def findHeight(root):
            if(not root):
                return 0

            lh = findHeight(root.left)
            rh = findHeight(root.right)

            if(abs(lh-rh) > 1):
                return -1

            if(lh == -1 or rh == -1):
                return -1         

            return 1 + max(lh,rh)

        return findHeight(root) >= 0     

