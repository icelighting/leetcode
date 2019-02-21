'''

给定四个包含整数的数组列表 A , B , C , D ,
计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。
为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。
所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。
'''
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        from collections import defaultdict
        length = len(A)
        dict1 = defaultdict(int)
        for i in A:
            for j in B:
                dict1[i + j] += 1


        dict2 = defaultdict(int)
        for i in C:
            for j in D:
                dict2[i + j] += 1

        count = 0
        for item in dict1.keys():
            if -item in dict2:
                count += dict1[item] * dict2[-item]## 这个地方用乘比较好，因为如果存在多个等于-item的，都可以表示出来，而不是单纯的价格1

        return count

if __name__ == '__main__':
    A = [ 1, 2]
    B = [-2,-1]
    C = [-1, 2]
    D = [ 0, 2]
    solute = Solution()
    print(solute.fourSumCount(A,B,C,D))

