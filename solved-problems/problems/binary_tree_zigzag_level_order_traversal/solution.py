# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if(not root):
            return []

        res = []
        flag = 0
        queue = [root]

        while queue:
            l = len(queue)
            temp = []

            for _ in range(l):

                node = queue.pop(0)
                temp.append(node.val)

                if(node.left):
                    queue.append(node.left)

                if(node.right):
                    queue.append(node.right)

            if(flag):
                temp[:] = temp[::-1]
                res.append(temp)
            else:
                res.append(temp)

            flag = not flag

        return res            




