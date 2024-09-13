#Simple game
def welcome():
    """Welcome user and shows basic rules"""
    sep = "="
    return print(f"""
Welcome to Tic Tac Toe
{sep * 40}
GAME RULES:
Each player can place one mark or stone
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a horizontal, vertical and diagonal rows
{sep * 40}""")

def board():
    """Shows a baord for the game"""
    return print(f"""
            +---+---+---+
            |{square[0] :^3}|{square[1] :^3}|{square[2] :^3}|
            +---+---+---+
            |{square[3] :^3}|{square[4] :^3}|{square[5] :^3}|   
            +---+---+---+         
            |{square[6] :^3}|{square[7] :^3}|{square[8] :^3}| 
            +---+---+---+  
          """)
def ch_player(move_x):
    """Chooses player"""
    if move_x % 2 == 1:
        return "o"
    else:
        return "x"

def move(number):
    """Places a number on board(in a square list)"""
    if not number.isdigit() and 0 > number < 10:
        return print("You must type only digits between 1-9!")
    elif square[int(number)] != "":
        return print("This square is taken!")
    else:
        return number

def round():
    """Places stones on board"""
    move_count = 1
    while move_count <= 9:
        player = ch_player(move_count)
        print(f"Player {player}") 
        square[int(move(input("Type a number from 1-9: ")))-1] = player #move
        print(square)
        move_count += 1
    print("End game")

    




#TODO placing stones
#TODO conditions for properly placing stones
#TODO cond. for only digits
#TODO cond. for placing stone over already used space
#TODO show updated grid
#TODO if there are 3 stones in a row ther is a winner
#TODO if ther is no space and no 3 stones in a row then end of game

#-----------Game----------
square = [""] * 9 #list of squares for placing stones

welcome()
board()
print("Let's start the game!")
round()

#-----------Round---------



print(square)