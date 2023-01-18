import sys
import numpy as np

class TicTacToe:
    
    def __init__(self):
        self.board = np.array([['A1', 'A2', 'A3'], ['B1', 'B2', 'B3'], ['C1', 'C2', 'C3']])
        
        
    def boardprinter(self):
        for x in self.board:
            for y in x:
                print(y, end = " " )
            print('')
            
    def userinput(self):
        entry = input('Player 1 -- Choose your location: ').upper()
        solution = np.argwhere(self.board == entry)
        ##Above is not real code. Shows where the entry is found as argwhere pulls out info
        
        if(len(solution) == 0):
            print('This square has been played.')
            starter.userinput()

        x = solution[0][0]
        y = solution[0][1]
            
        ##Reset input as P1 made a mistake
            
        self.board[x][y] = 'X'
        if(starter.check() == True):
            sys.exit()
            
        print(starter.boardprinter())
        
    def userinput2(self):
        entry = input('Player 2 -- Choose your location: ').upper()
        
        solution = np.argwhere(self.board == entry)

        if(len(solution) == 0):
            print('This square has been played.')
            starter.userinput2()

        x = solution[0][0]
        y = solution[0][1]
            
        self.board[x][y] = 'O'
        if(starter.check() == True):
            sys.exit()
            
        print(starter.boardprinter())
        
    
    def check(self):
        
        a = 0
        b = 0
        while a < 3:
            b = 0
            if(self.board[a][b] == self.board[a][b+1] == self.board[a][b+2]):
                print('Winner!')
                starter.boardprinter()
                return True
            a = a + 1

        while b < 3:
            a = 0
            if(self.board[a][b] == self.board[a+1][b] == self.board[a+2][b]):
                print('Winner!')
                starter.boardprinter()
                return True
            b = b + 1     

        if(self.board[0][0] == self.board[1][1] == self.board[2][2]):
                print('Winner!')
                starter.boardprinter()
                return True           

        if(self.board[2][0] == self.board[1][1] == self.board[0][2]):
                print('Winner!')
                starter.boardprinter()
                return True                  
            
            
        counter = 0
        for x in self.board:
            for y in x:
                if(y == 'X' or y == 'O'):
                    counter = counter + 1
        if(counter == 9):
            print('Game is over.')
            starter.boardprinter()
            return True
        else:
            return False

starter = TicTacToe()
print(starter.boardprinter())

while(starter.check() == False):
    starter.userinput()
    starter.userinput2()