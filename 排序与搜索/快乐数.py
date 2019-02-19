'''
编写一个算法来判断一个数是不是“快乐数”。
一个“快乐数”定义为：对于一个正整数，
每一次将该数替换为它每个位置上的数字的平方和，
然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。
'''
'''
什么时候会无限循环呢
'''
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a = [n]
        def happy(n):
            str_n = str(n)
            l = len(str_n)
            sums = 0
            for i in str_n:
                sums += int(i) ** 2
            return sums
        while n != 1:
            n = happy(n)
            a.append(n)
            if len(list(set(a))) != len(a):
                return False
        return True

if __name__ == '__main__':
    n = 19
    solute = Solution()
    print(solute.isHappy(n))

