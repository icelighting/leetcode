'''给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000'''


class Solution:
    '''
    根据回文的特性，一个大回文按比例缩小后的字符串也必定是回文，比如ABCCBA，那BCCB肯定也是回文。所以我们可以根据动态规划的两个特点：
    （1）把大问题拆解为小问题
    （2）重复利用之前的计算结果
    这道题。如何划分小问题，我们可以先把所有长度最短为1的子字符串计算出来，根据起始位置从左向右，这些必定是回文。
    然后计算所有长度为2的子字符串，再根据起始位置从左向右。到长度为3的时候，我们就可以利用上次的计算结果：
    如果中心对称的短字符串不是回文，那长字符串也不是，如果短字符串是回文，那就要看长字符串两头是否一样。这
    样，一直到长度最大的子字符串，我们就把整个字符串集穷举完了。
            '''
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if s == "":
            return []
        self.dic = {}
        self.strlist = list(s)
        print('set self',set(self.strlist))
        print(self.strlist)
        length = len(self.strlist)
        if len(set(self.strlist)) == 1:
            return s
        for i in range(1,length-1):
            print('i',i)
            if self.strlist[i-1] != self.strlist[i+1]:
                continue
            else:
                num = min(i, length - i-1)
                if num == 1:
                    if self.strlist[i-1] == self.strlist[i+1]:
                        j = 1
                        self.dic[j] = "".join(self.strlist[i-1:i+2])
                else:
                    j = self.chooseJ(i, num)

                if i+j+1 <=length-1:
                    if set(self.strlist[i-j:i+j+1]) == set(self.strlist[i+j+1]):
                        self.dic[j+1] = "".join(self.strlist[i-j:i+j+2])
                if i-j-1 >= 0:
                    if set(self.strlist[i-j:i+j+1]) == set(self.strlist[i-j-1]):
                        self.dic[j+1] = "".join(self.strlist[i-j-1:i+j+1])


                '''if i < length- i -1:
                    if set(self.strlist[i-j:i+j+1]) == self.strlist[i+j+1]:
                        self.dic[j] = "".join(self.strlist[i-j:i+j+2])
                elif i > length - i - 1:
                    if set(self.strlist[i-j:i+j+1]) == self.strlist[i-j-1]:
                        self.dic[j] = "".join(self.strlist[i-j-1:i+j+1])
                else:
                    if i - j >= 0 and i+j <= length-1:
                        if set(self.strlist[i-j:i +j+1]) == self.strlist[i+j+1]:
                            self.dic[j] = "".join(self.strlist[i - j:i + j+2])
                        if set(self.strlist[i-j:i+j+1]) == self.strlist[i-j-1]:
                            self.dic[j] = "".join(self.strlist[i-j-1:i+j+1])'''

        liter = None
        if self.dic != {}:
            maximum = max(self.dic.keys())
            liter = self.dic[maximum]
        else:
            for a in range(length-1):
                if self.strlist[a] == self.strlist[a+1]:
                    liter = "".join(self.strlist[a:a+2])

            if liter == None:
                liter = self.strlist[0]
        return liter

    def chooseJ(self,i,num):
        number = 0
        for j in range(1, num):
            print('j',j)
            if self.strlist[i - j] == self.strlist[i + j]:
                continue
            else:
                print(self.strlist[i - j - 1:i + j])
                str_list = "".join(self.strlist[i - j:i + j+1])
                self.dic[j] = str_list
                number = j
                break
        return number

    def case2(self,s):
        maxlenth = 0##回文字符串的长度
        length = len(s)
        start = 0###回文起始点
        for i in range(length):
            if i - maxlenth >= 1 and s[i-maxlenth-1:i+1] == s[i-maxlenth-1:i+1][::-1] :
                start = i - maxlenth - 1
                maxlenth += 2

            if i - maxlenth >= 0 and s[i-maxlenth:i+1] == s[i-maxlenth:i+1][::-1] :
                start = i - maxlenth
                maxlenth += 1

        return s[start: start + maxlenth]
if __name__ == '__main__':
    s = "abbbb"
    solute = Solution()
    print(solute.case2(s))