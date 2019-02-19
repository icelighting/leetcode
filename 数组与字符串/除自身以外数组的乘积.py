'''
给定长度为 n 的整数数组 nums,
其中 n > 1，返回输出数组 output ，
其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
'''

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length =len(nums)
        numList = list(range(length))
        counter = 1

        for i in range(length):
            if nums[i] == 0:
                continue
            else:
                counter *= nums[i]

        if nums.count(0) == 0:
            for j in range(length):
                numList[j] = int(counter / nums[j])
        elif nums.count(0) == 1:
            for j in range(length):
                if j == nums.index(0):
                    numList[j] = counter
                else:
                    numList[j] = 0
        else:
            for j in range(length):
                numList[j] = 0
        return numList



if __name__ == '__main__':
    nums = [1,2,3,4]
    nums2 = [0, 0, 0, 0]
    solute = Solution()
    print(solute.productExceptSelf(nums2))