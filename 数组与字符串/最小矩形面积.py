'''
给定在 xy 平面上的一组点，确定由这些点组成的任何矩形的最小面积，
其中矩形的边不一定平行于 x 轴和 y 轴。

如果没有任何矩形，就返回 0。

'''

'''
思路: 先要判断是否能构成矩形,利用值相等
可以吗? 对角定点坐标之和相等, 所以第一步, 先对横纵坐标进行筛选,找到相同的组把他们放在dict中
'''

class Solution(object):
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        from collections import defaultdict
        dic = defaultdict(list)
        length = len(points)
        x_list  = sorted(points,key=lambda points: points[0])
        for x, y in points:
            dic[x].append(y)
        seen = {}
        result = []
        for x2 in sorted(dic):
            column = dic[x2]
            column.sort()
            for a,b in enumerate(column):
                for i in range(a):
                    y1 = column[i]
                    if (x2, y1) in seen:
                        result.append((x2 - seen[b,y1]) *(b -y1))

        return result if result != float('inf') else 0





if __name__ == '__main__':
    points = [[3, 1], [1, 1], [0, 1], [2, 1], [3, 3], [3, 2], [0, 2], [2, 3]]
    solute = Solution()
    print(solute.minAreaFreeRect(points))