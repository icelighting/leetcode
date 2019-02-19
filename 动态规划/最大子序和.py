'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
'''
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        MaxSum = nums[0]
        for i in range(len(nums)):
            sum += nums[i]
            if sum > MaxSum:
                MaxSum = sum
            if sum < 0:
                sum = 0
        return MaxSum

if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    solute = Solution()
    import  time
    start = time.time()
    print(solute.maxSubArray(nums))
    end = time.time()
    print(end - start)
