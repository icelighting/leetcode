'''
给定两个非负整数 x 和 y，如果某一整数等于 x^i + y^j，其中整数 i >= 0 且 j >= 0，那么我们认为该整数是一个强整数。

返回值小于或等于 bound 的所有强整数组成的列表。

你可以按任何顺序返回答案。在你的回答中，每个值最多出现一次
'''

class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        a = 0## 超出了时间限制
        b = 0
        while x ** a <= bound:
            a += 1
        while y **b <= bound:
            b += 1
        l = []
        for i in range(a+1):
            for j in range(b +1):
                result = x** i + y** j
                if result <= bound:
                    l.append(result)

        return list(set(l))

    def case2(self, x, y, bound):
        l = []##还是超出时间限制
        a = 0
        b = 0
        while y**b <= bound:
            while x ** a +y ** b <= bound:
                l.append(x **a + y **b)
                a += 1
            a = 0
            b += 1

        return list(set(l))

    def case3(self, x, y, bound):
        


if __name__ == '__main__':
    x = 2
    y = 3
    bound = 10
    solute = Solution()
    print(solute.case2(x, y, bound))