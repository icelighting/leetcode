'''
编写一个函数，其作用是将输入的字符串反转过来。
'''


class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        sList = list(s)
        length = len(sList)
        s_list = []
        for i in range(length):
            s_list.append(sList[length-i-1])

        return "".join(s_list)



if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    solute = Solution()
    print(solute.reverseString(s))