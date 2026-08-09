class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = {}
        cols = {}
        boxes = {}

        for i in range(9):

            for j in range(9):

                num = board[i][j]

                if num == ".":
                    continue

                if i not in rows:
                    rows[i] = set()

                if j not in cols:
                    cols[j] = set()

                box = (i // 3, j // 3)

                if box not in boxes:
                    boxes[box] = set()

                if (
                    num in rows[i]
                    or num in cols[j]
                    or num in boxes[box]
                ):
                    return False

                rows[i].add(num)
                cols[j].add(num)
                boxes[box].add(num)

        return True