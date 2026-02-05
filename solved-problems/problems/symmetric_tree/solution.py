# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def checkSym(p,q):

            if(not p or not q):
                return p == q

            if(p.val != q.val):
                return False

            if(not checkSym(p.left,q.right) or not checkSym(p.right,q.left)):
                return False

            return True

        return checkSym(root.left,root.right)                   

        


