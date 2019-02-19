'''

给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
'''

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections
        dic = collections.Counter(s)
        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i

        return -1
    def case2(self, s):

        ## 利用 find 函数 找到字符传中对应字符的位置,rfind 可以找到更多的相同的字符的位置, 再比如rindex
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        p = len(s)
        for i in alphabet:
            if s.find(i) != -1 and s.find(i) == s.rfind(i):
                p = min(p, s.find(i))
        return p if p != len(s) else -1


if __name__ == '__main__':
    s = "leetcode"
    solute = Solution()
    print(solute.firstUniqChar(s))