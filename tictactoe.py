import os
os.system("clear")

class game():
    def __init__(self):
    	self.board = [" "," "," "," "," "," "," "," "," "," "]

    def disp(self):
    	print(" %s | %s | %s" %(self.board[1],self.board[2],self.board[3]))
    	print("___________")
    	print(" %s | %s | %s" %(self.board[4],self.board[5],self.board[6]))
    	print("___________")
    	print(" %s | %s | %s" %(self.board[7],self.board[8],self.board[9]))

    def update(self,bnum,player):
    	if self.board[bnum] == " ":
            self.board[bnum] = player

    def winner(self,player):
        for comb in [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]:
            result = True
            for bnum in comb:
                if self.board[bnum] != player:
                    result = False

            if result == True:
                    return True

        result = False

    def tie(self):
        used = 0
        for board in self.board:
            if board != " ":
                used += 1
            if used == 9:
                return True
            else:
                return False

    def reset(self):
        self.board = [" "," "," "," "," "," "," "," "," "," "]

    def ai(self,player):
        if self.board[5] == " ":
            self.update(5,player)

        for i in range(1,10):
            if self.board[i] == " ":
                self.update(i,player)
                break

g = game()

def refresh():
    os.system("clear")

    print ("\n                                                      TIC TAC TOE GAME                                                       ")

    g.disp()

while True:
    refresh()

    x = int(input("\n x) Choose (1-9)"))

    g.update(x, "X") 

    refresh()

    if g.winner("X"):
        print("\n X is the winner!!")
        again = input("\n Do you want to play again? (Y/N)")
        if again == "Y":
            g.reset()
            continue
        else:
            break

    if g.tie():
        print("\n Tie game!!")
        again = input("Do you want to play again? (Y/N)")
        if again == "Y":
            g.reset()
            continue
        else:
            break

    g.ai("0")

    refresh()

    if g.winner("0"):
        print("\n 0 is the winner!!")
        again = input("\n Do you want to play again? (Y/N)")
        if again == "Y":
            g.reset()
            continue
        else:
            break

    if g.tie():
        print("\n Tie game!!")
        again = input("Do you want to play again? (Y/N)")
        if again == "Y":
            g.reset()
            continue
        else:
            break