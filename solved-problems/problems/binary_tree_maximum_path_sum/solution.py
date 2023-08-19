# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:


        def findPathSum(root):
            nonlocal maxi

            if(not root):
                return 0

            leftSum = max(0,findPathSum(root.left))
            rightSum = max(0,findPathSum(root.right))

            maxi = max(maxi, leftSum + rightSum + root.val)

            return root.val + max(leftSum, rightSum)  

        maxi = -1e9   

        findPathSum(root)

        return maxi


