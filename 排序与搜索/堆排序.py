'''
写一下堆排序
'''
from collections import deque
class dui():
    def al(self,nums):
        l = len(nums) - 1
        sort_count = l//2
        for i in range(sort_count):
            self.heapAdjust(nums, sort_count-i,l)

        for i in range(l-1):
            L = self.swap(nums,1,l-i)
            self.heapAdjust(nums,1,l-i-1)


        return [nums[i] for i in range(1,len(nums))]

    def swap(self,L,i,j):
        L[i],L[j] = L[j],L[i]
        return L

    def heapAdjust(self,L,start,end):
        temp = L[start]
        i = start
        j = 2 * i

        while j < end:
            if (j < end) and (L[j] < L[j+1]):
                j += 1
            if temp < L[j]:
                L[i] =  L[j]
                i = j
                j = 2 * i

            else:
                break

        L[i] = temp

if __name__ == '__main__':
    nums = [3 ,1, 5, 3, 4, 9, 8]
    nums = deque(nums)
    nums.appendleft(0)
    sol = dui()
    print(sol.al(nums))
