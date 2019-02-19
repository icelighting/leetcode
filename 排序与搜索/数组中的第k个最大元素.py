'''

'''


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        length = len(nums)
        nums.sort()
        return nums[length-1-k]


if __name__ == '__main__':
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    solute = Solution()
    print(solute.findKthLargest(nums, k))