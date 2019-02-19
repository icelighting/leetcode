'''
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，
影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
'''
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        sum = 0
        i = 0
        while i < length:
            num = nums[i:i+2]
            maxmum = max(num)
            sum += maxmum
            if num.index(maxmum) == 1:
                i += 3
            else:
                i += 2
        x = 0
        sum2 = 0
        while x <length:
            sum2 += nums[x]
            x +=  2
        return max(sum, sum2)

if __name__ == '__main__':
    nums = [2,7,9,3,1]
    solute = Solution()
    print(solute.rob(nums))
