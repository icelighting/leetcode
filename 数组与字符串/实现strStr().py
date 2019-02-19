'''

实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle
字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle not in haystack:
            return -1
        if haystack == needle:##
            return 0
        for i in range(len(haystack) - len(needle) + 1):##这个循环无法判断的条件是, haystac和 needle的长度一样,这里的len就变成了0 所以先提前一步把它另做判断
            if haystack[i:i+len(needle)] == needle:
                return i

    def case2(self, haystack, needle):
        if len(needle) == 0:
            return 0
        res = haystack.split(needle)## 利用split这个函数 将字符串切割出来
        if len(res) == 1:
            return -1

        return len(res[0])




if __name__ == '__main__':
    haystack = "hello"
    needle = "ll"
    haystack2 = "mississippi"
    needle2 = "pi"
    solute = Solution()
    print(solute.strStr(haystack2, needle2))