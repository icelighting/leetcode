'''
给定整数n，计算小于n的所有质数
'''

class Solution:
    def countPrimes(self, n):## 埃拉托色尼筛选法求质数
        """
        :type n: int
        :rtype: int
        """
        x = [True] * (n + 1)
        p = 2
        while p * p < n:
            if x[p]:
                for i in range(p * 2, n , p):
                    x[i] = False
            p += 1
        return len([i for i in range(2, n) if x[i]])

if __name__ == '__main__':
    n = 10
    solute = Solution()
    print(solute.countPrimes(n))
