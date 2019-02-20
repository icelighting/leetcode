'''
复现插入排序
'''
class insert():
    def al(self,nums):
        l = len(nums)
        for i in range(1,l):
            v = nums[i]
            j = i- 1
            while j >= 0 and nums[i] < nums[j]:
                nums[j+1], nums[j] = nums[j],nums[j+1]
                j -= 1
            nums[j+1] = v
        return nums


if __name__ == '__main__':
    nums = [1, 5, 3, 4, 9, 8]
    solute = insert()
    print(solute.al(nums))
