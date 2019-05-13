'''
link: https://leetcode.com/problems/valid-sudoku
'''


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        f=''
        s=set()
        for i in board:
            for j in i :
                if j.isdigit():
                    if j not in s:
                        s.add(j)
                    else:
                        f='f'
                        return False
            s.clear()


        for k in range(9):
            for i in range(9):
                if board[i][k].isdigit():
                    if board[i][k] not in s:
                        s.add(board[i][k])
                    else:
                        return False
            s.clear()



        for j in range(3):

            for i in range(3):
                for x in range(3):
                    for y in range (3):

                        if board[(j*3+y)][(i*3)+x].isdigit():
                            if board[(j*3+y)][(i*3)+x] not in s:
                                s.add(board[(j*3+y)][(i*3)+x])
                            else:
                                f='f'
                                return False
                s.clear()



        if f!='f':
            return True
