'''
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。
'''

#思路: 需要判断整个单词的元素是否都一样,另外就是判断是否导致完全一致的问题
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s and not t:## 这里要考虑 s 和 t 都没有元素的情况,应该返回True
            return True
        elif s == t:
            return False
        if len(s) != len(t):
            return False
        import collections
        dic1 = collections.Counter(s)
        dic2 = collections.Counter(t)
        if dic1 == dic2:
            return True
        else:
            return False

if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    solute = Solution()
    print(solute.isAnagram(s, t))