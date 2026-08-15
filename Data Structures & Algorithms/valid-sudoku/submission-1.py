class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)

        #Square would be
        #square = (row // 3, column // 3)
        squares = collections.defaultdict(set)

        #For row in specified range of 9x9
        for row in range(9):
            #For column in range of 9x9
            for col in range(9):
                #If there is no number continue to next digit
                if board[row][col] == ".":
                    continue
                #if the number is inside the rows list then dupe
                #If number is inside col list then dupe
                #if number is inside square then dupe
                if (board[row][col] in rows[row] or     
                    board[row][col] in cols[col] or
                    board[row][col] in squares[(row // 3, col // 3)]):
                    return False
                #Add number to row, col and square for checking above
                cols[col].add(board[row][col])
                rows[row].add(board[row][col])
                squares[((row // 3, col // 3))].add(board[row][col])
        return True





