'''
给定一个包含 m x n 个元素的矩阵（m 行, n 列），
请按照顺时针螺旋顺序，返回矩阵中的所有元素。
'''
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])
        rotatematrix = []
        while matrix != []:
            for i in range(m):
                for j in range(n):
                    if i == 0 or i == m-1 or j == 0 or j == n-1:
                        rotatematrix.append(matrix[i].pop(0))
                if matrix[i] == []:
                    matrix.remove([])

            self.spiralOrder(matrix)

        return rotatematrix

    def case2(self, matrix):
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        if n == 0:
            return []
        self.rotatematrix = []
        self.rotateOperation(m,n,matrix)
        return self.rotatematrix

    def rotateOperation(self,m,n,matrix):
        counter = [0, 0]
        if m == n == 1:
            self.rotatematrix.append(matrix[0][0])
        elif m > 1 and n> 1:
            while counter[1]< n-1:
                self.rotatematrix.append(matrix[counter[0]][counter[1]])
                counter[1] += 1

            while counter[0] < m-1:
                self.rotatematrix.append(matrix[counter[0]][counter[1]])
                counter[0] += 1

            while counter[1]> 0:
                self.rotatematrix.append(matrix[counter[0]][counter[1]])
                counter[1] -= 1

            while counter[0] > 0:
                self.rotatematrix.append(matrix[counter[0]][counter[1]])
                counter[0] -= 1

        elif m == 1 and n > 1:
            for i in range(n):
                self.rotatematrix.append(matrix[0][i])
        elif m > 1 and n == 1:
            for i in range(m):
                self.rotatematrix.append(matrix[i][0])

        if m >= 2:
            matrix.pop(0)
            matrix.pop()

            if matrix == []:
                return self.rotatematrix
            else:
                if len(matrix[0]) >= 2:
                    for i in range(m - 2):
                        matrix[i].pop(0)
                        matrix[i].pop()
            if [] in matrix:
                return self.rotatematrix
            self.rotateOperation(m-2,n-2,matrix)

        else:
            #self.rotatematrix.extend(matrix[0])
            return self.rotatematrix

    def case3(self,matrix):
        if not matrix: return []
        row, col = len(matrix), len(matrix[0])
        seen = [[False] * col for _ in matrix]
        res = []
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for i in range(row * col):
            res.append(matrix[r][c])
            seen[r][c] = True
            pr = r + dr[di]
            pc = c + dc[di]
            if 0 <= pr < row and 0 <= pc < col and not seen[pr][pc]:
                r = pr
                c = pc
            else:
                di = (di + 1) % 4
                r += dr[di]
                c += dc[di]
        return res



if __name__ == '__main__':
    matrix =  [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
    ]
    matrix5 = [[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]

    matrix2 = [[1,2,3],[4,5,6],[7,8,9]]
    matrix3 = [[3,2,6]]
    matrix4 = [[1, 2], [3, 4]]
    solute = Solution()
    print(solute.case3(matrix5))