'''
给定一个字符串，
你需要反转字符串中每个单词的字符顺序，
同时仍保留空格和单词的初始顺序。
'''

class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sList = list(s)
        sList.append(' ')
        print(sList)
        bigList = []
        alist = []
        for i in sList:
            if i != ' ':
                alist.append(i)
            else:
                bigList.append(alist)
                alist = []
        s_list = []
        for m in range(len(bigList)):
            n = len(bigList[m])
            for j in range(n):
                s_list.append(bigList[m][n-j-1])
                if j == n-1 and m != len(bigList) -1:
                    s_list.append(' ')

        return  "".join(s_list)



if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    solute = Solution()
    print(solute.reverseWords(s))