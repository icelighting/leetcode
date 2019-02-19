class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length <= 1:
            return len(nums)
        s = 0
        for i in range(length-1):
            if nums[s] != nums[i+1]:
                s += 1
                nums[s] = nums[i+1]
        return s+1

if __name__ == '__main__':
    nums = [1,1,2]
    solute = Solution()
    print(solute.removeDuplicates(nums))