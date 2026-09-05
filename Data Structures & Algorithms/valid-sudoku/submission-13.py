class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        squared = defaultdict(list)
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if val in rows[r] or val in cols[c] or val in squared[r//3, c//3]:
                    return False
                else:
                    rows[r].append(val)
                    cols[c].append(val)
                    squared[r//3, c//3].append(val)
        return True