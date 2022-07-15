class Board:
    def swapPositions(self, position):
        for i in range(len(position)):
            if(position[i] == "W"):
                position[i] = "B"
            elif(position[i] == "B"):
                position[i] = "W"
        return position

    def generateOpeningBlack(self, position):
        blackPositions = self.swapPositions(position[:])
        moveList = self.generateOpening(blackPositions)
        solutions = []
        for moves in moveList:
            solutions.append(self.swapPositions(moves[:]))
        return solutions

    def generateMidgameEndgameBlack(self, position):
        blackPositions = self.swapPositions(position[:])
        moveList = self.generateMidgameEndgame(blackPositions)
        solutions = []
        for moves in moveList:
            solutions.append(self.swapPositions(moves[:]))
        return solutions

    def generateOpening(self, position):
        return self.generateAdd(position)
    

    def generateMidgameEndgame(self, position):
        count = 0
        for i in position:
            if(i=="W"):
                count+=1
        if(count == 3):
            return self.generateHopping(position)
        else:
            return self.generateMove(position)

    def generateAdd(self, position):
        positions = []
        for pos in range(len(position)):
            if position[pos] == "x":
                copy = position[:]
                copy[pos] = "W"
                if(self.closeMill(pos, copy)):
                    self.generateRemove(copy, positions)
                else:
                    positions.append(copy)
        return positions


    def generateMove(self, position):
        positions = []
        for pos in range(len(position)):
            if(position[pos] == "W"):
                neighbor = self.neighbors(pos)
                for node in neighbor:
                    if(position[node]=="x"):
                     copy = position[:]
                     copy[pos] = "x"
                     copy[node] = "W"
                     if(self.closeMill(node, copy)):
                         self.generateRemove(copy, positions)
                     else:
                         positions.append(copy)
        return positions


    def generateHopping(self, position):
        positions = []
        for pos in range(len(position)):
            if(position[pos] == "W"):
                for nPos in range(len(position)):
                    if(position[nPos] == "x"):
                        copy = position[:]
                        copy[pos] = "x"
                        copy[nPos] = "W"
                        if(self.closeMill(nPos, copy)):
                            self.generateRemove(copy, positions)
                        else:
                            positions.append(copy)
        return positions


    def generateRemove(self, position, positions):
        flag = 0
        for pos in range(len(position)):
            if(position[pos]=="B"):
                if(not self.closeMill(pos, position)):
                    copy = position[:]
                    copy[pos] = "x"
                    positions.append(copy)
                    flag = 1
        if(flag==0):
            positions.append(position)

    def closeMill(self, pos, board):
        currVal = board[pos]
        if(currVal == "W" or currVal == "B"):
            if(pos == 0):
                if(board[2] == currVal and board[4] == currVal):
                    return True
                elif(board[6] == currVal and board[18] == currVal):
                    return True
                return False
            elif(pos == 1):
                if(board[3] == currVal and board[5] == currVal):
                    return True
                elif(board[11] == currVal and board[20] == currVal):
                    return True
                return False
            elif(pos == 2):
                if(board[0] == currVal and board[4] == currVal):
                    return True
                elif(board[7] == currVal and board[15] == currVal):
                    return True
                return False
            elif(pos == 3):
                if(board[5] == currVal and board[1] == currVal):
                    return True
                elif(board[10] == currVal and board[17] == currVal):
                    return True
                return False
            elif(pos == 4):
                if(board[0] == currVal and board[2] == currVal):
                    return True
                elif(board[8] == currVal and board[12] == currVal):
                    return True
                return False
            elif(pos == 5):
                if(board[1] == currVal and board[3] == currVal):
                    return True
                elif(board[9] == currVal and board[14] == currVal):
                    return True
                return False
            elif(pos == 6):
                if(board[7] == currVal and board[8] == currVal):
                    return True
                elif(board[0] == currVal and board[18] == currVal):
                    return True
                return False
            elif(pos == 7):
                if(board[6] == currVal and board[8] == currVal):
                    return True
                elif(board[2] == currVal and board[15] == currVal):
                    return True
                return False
            elif(pos == 8):
                if(board[6] == currVal and board[7] == currVal):
                    return True
                elif(board[4] == currVal and board[12] == currVal):
                    return True
                return False
            elif(pos == 9):
                if(board[5] == currVal and board[14] == currVal):
                    return True
                elif(board[10] == currVal and board[11] == currVal):
                    return True
                return False
            elif(pos == 10):
                if(board[9] == currVal and board[11] == currVal):
                    return True
                elif(board[3] == currVal and board[17] == currVal):
                    return True
                return False
            elif(pos == 11):
                if(board[9] == currVal and board[10] == currVal):
                    return True
                elif(board[1] == currVal and board[20] == currVal):
                    return True
                return False
            elif(pos == 12):
                if(board[4] == currVal and board[8] == currVal):
                    return True
                elif(board[13] == currVal and board[14] == currVal):
                    return True
                elif(board[15] == currVal and board[18] == currVal):
                    return True
                return False
            elif(pos == 13):
                if(board[12] == currVal and board[14] == currVal):
                    return True
                elif(board[16] == currVal and board[19] == currVal):
                    return True
                return False
            elif(pos == 14):
                if(board[17] == currVal and board[20] == currVal):
                    return True
                elif(board[12] == currVal and board[13] == currVal):
                    return True
                elif(board[5] == currVal and board[9] == currVal):
                    return True
                return False
            elif(pos == 15):
                if(board[2] == currVal and board[7] == currVal):
                    return True
                elif(board[12] == currVal and board[18] == currVal):
                    return True
                elif(board[16] == currVal and board[17] == currVal):
                    return True
                return False
            elif(pos == 16):
                if(board[13] == currVal and board[19] == currVal):
                    return True
                elif(board[15] == currVal and board[17] == currVal):
                    return True
                return False
            elif(pos == 17):
                if(board[14] == currVal and board[20] == currVal):
                    return True
                elif(board[15] == currVal and board[16] == currVal):
                    return True
                elif(board[3] == currVal and board[10] == currVal):
                    return True
                return False
            elif(pos == 18):
                 if(board[0] == currVal and board[6] == currVal):
                    return True
                 elif(board[15] == currVal and board[12] == currVal):
                    return True
                 elif(board[19] == currVal and board[20] == currVal):
                    return True
                 return False
            elif(pos == 19):
                 if(board[13] == currVal and board[16] == currVal):
                    return True
                 elif(board[18] == currVal and board[20] == currVal):
                    return True
                 return False
            elif(pos == 20):
                 if(board[1] == currVal and board[11] == currVal):
                    return True
                 elif(board[14] == currVal and board[17] == currVal):
                    return True
                 elif(board[19] == currVal and board[18] == currVal):
                    return True
                 return False
        else:
            return False

    def neighbors(self, pos):
            if(pos == 0):
                return [1,2,6]
            elif(pos == 1):
                return [0,3,11]
            elif(pos == 2):
                return [0,3,4,7]
            elif(pos == 3):
                return [1,2,5,10]
            elif(pos == 4):
                return [2,5,8]
            elif(pos == 5):
                return [3,4,9]
            elif(pos == 6):
                return [0,7,18]
            elif(pos == 7):
                return [2,6,8,15]
            elif(pos == 8):
                return [4,7,12]
            elif(pos == 9):
                return [5,10,14]
            elif(pos == 10):
                return [3, 9, 11, 17]
            elif(pos == 11):
                return [1, 10, 20]
            elif(pos == 12):
                return [8, 13, 15]
            elif(pos == 13):
                return [12, 14, 16]
            elif(pos == 14):
                return [9, 13, 17]
            elif(pos == 15):
                return [7, 12, 16, 18]
            elif(pos == 16):
                return [13, 15, 17, 19]
            elif(pos == 17):
                return [10, 14, 16, 20]
            elif(pos == 18):
                 return [6, 15, 19]
            elif(pos == 19):
                 return [16, 18, 20]
            elif(pos == 20):
                 return [11, 17, 19]

