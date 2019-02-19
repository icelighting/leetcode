'''


给定一个整数数组 A，坡是元组 (i, j)，其中  i < j 且 A[i] <= A[j]。这样的坡的宽度为 j - i。

找出 A 中的坡的最大宽度，如果不存在，返回 0 。
'''


'''
2 <= A.length <= 50000
    0 <= A[i] <= 50000

'''

class Solution(object):
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if max(A) == A[0]:
            return None
        length = len(A)
        left = 0
        right = length -1
        maxi = 0
        while left < right:
            if A[left] <= A[right]:
                pLength = right - left
                return pLength
            else:
                pLength = 0
                if A[left] <= A[right-1] or A[left+1]>= A[left]:
                    right -= 1
                else:
                    left += 1
            if pLength > maxi:
                maxi = pLength

        return maxi

if __name__ == '__main__':
    A = [9,8,1,0,1,9,4,0,4,1]
    A2 = [2,2,1]
    A3 = [3,4,2,1]
    solute = Solution()
    print(solute.maxWidthRamp(A3))