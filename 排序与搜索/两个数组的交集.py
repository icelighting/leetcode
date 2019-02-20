'''
求两个数组元素的交际
'''
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = set(nums1)
        nums2 = set(nums2)
        x = nums1 & nums2## set集合可以直接使用& 来寻找交集
        return list(x)


if __name__ == '__main__':
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    solute = Solution()
    print(solute.intersection(nums1, nums2))
