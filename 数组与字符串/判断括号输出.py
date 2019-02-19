'''给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。'''

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        d = {'{':'}','(':')','[':']'}
        stack = []
        length = len(s)
        if length % 2 != 0 or length == 0:
            return False
        for i in s:
            if i in d:##这里判断的是 是否与d中的keys 相一致也是就如果是
                stack.append(i)##这里如果是前括号就全部储存起来

            else:#如果是后括号
                if not stack or d[stack.pop()] != i:## 这里not stack 就包括了第一个符号不是前括号的情况,后面的条件满足如果是后括号
                    #上一个对应的不是同一个前括号
                    ##如果两两成对,而且保持均匀, 最后会被完全清除 只剩[]
                    return False


        return stack == []

    def case2(self, s):
        a = {')': '(', ']': '[', '}': '{'}
        l = [None]
        for i in s:
            if i in a and a[i] == l[-1]:
                l.pop()
            else:
                l.append(i)
        return len(l) == 1
    ## 这里就是利用后括号进行处理
    ## 大概就是把前后括号分开 进行配对,能配则成功不能配则失败







if __name__ == '__main__':
    s = ""
    d1 = "()[]{}"
    solute = Solution()
    print(solute.case2(d1))