# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def findSym(leftroot,rightroot):

            if(not leftroot and not rightroot):
                return True 

            if(not leftroot or not rightroot):
                return False

            if(leftroot.val != rightroot.val):
                return False 

            return (findSym(leftroot.left,rightroot.right) and findSym(leftroot.right,rightroot.left)) 

        if(not root):
            return True 

        return findSym(root.left,root.right)    

        


