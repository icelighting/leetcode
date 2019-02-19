'''
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

    数字 1-9 在每一行只能出现一次。
    数字 1-9 在每一列只能出现一次。
    数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。


'''
##思路:对于数独正确与否的一条条筛选,判断


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        symbol = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for item in board:
            row = [data for data in item if data in symbol]
            if len(set(row)) != len(row):
                return False

        for j in range(len(board[0])):
            column = [i[j] for i in board if i[j] in symbol]
            if len(set(column)) != len(column):
                return False

        rownum = 0
        colnum = 0
        while rownum <= 6:
            while colnum <= 6:
                x = []
                for a in range(rownum, rownum + 3):
                    for b in range(colnum, colnum + 3):
                        if board[a][b] in symbol:
                            x.append(board[a][b])
                        if len(set(x)) != len(x):
                            return False

                colnum += 3

            rownum += 3

        return True

    def case2(self, board):
        ## 利用字典对 矩阵扫描储存
        ##  牺牲储存 换取效率
        ## 字典的索引效率要远远高于列表
        #列表根据偏移量,而字典根据键的hash完成的

        dic_row = [{} for i in range(len(board))]
        dic_column = [{} for i in range(len(board))]
        dic_box = [{} for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board)):
                num = board[i][j]
                if num == ".":
                    continue

                if num not in dic_row[i] and num not in dic_column[j] and num not in dic_box[3 * (i // 3) + (j // 3)]:
                    dic_row[i][num] = 1
                    dic_column[j][num] = 1
                    dic_box[3 * (i // 3 )+ (j // 3)][num] = 1
                else:
                    return False


        return True






if __name__ == '__main__':
    board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

    board2 = [[".",".","4",".",".",".","6","3","."],
            [".",".",".",".",".",".",".",".","."],
          ["5",".",".",".",".",".",".","9","."],
          [".",".",".","5","6",".",".",".","."],
          ["4",".","3",".",".",".",".",".","1"],
          [".",".",".","7",".",".",".",".","."],
          [".",".",".","5",".",".",".",".","."],
          [".",".",".",".",".",".",".",".","."],
          [".",".",".",".",".",".",".",".","."]]
    solute = Solution()
    print(solute.case2(board))