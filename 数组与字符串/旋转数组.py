'''
给定一个数组，将数组中的元素向右移动 k 个位置，
其中 k 是非负数。
'''
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        for i in range(len(nums)-k):
            nums.extend([nums[0]])
            nums.pop(0)
        return nums

    def case2(self, nums, k):
        nums[:] = nums[-(k % len(nums)):] + nums[:-(k % len(nums))]

        return nums

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    solute = Solution()
    print(solute.rotate(nums, k))