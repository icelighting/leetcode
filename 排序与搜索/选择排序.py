'''
啥也别说了
来实现一下选择排序吧
'''
class select():
    def al(self,nums):
        length = len(nums)
        for i in range(length-1):
            mimum = nums[i]
            idx = i
            for j in range(i,length):
                if nums[j] < mimum:
                    mimum = nums[j]
                    idx = j
            if idx != i :
                tmp = nums[i]
                nums[i] = mimum
                nums[idx] = tmp

        return nums
if __name__ == '__main__':
    nums = [1, 5, 3, 4, 9, 8]
    solute = select()
    print(solute.al(nums))

