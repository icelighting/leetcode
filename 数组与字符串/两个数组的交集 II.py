'''
给定两个数组，
编写一个函数来计算它们的交集。
'''
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        A = [len(nums1),  len(nums2)]
        B = [nums1, nums2]
        index = A.index(min(A))
        list = []
        for i in B[index]:
            if i in B[1-index]:
                B[1-index].remove(i)
                list.append(i)
            else:
                continue

        return list
    def case2(self,nums1, nums2):
        tmp_dict = dict()
        ret = []
        for i in nums1:
            tmp_dict[i] = tmp_dict[i] + 1 if tmp_dict.get(i) else 1
        for n in nums2:
            if tmp_dict.get(n) > 0:
                ret.append(n)
                tmp_dict[n] -= 1
        return ret
    def case3(self, nums1, nums2):#利用字典的计数能力
        dicts = {}
        for i in nums1:
            if i in dicts:
                dicts[i] += 1
            else:
                dicts[i] = 1
        a = []
        for j in nums2:
            if j in dicts and dicts[j] > 0:
                a.append(j)
                dicts[j] -= 1

        return a

if __name__ == '__main__':
    nums1 = [4, 7, 9, 7, 6, 7]
    nums2 = [5, 0, 0, 6, 1, 6, 2, 2, 4]
    solute = Solution()
    print(solute.intersect(nums1,nums2))
