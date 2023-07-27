# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        queue = [root]
        ans = []

        while queue:

            avg = 0
            length = len(queue)

            for i in range(length):

                node = queue.pop(0)

                avg += node.val

                if(node.left):
                    queue.append(node.left)

                if(node.right):
                    queue.append(node.right)
            
            avg /= length
            ans.append(avg)

        return ans     




