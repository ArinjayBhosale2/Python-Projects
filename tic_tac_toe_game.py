#Tic Tac Toe game by Arinjay (MILESTONE PROJECT 1)
def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])
    


def start():
    print("Welcome to Tic Tac Toe by Arinjay!")
    print("\n")

def player1_choice():
    player1_choice = "Wrong"
    while player1_choice not in ["X","O"]:
         player1_choice = input("Player 1 ,Do you want to be X or O: ")

         if player1_choice not in  ["X","O"]:
             print("Sorry,enter either X or O!")
    return player1_choice


def player2_choice(player1_choice):
        
    if player1_choice == "X":
        player2_choice = "O"
    else:
        player2_choice = "X"
    return player2_choice




def inpt(a):
    player1 = int(input(" player1: Choose(1-9): "))
    board[player1]= a
    display_board(board)
def p2_inpt(b):
    player2 = int(input(" player2: Choose(1-9): "))
    board[player2] = b
    display_board(board)




    
def player2_win(board):
       if [board[1],board[2],board[3]] == [b,b,b]:
         print("Player2 has won")
         return True
       elif [board[1],board[4],board[7]] == [b,b,b]:
         print("Player2 has won")
         return True
       elif [board[8],board[5],board[2]] == [b,b,b]:
         print("Player2 has won")
         return True
       elif [board[1],board[5],board[9]] == [b,b,b]:
         print("Player2 has won")
         return True
       elif [board[4],board[5],board[6]] == [b,b,b]:
         print("Playwer2 has won")
         return True
       elif [board[3],board[5],board[7]] == [b,b,b]:
         print("Player2 has won")
         return True
       elif [board[3],board[6],board[9]] == [b,b,b]:
         print("Player2 has won")
         return True
       return False

def player1_win(board):
       if [board[1],board[2],board[3]] == [a,a,a]:
         print("Player1 has won")
         return True
       elif [board[1],board[4],board[7]] == [a,a,a]:
         print("Player1 has won")
         return True
       elif [board[8],board[5],board[2]] == [a,a,a]:
         print("Player1 has won")
         return True
       elif [board[1],board[5],board[9]] == [a,a,a]:
         print("Player1 has won")
         return True
       elif [board[4],board[5],board[6]] == [a,a,a]:
         print("Player1 has won")
         return True
       elif [board[3],board[5],board[7]] == [a,a,a]:
         print("Player1 has won")
         return True
       elif [board[3],board[6],board[9]] == [a,a,a]:
         print("Player1 has won")
         return True
       return False

            
def gameon_choice():
    choice = 'wrong'
    while choice not in ['Y','N']:
        choice = input('Keep playing?{Y/N}: ')
        if choice not in ['Y','N']:
            print("Sorry,.invalid choice")
    if choice == 'Y':
        return True
    else:
        return False
#Initialisation of the game   
start()
board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
a = player1_choice()
b = player2_choice(a)
q = 1
p1 = [a, a, a]
p2 = [b, b, b]
d = len(board)
while q<(d-3):
    q = q+1
    inpt(a)
    if player1_win(board) == True:
        break
    
    if ' ' not in board:
            print('Draw!')
            break
        
    p2_inpt(b)
    if player2_win(board) == True:
        break
    
    else:
        continue
    
    

