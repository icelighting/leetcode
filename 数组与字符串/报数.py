'''
报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221

1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。

注意：整数顺序将表示为一个字符串。
'''

##思路: 利用递归 对于报数进行读取

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        x = "1"
        a = 1
        while a < n:
            x = self.recursion(x)
            a += 1

        return x




    def recursion(self, x):
        length = len(x)
        if length == 1:
            return "1"+x
        else:
            count = 1
            op = ""
            for i in range(length -1):
                if x[i] == x[i+1]:
                    count += 1
                else:
                    op += str(count) + str(x[i])
                    count = 1
            if x[-1] != x[-2]:
                op += "1"+x[-1]
            else:
                op += str(count) + x[-1]

            return op



if __name__ == '__main__':
    n = 6
    solute = Solution()
    print(solute.countAndSay(n))