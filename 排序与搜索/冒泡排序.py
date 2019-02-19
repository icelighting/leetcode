'''
现在，同样来实现以下冒泡排序吧
'''
class bumble():
    def al(self,nums):
        length = len(nums)
        for i in range(length- 1):
            for j in range(i+1, length-1):
                if nums[j] > nums[j+1]:
                    tmp = nums[j+1]
                    nums[j+1] = nums[j]
                    nums[j] = tmp

        return nums

if __name__ == '__main__':
    nums = [1, 5, 3, 4, 9, 8]
    solute = bumble()
    print(solute.al(nums))
