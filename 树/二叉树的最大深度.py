'''给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        #left_max = self.maxDepth(root.left) + 1
        #right_max = self.maxDepth(root.right) + 1

        #return max(left_max, right_max)

        #case2

        q = [root]
        j = 0
        while q:
            next_level = []
            for i in q:
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)

            j += 1
            q = next_level

        return j
