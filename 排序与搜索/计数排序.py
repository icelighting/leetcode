'''
实现一下计数排序
'''
class comparcount():
    def al(self, nums):
        l = len(nums)
        count =  [0] * l
        for i in range(l-1):
            for j in range(i+1,l):
                if nums[i] < nums[j]:
                    count[j] += 1
                else:
                    count[i] += 1
        S = [0] * l
        for i in range(l):
            S[count[i]] = nums[i]

        return S

if __name__ == '__main__':
    nums = [3 ,1, 5, 3, 4, 9, 8,2,7,6]
    solute = comparcount()
    print(solute.al(nums))
