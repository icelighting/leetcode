'''
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，
且元素按顺时针顺序螺旋排列的正方形矩阵。
'''

class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        nlist = list(range(1,n**2+1))
        matrix = []
        for i in range(n):
            matrix.append(list(range(n)))
        print(matrix)
        counter = [0,0]
        s= 0
        m = n // 2
        for i in range(m):
            while counter[1] < n -1:
                matrix[counter[0]+i*1][counter[1]+i*1] = nlist[s]
                s += 1
                counter[1] += 1

            while counter[0] < n -1:
                matrix[counter[0]+i*1][counter[1]+i*1] = nlist[s]
                s += 1
                counter[0] += 1

            while counter[1] > 0:
                matrix[counter[0]+i*1][counter[1]+i*1] = nlist[s]
                s += 1
                counter[1] -= 1

            while counter[0] > 0:
                matrix[counter[0]+i*1][counter[1]+i*1] = nlist[s]
                s += 1
                counter[0] -= 1

            n -= 2
        if n % 2 != 0:
            matrix[m][m] = nlist[-1]
        return matrix
if __name__ == '__main__':
    n = 3
    solute = Solution()
    print(solute.generateMatrix(7))