class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if val in squares[ (r//3 ,c//3) ]  or val in cols[c] or val in rows[r]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                squares[(r//3,c//3)].add(val)
        return True