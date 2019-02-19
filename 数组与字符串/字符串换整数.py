'''请你来实现一个 atoi 函数，使其能将字符串转换成整数。
首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。
当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。
该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。
注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。
在任何情况下，若函数不能进行有效的转换时，请返回 0。
说明：
假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，qing返回  INT_MAX (231 − 1) 或 INT_MIN (−231)
'''


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        strList = list(str)
        while ' ' in strList:
            strList.remove(' ')

        print('strlist',strList)
        str_new = "".join(strList)
        print('str_new',str_new)
        try:
            num = int(str_new)
        except ValueError:
            return 0
        if num < - 2**31:
            num = -2**31
        elif num > 2** 31 -1:
            num = 2**31 -1

        return num

    def MyAtoi(self,str):
        import re

        ret = re.findall(r"^[-+]?\d+", str.strip())
        print(ret)
        if ret:
            ret_str = ret[0]
            ret_str2 = ""
            if ret_str[0] == "-" or ret_str[0] == "+":
                ret_str2 = ret_str[1:]
            else:
                ret_str2 = ret_str

            ret_int = int(ret_str2)

            if ret_str[0] == "-":
                return  - ret_int  if ret_int <= 2**31 else -2 **31
            else:
                return ret_int if ret_int < 2**31-1 else 2**31-1

        else:
            return 0

    def case2(self,str):
        import re
        str_filter = re.findall(r'[-]?\d+', str)
        print(str_filter)
        str_filter2 = re.findall(r'\d', str)
        if int(str_filter[0]) < 0:
            x = -int(''.join(str_filter2))
        else:
            x = int(''.join(str_filter2))

        if x > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if x < -2 ** 31:
            return -2 ** 31

        return x
if __name__ == '__main__':
    str = "    -49"
    solute = Solution()
    print(solute.case2(str))
