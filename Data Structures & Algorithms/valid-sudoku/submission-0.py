class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {x:[0]*9 for x in range(0,9)}
        cols = {x:[0]*9 for x in range(0,9)}
        boxes = {x:[0]*9 for x in range(0,9)}

        for i in range(len(board)):
            for j in range(len(board[i])):
                if(board[i][j].isdigit()):
                    cur = board[i][j]
                    rows[i][int(cur)-1] += 1
                    cols[j][int(cur)-1] += 1
                    if(i < 3):
                        if(j < 3):
                            boxes[0][int(cur)-1] += 1
                        elif(j < 6):
                            boxes[3][int(cur)-1] += 1
                        else:
                            boxes[6][int(cur)-1] += 1
                    elif(i < 6):
                        if(j < 3):
                            boxes[1][int(cur)-1] += 1
                        elif(j < 6):
                            boxes[4][int(cur)-1] += 1
                        else:
                            boxes[7][int(cur)-1] += 1
                    else:
                        if(j < 3):
                            boxes[2][int(cur)-1] += 1
                        elif(j < 6):
                            boxes[5][int(cur)-1] += 1
                        else:
                            boxes[8][int(cur)-1] += 1
        for i in range(0, 9):
            for j in range(0, 9):
                if rows[i][j] > 1:
                    return False
                if cols[i][j] > 1:
                    return False
                if boxes[i][j] > 1:
                    return False
        return True