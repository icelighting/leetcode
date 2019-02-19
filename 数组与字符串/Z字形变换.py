'''
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N

之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);

'''

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) <= numRows:
            return
        import collections
        dic = collections.defaultdict(list)
        op = numRows + numRows - 2
        for i in range(1,len(s) +1):
            if 0< i % op <= numRows:
                 dic[i%op].append(s[i-1])
            elif i % op == 0:
                dic[2].append(s[i-1])
            else:
                dic[2* numRows - i%op ].append(s[i-1])

        outputList = []
        for key in dic.keys():
            outputList.extend(dic[key])
        return "".join(outputList)
    def case3(self,s, numRows):
        if numRows == 1 or len(s) <= numRows:
            return s
        op = 2*numRows -2
        strList = [''] * numRows
        for i in range(1, len(s)+1):
            if 0< i%op <= numRows:
                strList[i%op-1] += s[i-1]
            elif i%op == 0:
                strList[1] += s[i-1]
            else:
                strList[2*numRows-i%op-1] += s[i-1]

        return ''.join(strList)


    def case2(self,s, numRows):
        if len(s) < numRows or numRows == 1:
            return s
        dp = [''] * numRows # 这里相当于,创建了一个列表中的列表,只不过用字符串来表示列表
        index = 0
        step = 1
        for i in s:
            dp[index] += i
            index += step
            if index == numRows - 1:
                step = -1
            if index == 0:
                step = 1
        return ''.join(dp)




if __name__ == '__main__':
    s = "LEETCODEISHIRING"
    numRows = 4
    solute = Solution()
    print(solute.case3(s, numRows))