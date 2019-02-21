'''
告别了三数之和，我们来到了四数之和
给定一个包含 n 个整数的数组 nums 和一个目标值 target
，判断 nums 中是否存在四个元素 a，b，c 和 d ，
使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
'''


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length < 4:
            return []
        ans = set()
        for i in range(length-3):
            if i > 1 and nums[i] == nums[i-1]:
                continue
            b = self.threeSum(i,nums,target)
            ans = ans | b
        return list(ans)


    def threeSum(self,i,nums,target):
        ret = set()
        length = len(nums)
        for j in range(i+1,length-2):
            if j > i +2  and nums[j] == nums[j-1]:
                continue
            l = j + 1
            r = length
            value = self.twoSum(i,j,l,r, nums, target)
            ret = ret | value
        return ret

    def twoSum(self,i,j,l,r,nums, target):
        n = r - l + 1
        if n < 2:
            return set()
        ret = set()
        dic = dict()
        for m in range(l, r):
            other = target - nums[i] - nums[j] - nums[m]
            if other in dic:
                ret.add(tuple(sorted([nums[i],nums[j], nums[m], other])))
            dic[nums[m]] = m
        return ret


if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    nums1 = [0, 0, 0, 0]
    nums2 = [-5,5,4,-3,0,0,4,-2]
    target = 4
    solute = Solution()
    print(solute.fourSum(nums2, target))
