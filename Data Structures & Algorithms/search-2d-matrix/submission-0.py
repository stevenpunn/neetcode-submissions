class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # goals is for O(log(m*n)) time and O(1) space
        # we can have a left and right pointer for each row
        # then we can bsearch for each row, if r < middle, instantly move to the next row
        ROWS, COLS = len(matrix), len(matrix[0])
        top = 0
        bottom = ROWS - 1
        while top <= bottom:
            row = (top + bottom) // 2   # bsearch over the rows
            if target > matrix[row][-1]:    # target < last element of the row, 
                top = row + 1               # move down a row
            elif target < matrix[row][0]:   # if target < first element
                bottom = row - 1            # move up a row
            else:
                break

        if not (top <= bottom):             # bsearch over row with target
            return False
        row = (top + bottom) // 2
        left = 0
        right = COLS - 1
        while left <= right:
            mid = (left + right) // 2
            if target > matrix[row][mid]:   # move left ptr to right half
                left = mid + 1
            elif target < matrix[row][mid]: # move right ptr to left half
                right = mid - 1
            else:
                return True
        return False