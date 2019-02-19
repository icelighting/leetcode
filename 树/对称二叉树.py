'''
给定一个二叉树，检查它是否是镜像对称的。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #case1 : 采用递归方法
        if not root:
            return True
        def symmetric(left,right):
            if not left and not right:
                return True
            if left and right and left.val == right.val:
                l =  symmetric(left.left, right.right)
                r = symmetric(right.left, left.right)
                return l and r
            else:
                return False

        return symmetric(root.left, root.right)

    #case2 试图采用一下迭代的方法, 迭代，意思可以是将一代一代的列出来，采用广度优先的算法，因为是对称的，所以肯定是回文的
    def case2(self, root):
        q = [root]
        while q:
            next_level = []
            for i in q:
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
            if next_level != next_level[::-1]:
                return False
            q =  next_level

        return True

