class Solution:
    def invertTree(self, root):
        if root is None:
            return None

        root.left, root.right = root.right, root.left

        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)

        return root

