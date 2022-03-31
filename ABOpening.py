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
        self.estimate = self.miniMaxEstimate(list(start),self.depth,move, Result(-1*maxsize, ""), Result(maxsize, "")).estimate

    def countItems(self, board):
        white = 0
        black = 0
        for position in board:
            if(position == "W"):
                white+=1
            elif(position == "B"):
                black+=1
        return [white, black]

    def staticEstimation(self, board):
        self.totalLeaves+=1
        white, black = self.countItems(board)
        return white-black

    def miniMaxEstimate(self, position, depth, minmax, alpha, beta):
        if(depth == 0):
           estimates = self.staticEstimation(position)
           result = Result(estimates, position[:])
           return result

        if(minmax == 1):
            movelist = board.generateOpening(position[:])
            ans = Result(-1*maxsize, "")
            for position in movelist:
                tempSol = self.miniMaxEstimate(position[:], depth-1, 0, alpha, beta)
                if(tempSol.estimate > ans.estimate):
                    ans = tempSol
                    if(depth == self.depth):
                        self.position = position
                alpha = ans if(ans.estimate > alpha.estimate) else alpha
                if(beta.estimate <= alpha.estimate):
                    break
            return ans
        else:
            movelist = board.generateOpeningBlack(position[:])
            ans = Result(maxsize, "")
            for position in movelist:
                tempSol = self.miniMaxEstimate(position[:], depth-1, 1, alpha, beta)
                if(tempSol.estimate < ans.estimate):
                    ans = tempSol
                beta = ans if(ans.estimate < beta.estimate) else beta
                if(beta.estimate <= alpha.estimate):
                    break
            return ans

input_content = input()
input, output, depth = input_content.split(" ")
depth = int(depth)
with open(input) as f:
    initial_pos = f.readline()
    p = MiniMax(list(initial_pos),depth,1)
    f = open(output, "w")
    f.write(str(p.estimate)+"\n"+"".join(p.position)+"\n"+str(p.totalLeaves))
    f.close()