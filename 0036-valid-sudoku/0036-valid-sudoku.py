class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N=9
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        for r in range(0,N):
            for c in range(0,N):
                val = board[r][c]
                if val == ".":
                    continue
                if int(val) in rows[r]:
                    return False
                rows[r].add(int(val))
                if int(val) in cols[c]:
                    return False
                cols[c].add(int(val))
                boxIdx = (r//3)*3 + c//3
                if int(val) in boxes[boxIdx]:
                    return False
                boxes[boxIdx].add(int(val)) 
        return True