'''
 给定一个整数数组，判断是否存在重复元素。
如果任何值在数组中出现至少两次，函数返回 true。
如果数组中每个元素都不相同，则返回 false
'''

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length1 = len(nums)
        length2 = len(list(set(nums)))
        if length1 == length2:
            return False
        else:
            return True

if __name__ == '__main__':
    nums = [1,1,1,3,3,4,3,2,4,2]
    solute = Solution()
    print(solute.containsDuplicate(nums))
