# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dm=0
        
        #return Height
        def dfs(curr):
            if curr==None:
                return 0
            lefth=dfs(curr.left)
            righth=dfs(curr.right)
            self.dm=max(self.dm,lefth+righth)
            return 1+max(lefth,righth)
        dfs(root)
        return self.dm
        