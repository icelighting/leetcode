'''

给定一个二叉搜索树，编写一个函数
kthSmallest
来查找其中第 k 个最小的元素。
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.count=k
        self.res=0
        def core(root):
            if root :
                core(root.left)
                self.count=self.count-1
                if self.count==0:
                    self.res=root.val
                core(root.right)
        core(root)
        return self.res
