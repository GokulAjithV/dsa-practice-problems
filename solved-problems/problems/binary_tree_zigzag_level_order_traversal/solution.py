# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if(not root):
            return root

        queue = [root]
        ans = [[root.val]]
        flag = 0

        while queue:

            temp = []
            

            for i in range(len(queue)):

                node = queue.pop(0)

                if(node.left):
                    queue.append(node.left)
                    temp.append(node.left.val)
                if(node.right):
                    queue.append(node.right)
                    temp.append(node.right.val)
            
            if(not flag):
                temp.reverse()
            flag = not flag
            if(temp):
                ans.append(temp)       

        return ans


