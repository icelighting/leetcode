'''
给定一个字符串，请你找出其中不含有重复字符的
 最长子串 的长度。

'''

#思路:首先我想到的是,从两边设置两个指针,内家的形式,可以通过考察str里有没有重复元素来进行 判断
##问题在于我没有一个左右移动的好办法.什么时候左右移动呢

##思路2 来源于网上  初始化哈希表,字典. 字典的key值 记录的是字符,二
'''
这道题需要借助哈希查找key的O(n) 时间复杂度， 否则就会超时

　　 初始化一个 哈希表\字典  dic

头指针start 初始为0

当前指针 cur 初始为0

最大长度变量 l 初始为0

　　用cur变量从给定字符串str的开头开始 一位一位的向右查看字符，直到整个字符串遍历完， 对每一位字符进行如下：

　　　　当前位置的字符为 c = str[cur]

　　　　查询当前字符 c 是否 在哈希表dic的键 当中,表示 当前字符c 是否之前遍历到过

　　　　   如果 当前字符还没出现过，就 在dic中记录一个键值对  (当前字符c，当前位置cur )

　　　　　　cur 后移一位

　　　　   如果 当前字符出现过， 获取 当前字符串c 上次出现的位置 pre = dic[c]

　　　　　　如果pre 在 start后面即 pre>start， 则把start 移动到 pre的下一位， start = pre + 1， 这样保证cur继续向后遍历中 从start到cur没有重复元素

　　　　　　否则 start不动，start移动到某一个位置，说明在这个位置之前有重复的元素了，所以start只往后移动不往回移动

　　　　这时候在衡量一下  如果 cur - start + 1 (衡量当前没重复子串开头到结尾的长度) 比 长度变量 l 大， 那就替换 l 为  cur - start + 1
'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        length = len(s)
        left = 0
        right = length - 1
        l = 0
        middle = (right - left) // 2
        while left < right:

            if len(list(set(s[left:right+1]))) == len(list(s[left:right + 1])):
                strl = right - left + 1
                return strl
            else:
                strl = 1
                if len(list(set(s[left:middle+1]))) <= len(list(set(s[middle + 1: right+1]))):
                    left += 1
                else:
                    right -= 1
            if strl > l :
                l = strl
        return l

    def case2(self, s):
        start = 0
        l = 0
        dic = {}
        for i in range(len(s)):
            cur = s[i]
            if cur not in dic.keys():
                dic[cur] = i
            else:
                if dic[cur] > start:
                    start = dic[cur] + 1
                dic[cur] = i
            if i - start + 1 > l:
                l = i - start + 1

        return l


if __name__ == '__main__':

        s = "pwwkew"
        s1 = " "
        solute = Solution()
        print(solute.case2(s=" "))
        print(len(list(s1)))
