class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Aim for O(n^2) time and space
        # use a hashset to find duplicate elements

        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        # find the index for each sequare 
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":  # if is an empty space, skip
                    continue
                if (board[r][c] in rows[r]      # if val already in rows[r], duplicate the row
                    or board[r][c] in cols[c]   # if val already in cols[c]. duplicate the column
                    or board[r][c] in squares[(r//3, c//3)]):   # keeps squares in 3x3 box
                    return False

                cols[c].add(board[r][c])    # add the digit to rows
                rows[r].add(board[r][c])    # add the digit to columns
                squares[(r//3), c//3].add(board[r][c])
        
        return True