'''
给定一个字符串 (s) 和一个字符模式 (p)。实现支持 '.' 和 '*' 的正则表达式匹配。
'.' 匹配任意单个字符。
'*' 匹配零个或多个前面的元素。
匹配应该覆盖整个字符串 (s) ，而不是部分字符串。
'''

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        import re
        x = re.findall("^"+p+"$", s)
        return x[0] == s

    def case2(self,s ,p):
        m = len(s)
        n = len(p)
        dp = [[True] + [False] * m]
        for i in range(n):
            dp.append([False]*(m+1))

        for i in range(1, n + 1):
            x = p[i-1]
            if x == '*' and i > 1:
                dp[i][0] = dp[i-2][0]
            for j in range(1, m+1):
                if x == '*':
                    dp[i][j] = dp[i-2][j] or dp[i-1][j] or (dp[i-1][j-1] and p[i-2] == s[j-1]) or (dp[i][j-1] and p[i-2]=='.')
                elif x == '.' or x == s[j-1]:
                    dp[i][j] = dp[i-1][j-1]

        return dp[n][m]

    def case3(self, s, p):## 讲了两个表， 根据是都与表上对应将True 和 False 传递下去，最后看末尾时候为True 来判断整个列表是否都一致
        sn, pn = len(s), len(p)
        b = [False] * (sn + 1)
        b[0] = True
        i = 0
        while i < pn:
            c = p[i]
            i += 1
            if i < pn and p[i] == "*":
                if c == ".":
                    for j in range(sn):
                        if b[j]:
                            for k in range(j+1, sn+1):
                                b[k] = True
                            break
                else:
                    for j in range(sn):
                        if s[j] == c:
                            b[j+1] = b[j] or b[j+1]

                i += 1
            else:
                for j in reversed(range(sn)):
                    b[j+1] = b[j] and (s[j] == c or c == ".")
                b[0] = False
        return b[-1]

if __name__ == '__main__':
    s = "mississippi"
    p = "mis*is*p*."
    s1= "aa"
    p1 = "a*"
    solute = Solution()
    print(solute.isMatch(s1, p1))
