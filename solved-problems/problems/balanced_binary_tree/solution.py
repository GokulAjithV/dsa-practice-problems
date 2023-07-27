# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def findHeight(node):

            if(not node):
                return 0

            lh = findHeight(node.left)
            rh = findHeight(node.right)

            if(lh < 0 or rh < 0):
                return -1

            if(abs(lh-rh) > 1):
                return -1                    



            return max(lh,rh) + 1

        return findHeight(root) >= 0

