# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        def helper(vertical,level,root,dic):
            if(not root):
                return 

            dic[vertical].append((level,root.val))
            helper(vertical-1,level+1,root.left,dic)
            helper(vertical+1,level+1,root.right,dic)

        def verticalOrder(root):
            dic = defaultdict(list)
            helper(0,0,root,dic) 
            res = []
            for i in sorted(dic.keys()):
                temp = []
                for j in sorted(dic[i]):
                    temp.append(j[1])

                res.append(temp[:])

            return res

        return verticalOrder(root)                         
