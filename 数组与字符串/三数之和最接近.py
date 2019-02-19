'''给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
找出 nums 中的三个整数，使得它们的和与 target 最接近。
返回这三个数的和。假定每组输入只存在唯一答案'''

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        '''thought :
        将 nums 分成三组,按小组进行排列'''
        import copy
        mum = 2**31
        ans = []
        ansValue = 0
        lenght = len(nums)
        n = target // 3
        m = target % 3
        set(nums)
        nums.sort()

        num1 = [data for data in nums if data <=n]
        num2 = [data for data in nums if n<data <= 2*n + m]
        num3 = [data for data in nums if 2*n +m < data]
        numlist = [num1, num2, num3]
        print(num1,num2,num3)
        length1 = len(num1)
        length2 = len(num2)
        length3 = len(num3)
        llist = [length1, length2, length3]
        while  0 in llist:
            a = llist.index(0)
            b = llist.index(max(llist))
            numlist[a].append(numlist[b][0])
            numlist[b].pop(0)
        for i in range(length1):
            for j in range(length2):
                for z in range(length3):
                    sum = num1[i] + num2[j] + num3[z]
                    if abs(sum-target) < mum:
                        mum = abs(sum - target)
                        ans = [num1[i], num2[j], num3[z]]
                        ansValue = sum

                    if sum - target == 0:
                        return target

        return ansValue

    def case2(self, nums, target):
        mums = 2**31
        ans = []
        ansValue = 0
        length = len(nums)
        n = length // 3
        m = length % 3
        nums.sort()
        num1 = nums[:n+m]
        num2 = nums[n+m:2*n+m]
        num3 = nums[2*n+m:]
        print(num1, num2, num3)
        length1 = len(num1)
        length2 = len(num2)
        length3 = len(num3)
        for i in range(length1):
            for j in range(length2):
                for z in range(length3):
                    sum = num1[i] + num2[j] + num3[z]
                    if abs(sum - target) < mums:
                        mums = abs(sum - target)
                        ans = [num1[i], num2[j], num3[z]]
                        ansValue = sum

                    if sum - target == 0:
                        return target

        return ansValue


    def case3(self, nums, target):
        mm = 2** 31
        res = 0
        nums.sort()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) -1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                diff = abs(sum - target)
                if diff < mm:
                    mm = diff
                    res = sum

                if target == sum:
                    return target
                if sum < target:
                    left += 1
                else:
                    right -= 1

        return res



if __name__ == '__main__':
    nums = [0,1,2]
    nums1 = [1,1,-1,-1,3]
    num2 = [-1, 2, 1, -4]
    solute =Solution()
    print(solute.case3(nums,5))

