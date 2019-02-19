'''给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器，且 n 的值至少为 2。'''


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        left = 0
        right = length -1
        if not height or length == 1:
            return 0
        maxmum = 0
        while left < right:
            width = right - left
            heightness = min(height[right], height[left])
            plate = width * heightness
            if plate > maxmum:
                maxmum = plate
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxmum



if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    height2 = [2,3,4,5,18,17,6]
    solute = Solution()
    print(solute.maxArea(height2))