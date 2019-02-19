'''

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。
'''
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        s1 = self.climbStairs(n-1)
        s2 = self.climbStairs(n-2)
        return s1 + s2

    ## 注意到fn = fn-1 + fn-2 , 所以这实际上是一个斐波拉奇数列
    def case2(self,n):
        f1 = 1
        f2 = 2
        if n == 1:
            return f1
        for i in range(n-2):
            tmp = f2
            f2 = f1 + f2
            f1 = tmp

        return f2

if __name__ == '__main__':
    n = 3
    solute = Solution()
    print(solute.case2(3))
