'''
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。
'''
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)#暴力搜索法
        sums = 10000
        for i in range(l-1):
            for j in range(i,l):
                if nums[i] + nums[j] > s:
                    if j - i + 2< sums:
                        sums = j - i +2

        return sums


    def twoDivided(self, s, nums):


if __name__ == '__main__':
    s = 7
    nums = [2,3,1,2,4,3]
    solute = Solution()
    print(solute.minSubArrayLen(s,  nums))
