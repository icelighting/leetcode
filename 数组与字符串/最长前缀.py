'''编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。'''


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1 :
            return strs[0]
        if not strs:
            return " "
        minL = min([len(item) for item in strs])
        end = 0
        while end < minL:
            for i in range(1,len(strs)):
                if strs[i][end] != strs[i-1][end]:
                    if end == 0:
                        return " "
                    else:
                        return strs[0][:end]
            end += 1


        return strs[0][:end]

    def case2(self,strs):
        res = ""
        if len(strs) == 0:
            return ""
        for each in zip(*strs):  # zip()函数用于将可迭代对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
          if len(set(each)) == 1:#利用集合创建一个无序不重复元素集
            res += each[0]
          else:
            return res
        return res


if __name__ == '__main__':
    str = ["a","a"]
    solute = Solution()
    print(solute.longestCommonPrefix(str))
    print(solute.case2(str))