'''
在大小为 2N 的数组 A 中有 N+1 个不同的元素，其中有一个元素重复了 N 次。

返回重复了 N 次的那个元素。
'''

class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        length = len(A)
        A.sort()
        if A[0] == A[int(length/2)]:
            return A[0]
        elif A[int(length /2)] == A[length  -1]:
            return A[length -1]
        else:
            return A[int(length /2)-1]

if __name__ == '__main__':
    A = [5,1,5,2,5,3,5,4]
    solute = Solution()
    print(solute.repeatedNTimes(A))