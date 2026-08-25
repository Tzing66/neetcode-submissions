from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range (9):

                value = board[r][c]

                if value == '.':
                    continue
                
                boxkey = (r//3, c//3)

                if value in rows[r] or value in columns[c] or value in boxes[boxkey]:
                    return False
                
                rows[r].add(value)
                columns[c].add(value)
                boxes[boxkey].add(value)

        
        return True
                
        