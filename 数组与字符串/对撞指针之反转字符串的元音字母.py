'''
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
'''

class Solution(object):
    def reverseVowels(self, s):##超出时间限制
        """
        :type s: str
        :rtype: str
        """
        x = ''
        u = 'aeiouAEIOU'
        for i in s:
            if i in u:
                x += i
        p = 0
        print(list(x[::-1]))
        list_s = list(s)
        for i in range(len(list_s)):
            if list_s[i] in list(u):
                list_s[i] = list(x[::-1])[p]
                p += 1
        return ''.join(list_s)

    def p(self, s):##对撞指针的方法
        u = "aeiouAEIOU"
        i = 0
        j = len(s) - 1
        list_s = list(s)
        while i < j :
            if list_s[i] in u and list_s[j] in u:
                list_s[i], list_s[j] = list_s[j], list_s[i]
                i += 1
                j -= 1

            if list_s[i] not in u:
                i += 1
            if list_s[j] not in u:
                j -= 1

        return ''.join(list_s)

    def stack(self, p):## 利用列表，形成栈，出栈的思想，陷入后出
        u = "aeiouAEIOU"
        list_x = []
        for i in p:
            if i in u:
                list_x.append(i)
        res = ''
        for i in range(len(p)):
            if p[i] in u:
                res += list_x.pop()
            else:
                res += p[i]
        return res

if __name__ == '__main__':
    s = "hello world"
    solute = Solution()
    print(solute.stack(s))
