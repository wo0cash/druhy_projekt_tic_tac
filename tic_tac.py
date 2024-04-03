"""
tic_tac.py: druhý projekt do Engeto Online Python Akademie
author: Lukasz Orszulik 
email: luki93@seznam.cz
discord: discord: Lukasz Orszulik, wo0cash
"""

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
marks in a rows:
                        * horizontal
                        * vertical
                        * diagonal
{sep * 40}""")

def board():
    """Shows a baord for the game"""
    square = [""] * 9 #list of squares for placing stones
    return print(f"""
            +---+---+---+
            |{square[0] :^3}|{square[1] :^3}|{square[2] :^3}|
            +---+---+---+
            |{square[3] :^3}|{square[4] :^3}|{square[5] :^3}|   
            +---+---+---+         
            |{square[6] :^3}|{square[7] :^3}|{square[8] :^3}| 
            +---+---+---+  
          """)




#TODO players
#TODO placing stones
#TODO conditions for properly placing stones
#TODO cond. for only digits
#TODO cond. for placing stone over already used space
#TODO show updated grid
#TODO if there are 3 stones in a row ther is a winner
#TODO if ther is no space and no 3 stones in a row then end of game



#-----------Game----------
welcome()
board()