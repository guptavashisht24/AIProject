from board import Board
from sys import maxsize

board = Board()

class Result:
    def __init__(self, estimate = 0, position = ""):
        self.estimate = estimate
        self.position = position


class MiniMax:
    def __init__(self, start, depth, move):
        self.totalLeaves = 0
        self.depth = depth
        self.position = ""
        self.estimate = self.miniMaxEstimate(list(start),self.depth,move).estimate

    def countItems(self, board):
        white = 0
        black = 0
        for position in board:
            if(position == "W"):
                white+=1
            elif(position == "B"):
                black+=1
        return [white, black]

    def updatedStaticPtrs(self, position):
        currentMills = 0
        futureMills = 0
        for currPos in range(len(position)):
            if(position[currPos] == "W"):
               if(board.closeMill(currPos, position)):
                   currentMills+=1
        for currPos in range(len(position)):
            if(position[currPos] == "x"):
               copy = position[:]
               copy[currPos] = "W"
               if(board.closeMill(currPos, copy)):
                   futureMills+=1
        return 10*currentMills+5*futureMills



    def staticEstimation(self, position):
        self.totalLeaves+=1
        white, black = self.countItems(position)
        return white-black+self.updatedStaticPtrs(position)

    def miniMaxEstimate(self, position, depth, minmax):
        if(depth == 0):
           estimates = self.staticEstimation(position)
           result = Result(estimates)
           return result

        if(minmax == 1):
            movelist = board.generateOpening(position[:])
            ans = Result(-1*maxsize, "")
            for position in movelist:
                tempSol = self.miniMaxEstimate(position[:], depth-1, 0)
                if(tempSol.estimate > ans.estimate):
                    ans = tempSol
                    if(depth == self.depth):
                        self.position = position
            return ans
        else:
            movelist = board.generateOpeningBlack(position[:])
            ans = Result(maxsize, "")
            for position in movelist:
                tempSol = self.miniMaxEstimate(position[:], depth-1, 1)
                if(tempSol.estimate < ans.estimate):
                    ans = tempSol
            return ans

input_content = input()
input, output, depth = input_content.split(" ")
depth = int(depth)
with open(input) as f:
    initial_pos = f.readline()
    p = MiniMax(list(initial_pos),depth,1)
    f = open(output, "w")
    f.write("Board Position: "+"".join(p.position)+"\n"+"Positions evaluated by static estimation: "+str(p.totalLeaves)+".\n"+"MINIMAX ESTIMATE: "+str(p.estimate)+".")
    f.close()