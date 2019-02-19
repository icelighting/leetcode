'''

给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。
'''
## 思路: 回文数字符串, 以中心为对称, 那么相应的异或应该等于0
### 没那么困难 ,直接判断,列表反过来根正者是否一样就好了  Python isalnum() 方法检测字符串是否由字母和数字组成。
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        s_filter = re.findall(r'\w',s.lower())
        return s_filter == s_filter[::-1]


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    solute = Solution()
    print(solute.isPalindrome(s))