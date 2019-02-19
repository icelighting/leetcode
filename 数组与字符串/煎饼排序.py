'''

给定数组 A，我们可以对其进行煎饼翻转：
我们选择一些正整数 k <= A.length，然后反转 A 的前 k 个元素的顺序。
我们要执行零次或多次煎饼翻转（按顺序一次接一次地进行）以完成对数组 A 的排序。

返回能使 A 排序的煎饼翻转操作所对应的 k 值序列。
任何将数组排序且翻转次数在 10 * A.length 范围内的有效答案都将被判断为正确。
'''

class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if A == sorted(A):
            return []
        length = len(A)
        l = []
        for i in range(length):
            maximum = max(A[i:])
            l.append(A.index(maximum))
            A[i:] = A[i:][::-1]
        l.append(length)

        return l,A


if __name__ == '__main__':
    A = [3,2,4,1]
    solute = Solution()
    print(solute.pancakeSort(A))