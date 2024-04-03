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
{sep * 40}
""")




welcome()