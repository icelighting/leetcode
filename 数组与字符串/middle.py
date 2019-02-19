'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。
'''

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1 = sorted(nums1)
        print(nums1)
        lenth = len(nums1)
        m = int(lenth // 2)
        print(m)
        if lenth % 2 == 0:
            middle = (nums1[m-1] + nums1[m]) / 2
        else:
            middle = nums1[m]

        return middle

if __name__ == '__main__':
    num1 = [1,3]
    num2 = [2]
    solute = Solution()
    print(solute.findMedianSortedArrays(num1,num2))